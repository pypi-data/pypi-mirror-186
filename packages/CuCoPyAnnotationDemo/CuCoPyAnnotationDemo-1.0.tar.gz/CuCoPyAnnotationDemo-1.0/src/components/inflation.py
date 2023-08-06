from . import utils

def get_equivalent_worth(country_code, filename_, value=1, from_date=None, to_date=None):
    """
    get_equivalent_worth validates the given date(s) and retrieves their corresponding consumer price index.
    To calculate the equivalent worth, the function divides the recent cpi by the older cpi and multiplies that fraction with the desired value. 
    
    :param value: the monetary value of which to get the equivalent worth.
    :param from_date: the date at which (value) was recorded.
    :param to_date: the date for which to get the equivalent worth for. If None, will default to the most recent date for which a cpi is recorded.
    :return: the amount of money needed at (to_date) for it to have the same purchasing power as (value) in (from_date)
    """
    df = utils.get_dataframe(country_code, filename_)
    from_cpi = utils.get_cpi(from_date, df)
    to_cpi = utils.get_cpi(to_date, df)
    if from_cpi == None or to_cpi == None:
        return None
    else:
        return value * (to_cpi/from_cpi)

def _get_proportional_purchasing_power(df_cpi, from_date=None, to_date=None):
    """
    _get_proportional_purchasing_power is a helper function for get_adjusted_worth. It retrieves the given dates' cpis and divides the older cpi by the recent cpi.

    :param from_date: the date at which an initial value was recorded.
    :param to_date: the date for which to get the adjusted purchasing power.
    :return: the relative purchasing power (percentage based). 
    """
    from_cpi = utils.get_cpi(from_date, df_cpi)
    to_cpi = utils.get_cpi(to_date, df_cpi)
    if from_cpi == None or to_cpi == None:
        return None
    else:
        return from_cpi/to_cpi


def get_buying_power(country_code, filename_, value=1, from_date=None, to_date=None):
    """
    get_adjusted_worth validates the given date(s) and passes them to _get_proportional_purchasing_power to get the relative, percentage-based purchasing power.
    The relative purchasing power is then multiplied by the amount of money specified in (value).
    
    :param value: the monetary value of which to get the adjusted worth.
    :param from_date: the date at which (value) was recorded.
    :param to_date: the date for which to get the adjusted worth for. If None, will default to the most recent date for which a cpi is recorded.
    :return: the remaining purchasing power money has at (to_date) compared to (from_date).
    """
    df = utils.get_dataframe(country_code, filename_)
    ppp = _get_proportional_purchasing_power(df, from_date=from_date, to_date=to_date)

    if ppp == None:
        return None
    else:
        return value*ppp