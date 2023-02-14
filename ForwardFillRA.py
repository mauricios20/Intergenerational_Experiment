
import os
import pandas as pd

path = '/Users/mau/Dropbox/Mac/Documents/Dissertation/Intergenerational_Exp/Data'
os.chdir(path)
filter = ['subject2', 'year', 'ra']
dtf = pd.read_csv('MasterFile_Feb13_NoDuplicates.csv', usecols=filter)
dtf['ra1'] = dtf['ra']
dtf['ralinear'] = dtf['ra']
dtf['rapolynomial'] = dtf['ra']
dtf['ra1'].ffill(axis = 0, inplace=True)
dtf['ralinear'].interpolate(method='linear', limit_direction='forward', inplace=True)
dtf['rapolynomial'].interpolate(method='polynomial', order=2, inplace=True)
print(dtf.head(50))

writer = pd.ExcelWriter('ForwardFillRA1.xlsx', engine='xlsxwriter')
dtf.to_excel(writer, index=False)
writer.save()

