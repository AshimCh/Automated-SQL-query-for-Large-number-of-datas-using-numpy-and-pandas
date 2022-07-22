'''Automated SQL query for Large number of datas using numpy and pandas'''

import numpy as np
import pandas as pd
import os

T1 = "Tablename"

df = pd.read_excel('output sql query.xlsx')

df1 = pd.DataFrame(df)

print(df1)

combined_values = df1['id'].map(str) + ',' + df1['name'].map(str) + ',' + df1['address'].map(str)+ ',' + df1['phone'].map(str)
print(combined_values)

last_value = df1['id'].iat[-1]
print(last_value)

sourceFile = open('demo.txt', 'w')
for i in range (last_value):
    a = print('INSERT into '+T1+'('+'id '+','+'name '+','+'address '+','+'phone'+')',file = sourceFile)
    b = print('Values'+'('+combined_values[i]+')'+'\n',file = sourceFile)
    count = i+1
    




