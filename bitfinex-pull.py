#IF RUNNING THIS DATA GRAB AT A 1 MINUTE RESOLUTION GOING BACK TO 2013...IT IS ESTIMATED TO TAKE 12.07 DAYS

from usd_pairs import usd_pairs
from fetch_data import fetch_data
import pandas as pd #pip install pandas
import numpy as np
import datetime
import time
import os

def data_pull():
    # Define query parameters
    bin_size = '1m' #resolution in minutes
    limit = 1000
    resolution_minutes = 1 #resolution in minutes
    time_step = 1000 * (60*resolution_minutes) * limit

    t_start = datetime.datetime(2013, 1, 1, 0, 0)
    t_start = time.mktime(t_start.timetuple()) * 1000

    t_stop = datetime.datetime(2021, 7, 10, 23, 59)
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
        path1 = './DATA_BITFINEX/'
        path2 = pair
        path3 = '.csv'
        path4 = path2.replace(':','_')
        path = path1 + path4 + path3
        print(path)
        df.to_csv(path, index=True)
        print('Done saving data. Moving to next pair.')
    print('Done retrieving data')

data_pull()