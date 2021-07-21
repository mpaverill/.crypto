# find # of time-steps in BTC csv
# fill alt csv's with zeros for missing data
# fill in tensor one asset at-a-time
# Start date is 03/31/13
# timestamps correspond to equivalent dates between assets
import csv
from add_zeros import add_zeros
import numpy as np

def tensor_format():

    # number of timesteps in BTC dataset
    # with open('DATA_BITFINEX/btcusd.csv',"r", newline='', encoding='utf-8-sig') as file:
    #     reader = csv.reader(file, delimiter = ",")
    #     data = list(reader)
    #     max_timesteps = (len(data)) - 1
    
    # add zeros to each asset's missing data one asset at-a-time
    max_timesteps = 3420458
    with open('tensor_alts.csv', newline='', encoding='utf-8-sig') as file:
        reader = csv.reader(file, delimiter = ",")
        alt_list = list(reader)
    for asset in alt_list:
        path = 'DATA_BITFINEX/' + asset[0] + '.csv'
        with open(path,"r", newline='', encoding='utf-8-sig') as file:
            reader = csv.reader(file, delimiter = ",")
            data = list(reader)
            timesteps = (len(data)) - 1
        add_zeros(path, timesteps, max_timesteps)
        break


tensor_format()