import pandas as pd


def chart1(dpd, base, myliquidity, verbose):

    if base == 0:
        # feeV is myfee0 + myfee1 * close price (token1)
        dpd["feeV"] = (dpd["myfee0"]) + (dpd["myfee1"] * dpd["close"])
        #
        dpd["amountV"] = (dpd["amount0"]) + (dpd["amount1"] * dpd["close"])
        dpd["amountunb"] = (dpd["amount0unb"]) + (dpd["amount1unb"] * dpd["close"])
        dpd["fgV"] = (dpd["fee0token"]) + (dpd["fee1token"] * dpd["close"])
        dpd["feeusd"] = dpd["feeV"] * (
            dpd["pool.totalValueLockedUSD"].iloc[0]
            / (
                dpd["pool.totalValueLockedToken1"].iloc[0] * dpd["close"].iloc[0]
                + (dpd["pool.totalValueLockedToken0"].iloc[0])
            )
        )
        # -------
        dpd["feeVbase0"] = dpd["myfee0"] + (dpd["myfee1"] * dpd["close"])

    elif base == 1:
        dpd["feeV"] = (dpd["myfee0"] / dpd["close"]) + dpd["myfee1"]
        dpd["amountV"] = (dpd["amount0"] / dpd["close"]) + dpd["amount1"]
        dpd["feeVbase0"] = dpd["myfee0"] + (dpd["myfee1"] * dpd["close"])
        dpd["amountunb"] = (dpd["amount0unb"] / dpd["close"]) + dpd["amount1unb"]
        dpd["fgV"] = (dpd["fee0token"] / dpd["close"]) + dpd["fee1token"]
        dpd["feeusd"] = dpd["feeV"] * (
            dpd["pool.totalValueLockedUSD"].iloc[0]
            / (
                dpd["pool.totalValueLockedToken1"].iloc[0]
                + (dpd["pool.totalValueLockedToken0"].iloc[0] / dpd["close"].iloc[0])
            )
        )

    # Chart #1
    data = dpd[
        [
            "myfee0",
            "myfee1",
            "fgV",
            "feeV",
            "feeusd",
            "amountV",
            "ActiveLiq",
            "amountunb",
            "amount0",
            "amount1",
            "close",
        ]
    ]
    # Fill nans with zero
    data = data.fillna(0)

    # Calculate resampled temp DF by SUM
    temp = data.resample("D").sum()
    # Calculate resampled temp DF by MEAN
    temp2 = data.resample("D").mean()
    # Calculate resampled temp DF by FIRST
    temp3 = data.resample("D").first()
    # Calculate resampled temp DF by LAST
    temp4 = data.resample("D").last()

    # Create DataFrame
    df_1 = temp[["myfee0", "myfee1", "feeV", "fgV", "feeusd"]].copy()
    # Define ActiveLiq from mean resample
    df_1["ActiveLiq"] = temp2["ActiveLiq"].copy()
    # Define amount value and amount unbounded from resample first
    df_1[["amountV", "amountunb"]] = temp3[["amountV", "amountunb"]].copy()
    # Define shifted amount values from resampled last
    df_1[["amountV_shift"]] = temp4[["amountV"]]

    # Calculate S1%, Unbounded%, Concentrated Liquidity Multiplier, and Unbounded fees
    df_1["S1%"] = df_1["feeV"] / df_1["amountV"] * 100  # *365
    df_1["unb%"] = df_1["fgV"] / df_1["amountunb"] * 100  # *365
    df_1["MultiplierLiq"] = df_1["S1%"] / df_1["unb%"]
    df_1["feeunb"] = df_1["amountV"] * df_1["unb%"] / 100

    forecast = dpd["feeVbase0"].sum() * myliquidity * df_1["ActiveLiq"].mean()
    base_ccy = "token0" if base == 0 else "token1"
    if verbose:
        print(
            "---------------------------------- Backtest -----------------------------------"
        )
        print(
            "(Bounded) LP position returned:",
            df_1["feeV"].sum() / df_1["amountV"].iloc[0] * 100,
            "% in",
            len(df_1.index),
            "days, for an APR of",
            df_1["feeV"].sum() / df_1["amountV"].iloc[0] * 365 / len(df_1.index) * 100,
        )
        print(
            "(Unbounded) LP  position returned:",
            df_1["feeunb"].sum() / df_1["amountV"].iloc[0] * 100,
            "% in",
            len(df_1.index),
            "days, for an APR of",
            df_1["feeunb"].sum()
            / df_1["amountV"].iloc[0]
            * 365
            / len(df_1.index)
            * 100,
        )

        print(
            "Fee in token0 and token1:", dpd["myfee0"].sum(), "/", dpd["myfee1"].sum()
        )
        print("Total fee in USD", df_1["feeusd"].sum())
        print("Your liquidity was active for:", df_1["ActiveLiq"].mean(), "%")
        print("Forecast fee value in", base_ccy, ":", forecast)
        print(
            "---------------------------------- Backtest -----------------------------------"
        )

    # Chart #2
    final2 = temp3[["amountV", "amount0", "amount1", "close"]].copy()
    final2["feeV"] = temp["feeV"].copy()
    final2[["amountV_shift"]] = temp4[["amountV"]]

    final2["HODL"] = (
        final2["amount0"].iloc[0] / final2["close"] + final2["amount1"].iloc[0]
    )

    final2["IL"] = final2["amountV_shift"] - final2["HODL"]
    final2["ActiveLiq"] = temp2["ActiveLiq"].copy()
    final2["feecumsum"] = final2["feeV"].cumsum()
    final2["PNL"] = final2["feecumsum"] + final2["IL"]  # -Bfinal['gas']

    final2["HODLnorm"] = final2["HODL"] / final2["amountV"].iloc[0] * 100
    final2["ILnorm"] = final2["IL"] / final2["amountV"].iloc[0] * 100
    final2["PNLnorm"] = final2["PNL"] / final2["amountV"].iloc[0] * 100
    final2["feecumsumnorm"] = final2["feecumsum"] / final2["amountV"].iloc[0] * 100
    ch2 = final2[["amountV", "feecumsum"]]
    ch3 = final2[["ILnorm", "PNLnorm", "feecumsumnorm"]]

    # Chart #3

    final3 = pd.DataFrame()
    final3["amountV"] = data["amountV"]

    final3["amountV_shift"] = data["amountV"].shift(-1)
    final3["HODL"] = data["amount0"].iloc[0] / data["close"] + data["amount1"].iloc[0]

    final3["amountV_shift"].iloc[-1] = final3["HODL"].iloc[-1]
    final3["IL"] = final3["amountV_shift"] - final3["HODL"]
    final3["feecumsum"] = data["feeV"][::-1].cumsum()
    final3["PNL"] = final3["feecumsum"] + final3["IL"]
    final3["HODLnorm"] = final3["HODL"] / final3["amountV"].iloc[0] * 100
    final3["ILnorm"] = final3["IL"] / final3["amountV"].iloc[0] * 100
    final3["PNLnorm"] = final3["PNL"] / final3["amountV"].iloc[0] * 100
    final3["feecumsumnorm"] = final3["feecumsum"] / final3["amountV"].iloc[0] * 100

    ch2 = final3[["amountV", "feecumsum"]]
    ch3 = final3[["ILnorm", "PNLnorm", "feecumsumnorm"]]

    return df_1, final2, final3
