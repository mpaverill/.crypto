from Historic_Crypto import HistoricalData

# HistoricalData((TICKER), (TIMESTEP), (START_DATE), (END_DATE))
# TICKER = STR; TIMESTEP = INT; START_DATE = ####-##-##-##-##; END_DATE = ####-##-##-##-## OR DEFAULT = CURRENT DATE
ETH = HistoricalData('ETH-USD',300,'2021-04-11-00-00').retrieve_data()
print(ETH)