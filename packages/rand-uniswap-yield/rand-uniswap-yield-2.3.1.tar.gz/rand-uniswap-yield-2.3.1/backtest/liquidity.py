import math
import numpy as np
import pandas as pd


def get_amount0(sqrtA, sqrtB, liquidity, decimals):

    if sqrtA > sqrtB:
        (sqrtA, sqrtB) = (sqrtB, sqrtA)

    amount0 = (liquidity * 2**96 * (sqrtB - sqrtA) / sqrtB / sqrtA) / 10**decimals

    return amount0


def get_amount1(sqrtA, sqrtB, liquidity, decimals):

    if sqrtA > sqrtB:
        (sqrtA, sqrtB) = (sqrtB, sqrtA)

    amount1 = liquidity * (sqrtB - sqrtA) / 2**96 / 10**decimals

    return amount1


def get_initial_amounts(
    target: float,
    sqrt_min: float,
    sqrt_max: float,
    sqrt_token0: float,
    price: float,
    decimal_diff: int,
):

    # Calculate delta liquidity using target and get required amounts for tokens
    if sqrt_token0 > sqrt_min and sqrt_token0 < sqrt_max:
        deltaL = target / (
            (sqrt_token0 - sqrt_min)
            + (((1 / sqrt_token0) - (1 / sqrt_max)) * (price * 10 ** (decimal_diff)))
        )
        amount1 = deltaL * (sqrt_token0 - sqrt_min)
        amount0 = deltaL * ((1 / sqrt_token0) - (1 / sqrt_max)) * 10 ** (decimal_diff)

    elif sqrt_token0 < sqrt_min:
        deltaL = target / (((1 / sqrt_min) - (1 / sqrt_max)) * (price))
        amount1 = 0
        amount0 = deltaL * ((1 / sqrt_min) - (1 / sqrt_max))

    else:
        deltaL = target / (sqrt_max - sqrt_min)
        amount1 = deltaL * (sqrt_max - sqrt_min)
        amount0 = 0

    return amount0, amount1


def get_initial_token_ratio(
    amount0: float, amount1: float, initial_price: float, base: int
):
    if base == 0:
        amount1_in_amount0 = amount1 / initial_price
        total_amount0 = amount0 + amount1_in_amount0
        amount0_ratio = amount0 / total_amount0 * 100
        amount1_ratio = amount1_in_amount0 / total_amount0 * 100
    elif base == 1:
        # [] need to implement for base 1, until then exception
        raise Exception("Base 1 not implemented yet")

    return amount0_ratio, amount1_ratio


def get_amounts(asqrt, asqrtA, asqrtB, liquidity, decimal0, decimal1):

    sqrt = (np.sqrt(asqrt * 10 ** (decimal1 - decimal0))) * (2**96)
    sqrtA = np.sqrt(asqrtA * 10 ** (decimal1 - decimal0)) * (2**96)
    sqrtB = np.sqrt(asqrtB * 10 ** (decimal1 - decimal0)) * (2**96)

    if sqrtA > sqrtB:
        (sqrtA, sqrtB) = (sqrtB, sqrtA)

    if sqrt <= sqrtA:

        amount0 = get_amount0(sqrtA, sqrtB, liquidity, decimal0)
        return amount0, 0

    elif sqrt < sqrtB and sqrt > sqrtA:
        amount0 = get_amount0(sqrt, sqrtB, liquidity, decimal0)

        amount1 = get_amount1(sqrtA, sqrt, liquidity, decimal1)

        return amount0, amount1

    else:
        amount1 = get_amount1(sqrtA, sqrtB, liquidity, decimal1)
        return 0, amount1


# Use 'get_liquidity' function to calculate liquidity as a function of amounts and price range


def get_liquidity0(sqrtA, sqrtB, amount0, decimals):
    if sqrtA > sqrtB:
        (sqrtA, sqrtB) = (sqrtB, sqrtA)

    liquidity = amount0 / ((2**96 * (sqrtB - sqrtA) / sqrtB / sqrtA) / 10**decimals)
    return liquidity


