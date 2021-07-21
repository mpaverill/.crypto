import csv
from csv import writer
import pandas as pd
import numpy as np

def add_zeros(file_name, num_rows, max_rows):
    miss_rows = max_rows - num_rows
    names = ['Time', 'Open', 'Close', 'High', 'Low', 'Volume']
    df = pd.DataFrame(np.zeros((miss_rows, 6)), dtype=float, columns=names)

    with open(file_name, newline='', encoding='utf-8-sig') as file:
        file = csv.reader(file, dialect='excel', delimiter=',', quotechar='|')
        next(file, None)  #skip the headers
        for row in file: #iterates through each ASSET
            df.append(row)
    print(df)


    # new_row = [0.0,0.0]
    # with open(file_name, 'a+', newline='', encoding='utf-8-sig') as asset:
    #     # Create a writer object from csv module
    #     csv_writer = writer(asset)
    #     # Add contents of list as last row in the csv file
    #     for i in range(num_rows):
    #         csv_writer.writerow(new_row)

add_zeros(file_name='DATA_BITFINEX/dogeusd.csv', max_rows = 3420458, num_rows = 900000)