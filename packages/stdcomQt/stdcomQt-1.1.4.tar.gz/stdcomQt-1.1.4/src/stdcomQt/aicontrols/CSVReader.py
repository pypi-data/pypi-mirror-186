import numpy as np
import time
from six.moves import range

import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv('PID_train_data.csv')
    t = data['Time']
    u = data[['Q1', 'Q2']]
    y = data[['T1', 'T2']]
