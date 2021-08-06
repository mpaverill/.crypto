import pandas as pd
import numpy as np

def add_zeros(file_name, num_rows, max_rows):
    miss_rows = max_rows - num_rows
    names = ['open']
    df1 = pd.DataFrame(np.zeros((miss_rows, 1)), dtype=float, columns=names)

    df2 = pd.read_csv(file_name)
    del df2['Unnamed: 0']
    del df2['volume']
    del df2['low']
    del df2['high']
    del df2['close']
    del df2['time']
    df3 = pd.concat([df1, df2])
    df4 = df3['open'].tolist()

    return df4