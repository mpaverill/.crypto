from Historic_Crypto import HistoricalData
from Historic_Crypto import Cryptocurrencies
from Historic_Crypto import LiveCryptoData

# HistoricalData((TICKER), (TIMESTEP), (START_DATE), (END_DATE))
# TICKER = STR; TIMESTEP = INT; START_DATE = YYYY-MM-DD-HH-MM; END_DATE = YYYY-MM-DD-HH-MM OR DEFAULT = CURRENT DATE
Cryptocurrencies().find_crypto_pairs()
STORJ = Cryptocurrencies(coin_search = 'LUNA', extended_output=True).find_crypto_pairs()
STORJ = HistoricalData('LUNA-USD',300,'2020-04-11-00-00','2020-04-13-00-00').retrieve_data()