from cucopy import tools
from cucopy.components import settings, exchange

# VALID: 1,2
# INVALID: 3-7

import datetime, pytest

TOLERANCE = 0.1

configs = [
    ["USA", "CAN", settings.WORLD_ER, 1, "1997-09-23"],
    ["USA", "CAN", settings.WORLD_ER, 1, None],
    ["ABC", "CAN", settings.WORLD_ER, 1, "2010-09-23"],
    ["USA", "ABC", settings.WORLD_ER, 1, "2010-09-23"],
    ["USA", "CAN", settings.WORLD_ER, 1, "2010-13-32"],
    ["USA", "CAN", settings.WORLD_ER, 1, "2032-09-12"],
    ["USA", "CAN", settings.WORLD_ER, -1, "2010-09-23"]
]

def test_control_param():
    conf = configs[0]
    assert exchange.get_exchanged_value(
            from_country_code=conf[0], 
            to_country_code=conf[1], 
            filename_=conf[2],
            value=conf[3],
            date=datetime.datetime.strptime(conf[4], '%Y-%m-%d').date()) == pytest.approx(1.3845980283, TOLERANCE)

def test_missing_date():
    conf = configs[1]
    with pytest.raises(ValueError):
        exchange.get_exchanged_value(
            from_country_code=conf[0], 
            to_country_code=conf[1], 
            filename_=conf[2],
            value=conf[3],
            date=None)

def test_unknown_country_code_1():
    conf = configs[2]
    with pytest.raises(ValueError):
        exchange.get_exchanged_value(
            from_country_code=conf[0], 
            to_country_code=conf[1], 
            filename_=conf[2],
            value=conf[3],
            date=datetime.datetime.strptime(conf[4], '%Y-%m-%d').date())
    
def test_unknown_country_code_2():
    conf = configs[3]
    with pytest.raises(ValueError):
        exchange.get_exchanged_value(
            from_country_code=conf[0], 
            to_country_code=conf[1], 
            filename_=conf[2],
            value=conf[3],
            date=datetime.datetime.strptime(conf[4], '%Y-%m-%d').date())

def test_invalid_date():
    conf = configs[4]
    with pytest.raises(ValueError):
        exchange.get_exchanged_value(
            from_country_code=conf[0], 
            to_country_code=conf[1], 
            filename_=conf[2],
            value=conf[3],
            date=datetime.datetime.strptime(conf[4], '%Y-%m-%d').date())

def test_exceeding_date():
    conf = configs[5]
    with pytest.raises(ValueError):
        exchange.get_exchanged_value(
            from_country_code=conf[0], 
            to_country_code=conf[1], 
            filename_=conf[2],
            value=conf[3],
            date=datetime.datetime.strptime(conf[4], '%Y-%m-%d').date())

def test_negative_value():
    conf = configs[6]
    with pytest.raises(ValueError):
        exchange.get_exchanged_value(
            from_country_code=conf[0], 
            to_country_code=conf[1], 
            filename_=conf[2],
            value=conf[3],
            date=datetime.datetime.strptime(conf[4], '%Y-%m-%d').date())