def get_liquidity1(sqrtA, sqrtB, amount1, decimals):

    if sqrtA > sqrtB:
        (sqrtA, sqrtB) = (sqrtB, sqrtA)

    liquidity = amount1 / ((sqrtB - sqrtA) / 2**96 / 10**decimals)
    return liquidity


def get_liquidity(asqrt, asqrtA, asqrtB, amount0, amount1, decimal0, decimal1):

    sqrt = (np.sqrt(asqrt * 10 ** (decimal1 - decimal0))) * (2**96)
    sqrtA = np.sqrt(asqrtA * 10 ** (decimal1 - decimal0)) * (2**96)
    sqrtB = np.sqrt(asqrtB * 10 ** (decimal1 - decimal0)) * (2**96)

    if sqrtA > sqrtB:
        (sqrtA, sqrtB) = (sqrtB, sqrtA)

    if sqrt <= sqrtA:
        liquidity0 = get_liquidity0(sqrtA, sqrtB, amount0, decimal0)
        return liquidity0

    elif sqrt < sqrtB and sqrt > sqrtA:
        liquidity0 = get_liquidity0(sqrt, sqrtB, amount0, decimal0)
        liquidity1 = get_liquidity1(sqrtA, sqrt, amount1, decimal1)
        liquidity = liquidity0 if liquidity0 < liquidity1 else liquidity1
        return liquidity

    else:
        liquidity1 = get_liquidity1(sqrtA, sqrtB, amount1, decimal1)
        return liquidity1


def get_token_amounts(
    range_min: float,
    range_max: float,
    investment_target: float,
    initial_price: float,
    decimal: int,
    base: int,
):
    """
    Function to calculate token amounts and ratios from a range of prices, investment target, and initial price.

    :param range_min: Minimum price range
    :param range_max: Maximum price range
    :param investment_target: Investment target
    :param initial_price: Initial price
    :param decimal: Number of decimal places
    :param base: Base token 0 or 1
    :return: Dict of token amounts and ratios

    """

    # Calculate my liquidity based on supplied mini and maxi arguments
    SMIN = np.sqrt(range_min * 10 ** (decimal))
    SMAX = np.sqrt(range_max * 10 ** (decimal))

    # Calculate base price and sqrt price of base token
    # If base is zero (using pool0 token)
    if base == 0:
        sqrt0 = np.sqrt(initial_price * 10 ** (decimal))
    # If base is one (using pool1 token)
    elif base == 1:
        sqrt0 = np.sqrt(1 / initial_price * 10 ** (decimal))

    # Get amounts for initial investment for both token
    amount0, amount1 = get_initial_amounts(
        target=investment_target,
        sqrt_min=SMIN,
        sqrt_max=SMAX,
        sqrt_token0=sqrt0,
        initial_price=initial_price,
        decimal_diff=decimal,
    )
    # Get the pct ratio of token0 and token1
    amount0_ratio, amount1_ratio = get_initial_token_ratio(
        amount0=amount0, amount1=amount1, initial_price=initial_price, base=base
    )

    return {
        "amount0": amount0,
        "amount1": amount1,
        "amount0_ratio": amount0_ratio,
        "amount1_ratio": amount1_ratio,
    }


def get_amounts_combinations(
    range_min: float,
    range_max: float,
    investment_target_amount: float,
    decimal: int,
    base: int,
):
    """
    Function to iterate over a permutation of ranges and calculate the required LP liquidity for each combination

    :param range_min: minimum range
    :param range_max: maximum range
    :param initial_price: initial price of token
    :param investment_target_amount: target investment
    :param decimal: decimal places of token
    :param base: base token 0 or 1
    """

    # Create array to hold values
    results = []
    range_arr = []
    # Iterate over range_min and range_max values
    for i in range(range_min + 1, range_max):
        range_arr.append(i)
        # Get amounts for initial investment for both token
        results.append(
            get_token_amounts(
                range_min=range_min,
                range_max=range_max,
                investment_target=investment_target_amount,
                initial_price=i,
                decimal=decimal,
                base=base,
            )
        )
    df = pd.DataFrame(results)
    df.index = range_arr

    return df


def price_to_tick(p):
    return math.floor(math.log(p, 1.0001))
