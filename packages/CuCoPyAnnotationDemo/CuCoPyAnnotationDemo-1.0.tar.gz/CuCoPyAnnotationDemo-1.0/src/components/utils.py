import datetime, dateutil.relativedelta
import pandas as pd
import numpy as np
from .settings import WORLD_CPI, WORLD_CY, WORLD_ER

def _get_value(date, df, type_, fpath=None):
    """
    _get_value looks up the value of a cell for a given date (date) in a table provided by the Federal Statistical Office.

    :param date: the date for which to get a cpi for.
    :param df: the dataframe in which to look for the value.
    :param type_: the type of information in the file (cpi? exchange value?)
    :param fpath: the filepath of the dataframe. Used for recursive miss prevention.
    :return: the value of a cell in a dataframe for a given date (date). 
    """
    #df_cpi = pd.read_csv(DATA_CPI, sep=";")
    try:
        target_cpi = df[str(date.year)].values[0]
        if np.isnan(target_cpi):
            try:
                alt_code = get_exchange_rate_region(date, df['Country Code'].values[0])
                alt_df = get_dataframe(alt_code, fpath)
                val = _get_value(date=date, df=alt_df, type_ = type_, fpath = fpath)
                return val
            except Exception:
                raise ("Not a number.")
        return float(target_cpi)
    except Exception as e:
        f_occ = _get_occurence(df)
        l_occ = _get_occurence(df, True)
        raise ValueError("Couldn't find a(n) {} for the given date. Supported dates for the given currency range from {} to {}".format(type_, f_occ, l_occ))

def _get_occurence(df, do_reverse = False):
    """
    _get_occurence finds and returns the first/ last date for which a value was recorded in a dataframe.

    :param df: the dataframe to look through.
    :param do_reverse: specifies, whether to look for the first/ last occurence.
    :return: the year of the first/ last occurence.
    """
    import math

    if do_reverse:
        df = df[df.columns[::-1]]

    for col in df:
        val = df[col].values[0]
        try:
            float(val)
            if not math.isnan(float(val)):
                return df[col].name
        except ValueError:
            continue

def get_cpi(date, df_cpi):
    return _get_value(date, df_cpi, "cpi", WORLD_CPI)

def get_exchange_rate(date, df_er):
    return _get_value(date, df_er, "exchange rate", WORLD_ER)

def get_valid_date(date):
    """
    get_valid_date tries to convert a given string into a valid datetime object (YYYY-mm-dd).

    :param date: the date to check for validity. May be str or datetime.datetime object.
    :return: the given date as a datetime.datetime object in a "YYYY-mm-dd" format. 
    """
    try:
        date_ = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        return date_
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-mm-dd")

def validate_dates(dates):
    """
    validate_dates turns a list of dates into valid dates using the \'get_valid_date\' method.

    :param dates: the list of dates to check for validity. May be list of str or datetime.datetime objects. Alternatively, when no second date is specified, it will return a list containing the first date and today's date from a month ago.
    :return: the given list's dates as datetime.datetime object in a "YYYY-mm-dd" format. 
    """
    dates[0] = get_valid_date(dates[0])
    if dates[1] == None:
        dates[1] = datetime.date.today() - dateutil.relativedelta.relativedelta(years=1)
    else:
        dates[1] = get_valid_date(dates[1])

    if dates[0] > dates[1]:
        raise ValueError("Invalid order of dates. \'from_date\' has to be earlier than \'to_date\'.")

    return dates

def get_dataframe(country_code, filename_):
    """
    get_dataframe extracts the country's row specified by \'country_code\'.

    :param country_code: the list of dates to check for validity. May be list of str or datetime.datetime objects. Alternatively, when no second date is specified, it will return a list containing the first date and today's date from a month ago.
    :return: the given list's dates as datetime.datetime object in a "YYYY-mm-dd" format. 
    """
    df = pd.read_csv(filename_, skiprows=4)
    matching_indices = df.index[df['Country Code'] == country_code].tolist()
    if len(matching_indices) == 0:
        raise ValueError("No matching dataset found for the given country code ({})".format(country_code))
    res_df = df.loc[matching_indices]
    return res_df

def get_exchange_rate_region(date, country_code):
    """
    get_exchange_rate_region looks up the country code of a newly adopted currency.

    :param date: the date at which to check for the alternative currency.
    :param country_code: the country code for which to find its alternative for.
    :return: the newly adopted currency code.
    """
    df = pd.read_csv(WORLD_CY, skiprows=4)
    vals = df.loc[df['Country Code'] == country_code][['New Country Code', 'Yielded']].values
    if vals[0][1] <= date.year:
        return vals[0][0]
