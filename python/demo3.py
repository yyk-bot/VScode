import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_table('./Sample.txt',header= 10)
data.set_index('wavelength', inplace=True)
column_data = data.iloc[:, 1:].values
x_values = data.index.values

data.plot(y=column_data, ytype='line', kind='line', title='Wavelength vs Line Plots', xlabel='Wavelength', ylabel='Values')
data.plot(y=column_data[1:], ytype='scatter', kind='scatter', title='Wavelength vs Scatter Plots', xlabel='Wavelength', ylabel='Values', secondary_y=True)