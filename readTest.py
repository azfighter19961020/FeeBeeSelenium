# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd

original = pd.read_csv('output.csv')
original.columns = ['商品','價格','商店']

print(original.head())
print(original.shape)
