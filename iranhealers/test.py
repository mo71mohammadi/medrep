import xlrd

workbook = xlrd.open_workbook('test.xlsx"')
print(workbook)

import pandas as pd

df = pd.read_excel("test.xlsx")
print(df)
