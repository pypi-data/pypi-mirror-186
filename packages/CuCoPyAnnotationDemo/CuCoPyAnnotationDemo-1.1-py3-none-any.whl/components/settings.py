import pathlib

WORLD_PATH = pathlib.Path(__file__).parent.absolute().joinpath("../data/")
WORLD_CPI = WORLD_PATH.joinpath("ConsumerPriceIndex.csv")
WORLD_ER = WORLD_PATH.joinpath("ExchangeRate_LCU_per_USD.csv")
WORLD_CY = WORLD_PATH.joinpath("_CurrencyYield.csv")

DOWNLOAD_CPI = "https://api.worldbank.org/v2/en/indicator/FP.CPI.TOTL?downloadformat=csv"
DOWNLOAD_ER = "https://api.worldbank.org/v2/en/indicator/PA.NUS.FCRF?downloadformat=csv"
