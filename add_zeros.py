import pandas as pd
import numpy as np

def add_zeros(file_name, num_rows, max_rows):
    miss_rows = max_rows - num_rows
    names = ['open']
    df1 = pd.DataFrame(np.zeros((miss_rows, 1)), dtype=float, columns=names)

    df2 = pd.read_csv(file_name)
    zeros = df1['open'].tolist()
    prices = df2['open'].tolist()
    zeros.extend(prices)

    return zeros