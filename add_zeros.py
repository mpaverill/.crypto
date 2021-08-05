import csv
from csv import writer
import pandas as pd
import numpy as np

def add_zeros(file_name, num_rows, max_rows):
    miss_rows = max_rows - num_rows
    names = ['time', 'open']
    df1 = pd.DataFrame(np.zeros((miss_rows, 2)), dtype=float, columns=names)
    
    df2 = pd.read_csv('DATA_BITFINEX/test.csv')
    del df2['Unnamed: 0']
    del df2['volume']
    del df2['low']
    del df2['high']
    del df2['close']

    df3 = df1.append(df2)
    print(df3)

#LEFT OFF APPENDING ASSET DF TO ZEROS DF. THE RESULTING DF WILL CONVERTED TO CSV AND THEN PLACED INTO THE TENSOR



    # with open(file_name, newline='', encoding='utf-8-sig') as file:
    #     file = csv.reader(file, dialect='excel', delimiter=',', quotechar='|')
    #     next(file, None)  #skip the headers
    #     for row in file: #iterates through each ASSET
    #         for value in row:
    #             value = float(value)
    #             df.append(value)
            

    # new_row = [0.0,0.0]
    # with open(file_name, 'a+', newline='', encoding='utf-8-sig') as asset:
    #     # Create a writer object from csv module
    #     csv_writer = writer(asset)
    #     # Add contents of list as last row in the csv file
    #     for i in range(num_rows):
    #         csv_writer.writerow(new_row)

add_zeros(file_name='DATA_BITFINEX/test.csv', max_rows = 45, num_rows = 30)