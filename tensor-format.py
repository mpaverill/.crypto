import numpy as np
import csv
from csv import writer

from numpy.core.fromnumeric import shape

print("Building Timeseries Tensor")
def add_zeros(file_name, num_rows):
    new_row = [0.0,0.0]
    with open(file_name, 'a+', newline='', encoding='utf-8-sig') as asset:
        # Create a writer object from csv module
        csv_writer = writer(asset)
        # Add contents of list as last row in the csv file
        for i in range(num_rows):
            csv_writer.writerow(new_row)

#determine the # of timesteps in timeseries
with open('DATA/BTC.csv', newline='', encoding='utf-8-sig') as btc:
    file = csv.reader(btc, dialect='excel', delimiter='\n', quotechar='|')
    i = 0
    for row in file:
        if i == 0:
            headers = row[i]
        i += 1
#total number of timesteps available (based on BTC data)
max_samples = i-1

#construct empty timeseries tensor
float_data = np.zeros((max_samples, 200))

#populate each column of the numpy array with single asset

#get the path name for each asset
with open('top_200.csv', newline='', encoding='utf-8-sig') as top200:
    file = csv.reader(top200, dialect='excel', delimiter=',', quotechar='|')
    c = 0
    for row in file: #iterates through each ASSET
        path1 = 'DATA/'
        path2 = row[0]
        path3 = '.csv'
        path = path1 + path2 + path3
        r = 0

        #count number of samples in order to determine the number of missing data points
        with open(path, newline='') as asset:
            file = csv.reader(asset, dialect='excel', delimiter=',', quotechar='|')
            next(file, None)  #skip the headers
            num_samples = 0 
            for j in file: #iterates through each ROW of the asset
                num_samples += 1
        #add zeros to missing data in each asset
        miss_rows = max_samples - num_samples
        if miss_rows != 0:
            add_zeros(path, miss_rows)

        #index the the opening price for each timestep one asset at a time
        with open(path, newline='') as asset:
            file = csv.reader(asset, dialect='excel', delimiter=',', quotechar='|')
            next(file, None)  #skip the headers
            for j in file: #iterates through each ROW of the asset
                openPrice = float(j[1])
                float_data[r][c] = openPrice
                r += 1
        c += 1
        phrase = '/200 Datasets Complete'
        num_complete = str(c)
        print(num_complete + phrase)

print(float_data[:][:])

# save to csv file
np.savetxt('float_data.csv', float_data, delimiter=',')

#Finished filling float_data tensor with opening prices in float format. I think the next step is normalizing each column (asset) on a scale of 0-1.
