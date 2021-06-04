import bitfinex
 
# Create api instance of the v2 API
api_v2 = bitfinex.bitfinex_v2.api_v2()
result = api_v2.candles()
print(result)