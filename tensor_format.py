# find # of time-steps in BTC csv
# fill alt csv's with zeros for missing data
# fill in tensor one asset at-a-time
# Start date is 03/31/13
# timestamps correspond to equivalent dates between assets
import csv
from add_zeros import add_zeros
import numpy as np
import pandas as pd
from pandasgui import show

def tensor_format():
    
    # fill tensor with timesteps and find max number of timesteps using BTC
    with open('DATA_BITFINEX/btcusd.csv',"r", newline='', encoding='utf-8-sig') as file:
        next(file, None)  #skip the headers
        reader = csv.reader(file, delimiter = ",")
        data = list(reader)
        max_timesteps = (len(data))
        timesteps = []
        i = 0
        for row in data:
            timestamp = row[0]
            timesteps.append(timestamp)
            i += 1
    col_names = ['time']
    tensor = pd.DataFrame(data=timesteps, dtype=float, columns=col_names)      

    # add zeros to missing data and insert into tensor
    with open('tensor_alts.csv', newline='', encoding='utf-8-sig') as file:
        reader = csv.reader(file, delimiter = ",")
        alt_list = list(reader)
        j = 1
    for asset in alt_list:
        path = 'DATA_BITFINEX/' + asset[0] + '.csv'
        with open(path,"r", newline='', encoding='utf-8-sig') as file:
            reader = csv.reader(file, delimiter = ",")
            data = list(reader)
            num_timesteps = (len(data)) - 1
        asset_df = add_zeros(path, num_timesteps, max_timesteps)
        tensor[asset[0]] = asset_df
        print(str(j) + '/13 complete')
        j += 1
    del tensor['time']
    del tensor['dogeusd']
    del tensor['adausd']
    del tensor['etcusd']
    del tensor['bchnusd']
    del tensor['dshusd']
    del tensor['zecusd']
    del tensor['dotusd']
    del tensor['xlmusd']
    # Get names of indexes for which column Age has value 30
    indexNames = tensor[ tensor['eosusd'] == 0.0 ].index
    # Delete these row indexes from dataFrame
    tensor.drop(indexNames , inplace=True)
    print(tensor)
    tensor.to_csv('tensor.csv', index=False)
    print('Done building tensor')
    
tensor_format()