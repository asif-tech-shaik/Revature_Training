"""Module for Interest Calculation"""


def simple_interest(prin,ny,ratein):
    """
    calculating the Simple interest rate
    :param princple: principal amount
    :param ny: no of years
    :param rateIn: rate of interest
    :return: Simple interest and Total amount
    """
    si = prin * ny * ratein / 100
    amount=prin + si
    return si,amount


def compound_interest(prin,ny,ratein):
    """
    calculating the compound interest rate
    :param princple: priniciple amount
    :param ny: no of years
    :param rateIn: rate of interest
    :return: total amount
    """
    amount=prin * (1+(ratein/ny)) ** (1 * ny)
    return amount
