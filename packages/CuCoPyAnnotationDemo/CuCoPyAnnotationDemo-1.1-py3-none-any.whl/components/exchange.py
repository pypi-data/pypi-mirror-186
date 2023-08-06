from . import utils

def get_exchanged_value(from_country_code, to_country_code, filename_, value=1, date=None):
    """
    get_exchanged_value looks up the official exchange rate provided by the International Monetary Fund and exchanges the given value from one currency to the other.
    :param from_country_code: the country in which the value was recorded.
    :param to_country_code: the country to whichs currency should be exchanged.
    :param filename_: the file path to the exchange rate table.
    :param value: the amount of money to be exchanged.
    :param date: the date for which the exchange should take place.
    :return: the exchanged worth of the initial value in another currency.
    """
    if date == None:
        raise ValueError("Missing date.")
    if value <= 0:
        raise ValueError("Entered value is less than, or equal to, zero.")

    from_df = utils.get_dataframe(from_country_code, filename_)
    to_df = utils.get_dataframe(to_country_code, filename_)

    from_rate = utils.get_exchange_rate(date, from_df)
    to_rate = utils.get_exchange_rate(date, to_df)

    if from_rate == None or to_rate == None:
        return None
    else:
        return value * (to_rate/from_rate)
