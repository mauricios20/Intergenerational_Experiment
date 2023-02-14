import os
import pandas as pd

# Import data
path = '/Users/mau/Dropbox/Mac/Documents/Dissertation/Intergenerational_Exp/Data'
os.chdir(path)
filter = ['condition', 'subject2', 'year', 'ra']
dtf = pd.read_csv('DataNoPracticewithRA.csv', usecols=filter)
dfstata = pd.read_csv('MasterDataExcel.csv')

print(len(dtf.year.unique()))
print(len(dfstata.year.unique()))
print(dtf.info())
print(dfstata.info())
# Inner merge All
inner_merge = dfstata.merge(dtf, on=['year', 'subject2'], how='outer').fillna('.')


# inner_merge = pd.merge(dtf, dfstata, on='subject2', how='left').fillna('.')
print(inner_merge.info())
print(inner_merge.columns)
print(len(inner_merge.year.unique()))


inner_merge.drop(['condition_x'], axis=1, inplace=True)
inner_merge.rename({'condition_y': 'condition'}, axis=1, inplace=True)
print(inner_merge.columns)
print(inner_merge.tail(35))

SortedDtf = inner_merge.sort_values(by=['subject2', 'year'])
print(SortedDtf.tail(35))
# dummies = pd.get_dummies(df['Category']).rename(columns=lambda x: 'Category_' + str(x))
# df = pd.concat([df, dummies], axis=1)


writer = pd.ExcelWriter('MasterFilewithRA.xlsx', engine='xlsxwriter')
inner_merge.to_excel(writer, index=False)
writer.save()

writer = pd.ExcelWriter('MasterFilewithRASorted.xlsx', engine='xlsxwriter')
SortedDtf.to_excel(writer, index=False)
writer.save()
