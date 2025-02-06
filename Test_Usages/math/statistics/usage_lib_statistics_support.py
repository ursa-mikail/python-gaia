
import os, sys
import numpy as np
import math
from scipy import stats

# point to path
lib_path = os.path.abspath('../../../Libraries/data')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../Libraries/math/statistics')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../Libraries/display/console')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../Libraries/display/plot')
sys.path.append(lib_path)

# import package from path
from data_generator import data_generator   # file name
from data_processor import data_processor
from data_manipulator import data_manipulator
from lib_statistics import lib_statistics

from display_console import display_console
from display_plot import display_plot


import pandas as pd

def declare_object_start(object_ids):
    if type(object_ids) is list:
        for i in range(0, len(object_ids)):
            print("=====[" + object_ids[i] + " Start]===== ")
    else:
        print("=====[" + object_ids + " Start]===== ")
    return None

def declare_object_end(object_ids):
    if type(object_ids) is list:
        for i in range(0, len(object_ids)):
            print("=====[" + object_ids[i] + " End]===== ")
    else:
        print("=====[" + object_ids + " End]===== ")
    return None

####################################
# data
####################################
# 5 observations(row), 3 variables (column)
v1 = [4.0, 4.2, 3.9, 4.3, 4.1]
v2 = [2.0, 2.1, 2.0, 2.1, 2.2]
v3 = [0.60, 0.59, 0.58, 0.62, 0.63]

observed_data_00 = [29, 24, 22, 19, 21, 18, 19, 20, 23, 18, 20, 23]

x = [2.1, 2.5, 4.0, 3.6]  # economic growth
y = [8, 12, 14, 10]  # profits

categories = ["white", "hispanic", "black", "asian", "other"]

national = pd.DataFrame([categories[0]] * 100000 + [categories[1]] * 60000 + \
                        [categories[2]] * 50000 + [categories[3]] * 15000 + [categories[4]] * 35000)

minnesota = pd.DataFrame([categories[0]] * 600 + [categories[1]] * 300 + \
                         [categories[2]] * 250 + [categories[3]] * 75 + [categories[4]] * 150)