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

#get the path name for each asset
with open('top_200.csv', newline='', encoding='utf-8-sig') as top200:
    file = csv.reader(top200, dialect='excel', delimiter=',', quotechar='|')
    for row in file:
        path1 = 'DATA/'
        path2 = row[0]
        path3 = '.csv'
        path = path1 + path2 + path3
        #index the the opening price for each timestep one asset at a time
        with open(path, newline='') as asset:
            file = csv.reader(asset, dialect='excel', delimiter=',', quotechar='|')
            next(file, None)  # skip the headers
            for j in file:
                num = float(j[1])
                print(type(num))
            break
            

#left off converting each opening price to floats one asset at a time, not one timestep at a time
#need to manipulate every asset but BTC to have zeros in the timesteps that don't have data