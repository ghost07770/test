# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:45:15 2019

@author: Kritartha Patowary
"""

import pandas as pd

#initialiting data os lists

data = {'Name':['Tom','nick','krish','jack'],
        'Age' :[20,21,19,18]}

#creating DataFrame
df=pd.DataFrame(data)

#Print the output.
print(df)