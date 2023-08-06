import numpy as np
from .liquidity import *
from .graphql_query import *
from .charts import *

"""
    Bactest method steps:
    1. Fetch data from Graph
    2. Calculate decimals for token0 and token1
    3. Apply decimals for feeGrowthGlobal0X128 and feeGrowthGlobal1X128 as fg0 and fg1
    4. Calculate fees earned by unbounded unit of liquidity in one period
"""


def backtest(
    range_min: float,
    range_max: float,
    target: float,
    base: int = 0,
    address: str = "",
    startfrom: int = 0,
    network: str = "",
    dpd=None,
    verbose=False,
):
    """
    Backtesting method for calculating returns on a specific strategy.

    :param address (str): Address of the strategy to backtest
    :param startfrom (int): Unix timestamp of the start date
    :param network (int): Network of the strategy
    :param range_min (float): Minimum bound of the range of the strategy
    :param range_max (float): Maximum bound of the range of the strategy
    :param target (float): Target investment amount of the strategy
    :param base (int): Base token to calculate for (token0 or token1)
    :return:     dpd, df_query, df_1, df_2
        - dpd (pd.DataFrame): Returns the dataframe used for calculations
        - df_query (pd.DataFrame): Returns the original dataframe of the query
        - df_1 (pd.DataFrame): Returns the dataframe of Chart 3 and DPD
        - df_2 (pd.DataFrame): Returns the dataframe of Chart 2

    """

    if dpd is None:
        dpd = graph(network, address, startfrom)
    df_query = dpd.copy()

    # Decide if dpd is integer or time index
    if isinstance(dpd.index, pd.DatetimeIndex):
        # Convert to integer range
        dpd.index = range(len(dpd.index))

    # Calculate decimals for pool tokens
    decimal0 = dpd.iloc[0]["pool.token0.decimals"]
    decimal1 = dpd.iloc[0]["pool.token1.decimals"]
    decimal = decimal1 - decimal0
    # Apply decimals for feeGrowthGlobal
    dpd["fg0"] = ((dpd["feeGrowthGlobal0X128"]) / (2**128)) / (10**decimal0)
    dpd["fg1"] = ((dpd["feeGrowthGlobal1X128"]) / (2**128)) / (10**decimal1)

    # Calculate fg0 and fg1 (fee earned by an unbounded unit of liquidity in one period)
    # F_Unb = fg(t) — fg(t-1)
    dpd["fg0shift"] = dpd["fg0"].shift(-1)
    dpd["fg1shift"] = dpd["fg1"].shift(-1)
    dpd["fee0token"] = dpd["fg0"] - dpd["fg0shift"]
    dpd["fee1token"] = dpd["fg1"] - dpd["fg1shift"]

    # Calculate my liquidity based on supplied range_min and range_max arguments
    SMIN = np.sqrt(range_min * 10 ** (decimal))
    SMAX = np.sqrt(range_max * 10 ** (decimal))

    # Calculate base price and sqrt price of base token
    # If base is zero (using pool0 token)
    if base == 0:
        sqrt0 = np.sqrt(dpd["close"].iloc[-1] * 10 ** (decimal))
        dpd["price0"] = dpd["close"]
    # If base is one (using pool1 token)
    elif base == 1:
        sqrt0 = np.sqrt(1 / dpd["close"].iloc[-1] * 10 ** (decimal))
        dpd["price0"] = 1 / dpd["close"]

    # Get amounts for initial investment for both token
    amount0, amount1 = get_initial_amounts(
        target=target,
        sqrt_min=SMIN,
        sqrt_max=SMAX,
        sqrt_token0=sqrt0,
        price=dpd["price0"].iloc[0],
        decimal_diff=decimal,
    )

    # Get the pct ratio of token0 and token1
    amount0_ratio, amount1_ratio = get_initial_token_ratio(
        amount0=amount0,
        amount1=amount1,
        initial_price=dpd["price0"].iloc[-1],
        base=base,
    )
    # first_date = dpd['periodStartUnix'].iloc[-1].strftime("%m/%d/%Y, %H:%M:%S")
    # first_close_price = dpd['close'].iloc[-1]
    # print(f"Closing price on {first_date}: {first_close_price}")
    # Use get_liquidity function from liquidity module
    myliquidity = get_liquidity(
        dpd["price0"].iloc[-1],
        range_min,
        range_max,
        amount0,
        amount1,
        decimal0,
        decimal1,
    )
    if verbose:
        print("Amounts:", amount0, "/", amount1)
        print(
            "Amount ratios:",
            round(amount0_ratio, 2),
            "% /",
            round(amount1_ratio, 2),
            "%",
        )
        print("My liquidity:", myliquidity)

    # Calculate active liquidity

    dpd["ActiveLiq"] = 0
    dpd["amount0"] = 0
    dpd["amount1"] = 0
    dpd["amount0unb"] = 0
    dpd["amount1unb"] = 0

    # Calculate liquidity for base currency (token1)
    if base == 0:
        for i, row in dpd.iterrows():
            # If both bounds are within high and low prices
            # If high price > range_minmum bound and low price < range_maxmum bound
            if dpd["high"].iloc[i] > range_min and dpd["low"].iloc[i] < range_max:
                dpd.iloc[i, dpd.columns.get_loc("ActiveLiq")] = (
                    (
                        min(range_max, dpd["high"].iloc[i])
                        - max(dpd["low"].iloc[i], range_min)
                    )
                    / (dpd["high"].iloc[i] - dpd["low"].iloc[i])
                    * 100
                )
            else:
                dpd.iloc[i, dpd.columns.get_loc("ActiveLiq")] = 0

            # Calculate bounded amounts with liquidity module
            amounts = get_amounts(
                dpd["price0"].iloc[i],
                range_min,
                range_max,
                myliquidity,
                decimal0,
                decimal1,
            )
            dpd.iloc[i, dpd.columns.get_loc("amount0")] = amounts[1]
            dpd.iloc[i, dpd.columns.get_loc("amount1")] = amounts[0]

            # Calculate unbounded amounts with liquidity module
            amountsunb = get_amounts(
                (dpd["price0"].iloc[i]),
                1.0001 ** (-887220),
                1.0001**887220,
                1,
                decimal0,
                decimal1,
            )
            dpd.iloc[i, dpd.columns.get_loc("amount0unb")] = amountsunb[1]
            dpd.iloc[i, dpd.columns.get_loc("amount1unb")] = amountsunb[0]

    # Calculate liquidity for non-base currency (token1)
    elif base == 1:
        for i, row in dpd.iterrows():
            # If both bounds are within high and low prices
            if (1 / dpd["low"].iloc[i]) > range_min and (
                1 / dpd["high"].iloc[i]
            ) < range_max:
                dpd.iloc[i, dpd.columns.get_loc("ActiveLiq")] = (
                    (
                        min(range_max, 1 / dpd["low"].iloc[i])
                        - max(1 / dpd["high"].iloc[i], range_min)
                    )
                    / ((1 / dpd["low"].iloc[i]) - (1 / dpd["high"].iloc[i]))
                    * 100
                )
            else:
                dpd.iloc[i, dpd.columns.get_loc("ActiveLiq")] = 0

            # Calculate bounded amounts with liquidity module
            amounts = get_amounts(
                (dpd["price0"].iloc[i] * 10 ** (decimal)),
                range_min,
                range_max,
                myliquidity,
                decimal0,
                decimal1,
            )
            dpd.iloc[i, dpd.columns.get_loc("amount0")] = amounts[0]
            dpd.iloc[i, dpd.columns.get_loc("amount1")] = amounts[1]

            # Calculate unbounded amounts with liquidity module
            amountsunb = get_amounts(
                (dpd["price0"].iloc[i]),
                1.0001 ** (-887220),
                1.0001**887220,
                1,
                decimal0,
                decimal1,
            )
            dpd.iloc[i, dpd.columns.get_loc("amount0unb")] = amountsunb[0]
            dpd.iloc[i, dpd.columns.get_loc("amount1unb")] = amountsunb[1]

    # Final fee calculation
    # Total fees * my liquidity * active liquidity / by 100
    dpd["myfee0"] = dpd["fee0token"] * myliquidity * dpd["ActiveLiq"] / 100
    dpd["myfee1"] = dpd["fee1token"] * myliquidity * dpd["ActiveLiq"] / 100

    # Calculate volatility based on price
    window_size = 24  #  Daily volatility
    # Calculate rolling volatility with a daily rolling window and annualize dpd
    dpd["volatility0_ann"] = dpd["price0"].pct_change().rolling(window_size).std() * (
        252**0.5
    )

    # Create human readable timestamp indexes
    dpd.index = pd.to_datetime(dpd["periodStartUnix"], unit="s")

    # Get charting for more detailed metrics
    a1, a2, a3 = chart1(dpd, base, myliquidity, verbose)

    # Format data for plotting -- Chart 3 and DPD
    # Concat dataframes and drop duplicate columns
    df_1 = pd.concat([dpd, a3], axis=1).T.drop_duplicates().T
    df_1.sort_index(inplace=True)

    # Iterate and drop non-norm columns if normalized exists
    norm_cols = []
    for i in df_1.columns:
        if "norm" in i:
            norm_cols.append(i)

    for i in df_1.columns:
        for f in norm_cols:
            if f.split("norm")[0] == i:
                df_1.drop(columns=i, axis=1, inplace=True)

    # Drop other columns used for calculations
    df_1.drop(
        columns=[
            "periodStartUnix",
            "fg0shift",
            "fg1shift",
            "pool.token0.decimals",
            "pool.token1.decimals",
            "pool.totalValueLockedToken0",
            "pool.totalValueLockedToken1",
            "pool.totalValueLockedUSD",
            "feeGrowthGlobal0X128",
            "feeGrowthGlobal1X128",
            "amountV_shift",
        ],
        inplace=True,
    )

    # Format data for plotting -- Chart 1 and Chart 2
    # Concat dataframes and drop duplicate columns
    df_2 = pd.concat([a1, a2], axis=1).reset_index().T.drop_duplicates().T
    # Set date as an index
    df_2.set_index("periodStartUnix", inplace=True)
    df_2.sort_index(inplace=True)
    # Iterate and drop non-norm columns if normalized exists
    norm_cols = []
    for i in df_2.columns:
        if "norm" in i:
            norm_cols.append(i)

    for i in df_2.columns:
        for f in norm_cols:
            if f.split("norm")[0] == i:
                df_2.drop(columns=i, axis=1, inplace=True)

    return dpd, df_query, df_1, df_2


