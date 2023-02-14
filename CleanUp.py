import os
import pandas as pd

# define function to swap columns


def swap_columns(df, col1, col2):
    col_list = list(df.columns)
    x, y = col_list.index(col1), col_list.index(col2)
    col_list[y], col_list[x] = col_list[x], col_list[y]
    df = df[col_list]
    return df


# Import data
path = '/Users/mau/Dropbox/Mac/Documents/Dissertation/Intergenerational_Exp/Data'
os.chdir(path)
filter = ['subject2', 'Condition', 'Y', 'BAB', 'C', 'US', 'AC', 'AS', 'ARD',
          'EAB', 'APR', 'Belief', 'RA',	'Average',	'High',	'Low',	'GT30',
          'LT30']
dtf = pd.read_csv('DataNoPracticeFinal.csv', usecols=filter)
dtfQ = pd.read_csv('QualtircsRecodeNov11_2022.csv')

len(dtfQ.subject2.unique())
len(dtf.subject2.unique())
dtf.shape
dtf.info()
dtfQ.shape

# Overall Dataframe
SortedDtf = dtf.sort_values(by=['subject2', 'Y'])
print(SortedDtf)

# swap points and rebounds columns
df = swap_columns(SortedDtf, 'Condition', 'subject2').fillna('.')

# view updated DataFrame
print(df.subject2.unique())

# Rename
dic = {'Condition': 'condition', 'Y': 'year', 'BAB': 'bab',
       'C': 'alloca', 'US': 'stocks', 'AC': 'ac', 'AS': 'as', 'ARD': 'ard',
       'EAB': 'eab', 'APR': 'apr', 'Belief': 'belief', 'RA': 'ra',
       'Average': 'average', 'High': 'high', 'GT30': 'gt30', 'LT30': 'lt30'}

# Overall_dtf dtf
Overall_dtf = df.rename(columns=dic)


# To cvs file
writer = pd.ExcelWriter('FullPanel_MasterFile.xlsx', engine='xlsxwriter')
Overall_dtf.to_excel(writer, index=False)
writer.save()

# For Individual Statistics
dtfg1 = dtf.loc[dtf['Condition'].isin(["Gen1"])]
dtfg2Neg = dtf.loc[dtf['Condition'].isin(["Gen2Neg"])]
dtfg2Pos = dtf.loc[dtf['Condition'].isin(["Gen2Pos"])]
dtfg3NegPos = dtf.loc[dtf['Condition'].isin(["Gen3NegPos"])]
dtfg3PosNeg = dtf.loc[dtf['Condition'].isin(["Gen3PosNeg "])]
dtfg3PosPos = dtf.loc[dtf['Condition'].isin(["Gen3PosPos"])]
dtfg3NegNeg = dtf.loc[dtf['Condition'].isin(["Gen3NegNeg"])]

Sub = dtfg3PosPos.subject2.unique()
print(Sub)

print(len(dtfg3NegNeg.subject2.unique()))

#  ################ $$ Overall $$ ####################

dtf.columns
dtfQ.columns
listQ = dtfQ.subject2.unique()
listE = dtf.subject2.unique()

listQ
listE
count = sum(f in listE for f in listQ)
print(count)

# Without 20 Subjects
inner_merge1 = pd.merge(dtf, dtfQ, on='subject2')
dummies = pd.get_dummies(inner_merge1['Condition_x']).rename(columns=lambda x: str(x).lower()+'dum')
df1 = pd.concat([inner_merge1, dummies], axis=1)
writer = pd.ExcelWriter('BMasterFile_Nov16_Missing20.xlsx', engine='xlsxwriter')
df1.to_excel(writer, index=False)
writer.save()

# Inner merge All
inner_merge = pd.merge(dtf, dtfQ, on='subject2', how='left').fillna('.')
inner_merge.shape
inner_merge.columns
len(inner_merge.subject2.unique())

# dummies = pd.get_dummies(df['Category']).rename(columns=lambda x: 'Category_' + str(x))
# df = pd.concat([df, dummies], axis=1)

dummies = pd.get_dummies(inner_merge['Condition_x']).rename(columns=lambda x: str(x).lower()+'dum')
df = pd.concat([inner_merge, dummies], axis=1)

list = []
for i in df['QTotalDuration']:
    if i == '.':
        list.append(1)
    else:
        list.append(0)

df['missingQ'] = list

writer = pd.ExcelWriter('UMasterFile_Nov16_ALL.xlsx', engine='xlsxwriter')
df.to_excel(writer, index=False)
writer.save()
