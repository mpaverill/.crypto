import bitfinex
import datetime
import time

from requests.models import parse_header_links

# Define query parameters
pair = 'btcusd' # Currency pair of interest
bin_size = '15m' # This will return 1 minute data
limit = 1000    # We want the maximum of 1000 data points 

# # Define the start date
# t_start = datetime.datetime(2018, 4, 1, 0, 0)
# t_start = time.mktime(t_start.timetuple()) * 1000

# # Define the end date
# t_stop = datetime.datetime(2018, 4, 2, 0, 0)
# t_stop = time.mktime(t_stop.timetuple()) * 1000
# result = api_v2.candles(symbol=pair, interval=bin_size,  
#                         limit=limit, start=t_start, end=t_stop)
# print(len(result))

def fetch_data(start, stop, symbol, interval, tick_limit, step):
    # Create api instance
    api_v2 = bitfinex.bitfinex_v2.api_v2()
    data = []
    start = start - step
    while start < stop:
        start = start + step
        end = start + step
        res = api_v2.candles(symbol=symbol, interval=interval,
                             limit=tick_limit, start=start,
                             end=end)
        data.extend(res)
        print(str(start) + '/' + str(stop))
        time.sleep(2)
    return data
result = fetch_data

# Set step size
time_step = 90000000

# Define the start date 
t_start = datetime.datetime(2018, 4, 1, 0, 0)
t_start = time.mktime(t_start.timetuple()) * 1000

# Define the end date
t_stop = datetime.datetime(2018, 4, 12, 0, 0)
t_stop = time.mktime(t_stop.timetuple()) * 1000
pair_data = fetch_data(start=t_start, stop=t_stop, symbol=pair,
                    interval=bin_size, tick_limit=limit, 
                    step=time_step)
print(pair_data)                    
print(len(pair_data))