def get_token_amounts_and_IL(
    dataframe: pd.DataFrame,
    target_investment_amount: float,
    range_min: float,
    range_max: float,
) -> pd.DataFrame:

    # Calculate decimals for pool tokens
    decimal0 = dataframe.iloc[0]["pool.token0.decimals"]
    decimal1 = dataframe.iloc[0]["pool.token1.decimals"]
    decimal = decimal1 - decimal0

    # Calculate my liquidity based on supplied mini and maxi arguments
    sqrt_min = np.sqrt(range_min * 10 ** (decimal))
    sqrt_max = np.sqrt(range_max * 10 ** (decimal))

    # Calculate base price and sqrt price of base token
    # If base is zero (using pool0 token)
    sqrt_token0 = np.sqrt(dataframe.close.iloc[-1] * 10 ** (decimal))
    dataframe["price0"] = dataframe["close"]

    # Calculate delta liquidity using target and get required amounts for tokens
    if sqrt_token0 > sqrt_min and sqrt_token0 < sqrt_max:
        deltaL = target_investment_amount / (
            (sqrt_token0 - sqrt_min)
            + (
                ((1 / sqrt_token0) - (1 / sqrt_max))
                * (dataframe.close.iloc[-1] * 10 ** (decimal))
            )
        )
        amount1 = deltaL * (sqrt_token0 - sqrt_min)
        amount0 = deltaL * ((1 / sqrt_token0) - (1 / sqrt_max)) * 10 ** (decimal)

    elif sqrt_token0 < sqrt_min:
        deltaL = target_investment_amount / (
            ((1 / sqrt_min) - (1 / sqrt_max)) * (dataframe.close.iloc[-1])
        )
        amount1 = 0
        amount0 = deltaL * ((1 / sqrt_min) - (1 / sqrt_max))

    else:
        deltaL = target_investment_amount / (sqrt_max - sqrt_min)
        amount1 = deltaL * (sqrt_max - sqrt_min)
        amount0 = 0

    myliquidity = get_liquidity(
        asqrt=dataframe["price0"].iloc[-1],
        asqrtA=range_min,
        asqrtB=range_max,
        amount0=amount0,
        amount1=amount1,
        decimal0=decimal0,
        decimal1=decimal1,
    )

    dpd = dataframe.copy()
    dpd["ActiveLiq"] = 0
    dpd["amount0"] = 0
    dpd["amount1"] = 0

    # Decide if dpd is integer or time index
    if isinstance(dpd.index, pd.DatetimeIndex):
        # Convert to integer range
        dpd.index = range(len(dpd.index))

    for i, row in dpd.iterrows():
        if dpd["high"].iloc[i] > range_min and dpd["low"].iloc[i] < range_max:
            dpd.iloc[i, dpd.columns.get_loc("ActiveLiq")] = (
                (
                    min(range_max, dpd["high"].iloc[i])
                    - max(dpd["low"].iloc[i], range_min)
                )
                / (dpd["high"].iloc[i] - dpd["low"].iloc[i])
                * 100
            )
        else:
            dpd.iloc[i, dpd.columns.get_loc("ActiveLiq")] = 0

        amounts = get_amounts(
            dpd["price0"].iloc[i], range_min, range_max, myliquidity, decimal0, decimal1
        )
        dpd.iloc[i, dpd.columns.get_loc("amount0")] = amounts[1]
        dpd.iloc[i, dpd.columns.get_loc("amount1")] = amounts[0]

    dpd["HODL"] = dpd["amount0"].iloc[0] + dpd["close"] * dpd["amount1"].iloc[0]
    dpd["amountV"] = (dpd["amount0"]) + (dpd["amount1"] * dpd["close"])

    dpd["IL_5050"] = (dpd["amountV"] / dpd["HODL"] - 1) * 100

    hodl_value_100_token0 = (
        dpd["amount0"].iloc[0] + dpd["amount1"].iloc[0] * dpd["close"].iloc[0]
    )
    dpd["IL_100_token0"] = (
        (dpd["amountV"] - hodl_value_100_token0) / hodl_value_100_token0 * 100
    )

    hodl_value_100_token1 = (dpd["amount0"].iloc[0] / dpd["close"].iloc[0]) + dpd[
        "amount1"
    ].iloc[0]
    dpd["IL_100_token1"] = (
        (dpd["amountV"] - hodl_value_100_token1 * dpd["close"]) / dpd["close"] * 100
    )

    hedge_initial_value = dpd["amount1"].iloc[0] * dpd["close"].iloc[0]
    dpd["amountHedge"] = hedge_initial_value - (
        hedge_initial_value * (dpd["close"] / dpd["close"].iloc[0])
    )
    dpd["IL_5050_w_hedge"] = (
        (dpd["amountV"] + dpd["amountHedge"]) / dpd["HODL"] - 1
    ) * 100

    hodl_value_100_token0 = (
        dpd["amount0"].iloc[0] + dpd["amount1"].iloc[0] * dpd["close"].iloc[0]
    )
    dpd["IL_100_token0"] = (
        (dpd["amountV"] - hodl_value_100_token0) / hodl_value_100_token0 * 100
    )
    dpd["IL_100_token0_w_hedge"] = (
        (dpd["amountV"] + dpd["amountHedge"] - hodl_value_100_token0)
        / hodl_value_100_token0
        * 100
    )

    hodl_value_100_token1 = (dpd["amount0"].iloc[0] / dpd["close"].iloc[0]) + dpd[
        "amount1"
    ].iloc[0]
    dpd["IL_100_token1"] = (
        (dpd["amountV"] - hodl_value_100_token1 * dpd["close"]) / dpd["close"] * 100
    )
    dpd["IL_100_token1_w_hedge"] = (
        (dpd["amountV"] + dpd["amountHedge"] - hodl_value_100_token1 * dpd["close"])
        / dpd["close"]
        * 100
    )

    return dpd


def get_range_min_max_prices(
    dpd: pd.DataFrame, range_min: float, range_max: float, current_price: float
) -> pd.DataFrame:
    df_artificial_dpd = dpd.copy(deep=True)

    # Get DataFrame to be able to split into 3 pieces
    modulo = 3
    fx = df_artificial_dpd.shape[0] % modulo
    if fx == 1 or fx == 2:
        df_artificial_dpd = df_artificial_dpd.iloc[:-fx]

    # Generate artificial prices by covering all price ranges
    s1 = np.linspace(current_price, range_max, int(dpd.shape[0] / 3))
    s2 = np.linspace(range_max, range_min, int(dpd.shape[0] / 3))
    s3 = np.linspace(range_min, current_price, int(dpd.shape[0] / 3))
    df_artificial_dpd["close"] = np.concatenate((s1, s2, s3))

    return df_artificial_dpd
