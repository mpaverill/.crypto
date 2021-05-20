import numpy as np
import csv

def add_zeros(file_name, num_rows):
        with open(file_name, 'a+', newline='') as asset:
        # Create a writer object from csv module
        csv_writer = writer(asset)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(

#determine the # of timesteps in timeseries
with open('DATA/BTC.csv', newline='', encoding='utf-8-sig') as btc:
    file = csv.reader(btc, dialect='excel', delimiter='\n', quotechar='|')
    i = 0
    for row in file:
        if i == 0:
            headers = row[i]
        i += 1  
samples = i
print(samples-1)

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

        #add zeros to missing data in each asset
        max_rows = samples - 1

        #index the the opening price for each timestep one asset at a time
        with open(path, newline='') as asset:
            file = csv.reader(asset, dialect='excel', delimiter=',', quotechar='|')
            next(file, None)  # skip the headers
            for j in file:
                num = float(j[1])
            break
            

#left off creating a function to add zeros to the missing data of each asset