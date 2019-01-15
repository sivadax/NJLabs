# Load the Pandas libraries with alias 'pd'
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt



# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
data = pd.read_csv("aple.us.txt")
# Preview the first 5 lines of the loaded data
data.head()

print (data)

