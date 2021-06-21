from usd_pairs import usd_pairs
import bitfinex
import pandas as pd
import numpy as np
import datetime
import time
import os


# Create a function to fetch the data
def fetch_data(start, stop, symbol, interval, tick_limit, step):
    # Create api instance
    api_v2 = bitfinex.bitfinex_v2.api_v2()

    data = []
    start = start - step
    while start < stop:
        start = start + step
        end = start + step
        res = api_v2.candles(symbol=symbol, interval=interval, limit=tick_limit, start=start, end=end)
        data.extend(res)
        print('Retrieving data from {} to {} for {}'.format(pd.to_datetime(start, unit='ms'),
                                                            pd.to_datetime(end, unit='ms'), symbol))
        time.sleep(1.5)
    return data


# Define query parameters
bin_size = '15m'
limit = 1000
time_step = 1000 * 900 * limit

t_start = datetime.datetime(2021, 6, 1, 0, 0)
t_start = time.mktime(t_start.timetuple()) * 1000

t_stop = datetime.datetime(2021, 6, 3, 23, 59)
t_stop = time.mktime(t_stop.timetuple()) * 1000

pairs = usd_pairs()

save_path = './DATA_BITFINEX'

if os.path.exists(save_path) is False:
    os.mkdir(save_path)

for pair in pairs:
    pair_data = fetch_data(start=t_start, stop=t_stop, symbol=pair, interval=bin_size, tick_limit=limit, step=time_step)

    # Remove error messages
    ind = [np.ndim(x) != 0 for x in pair_data]
    pair_data = [i for (i, v) in zip(pair_data, ind) if v]

    # Create pandas data frame and clean data
    names = ['time', 'open', 'close', 'high', 'low', 'volume']
    df = pd.DataFrame(pair_data, columns=names)
    df.drop_duplicates(inplace=True)
    df['time'] = pd.to_datetime(df['time'], unit='ms')
    df.set_index('time', inplace=True)
    df.sort_index(inplace=True)

    print('Done downloading data. Saving to .csv.')
    print(df)
    df.to_csv(r'./DATA_BITFINEX/1INCH.csv', index=True)
    print('Done saving data. Moving to next pair.')
    break
print('Done retrieving data')