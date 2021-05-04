import numpy as np
import csv

#determine the # of timesteps in timeseries
with open('DATA/BTC.csv', newline='', encoding='utf-8-sig') as btc:
    file = csv.reader(btc, dialect='excel', delimiter='\n', quotechar='|')
    i = 0
    for row in file:
        if i == 0:
            headers = row[i]
        i += 1  
samples = i

#construct empty timeseries tensor
float_data = np.zeros((samples-1, 200))

#populate each column of the numpy array with single asset
for i in range(200):
    with open('top_200.csv', newline='', encoding='utf-8-sig') as top200:
        file = csv.reader(top200, dialect='excel', delimiter=',', quotechar='|')
        for row in file:
            print(i)
            path1 = 'DATA/'
            path2 = row[i]
            path3 = '.csv'
            path = path1 + path2 + path3
            print(path)
            # with open(path, newline='') as asset:
            #     file = csv.reader(asset, dialect='excel', delimiter='\n', quotechar='|')
            #     for j in range(samples):

#left off trying to take the first 8 digits of the opening price for each asset and filling in each timestep one asset at a time