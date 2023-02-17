
import os
import pandas as pd
import math
import numpy as np

path = '/Users/mau/Dropbox/Mac/Documents/Dissertation/Intergenerational_Exp/Data'
os.chdir(path)
filter = ['subject2', 'year', 'ra']
dtf = pd.read_csv('MasterFile_Feb13_NoDuplicates.csv', usecols=filter)

# Filter the DataFrame to select all rows where the year column is 31
df_filtered = dtf.loc[dtf['year'] == 31]

# Get the value of ra in row 31
ra_value = df_filtered.at[df_filtered.index[0], 'ra']

# Assign this value to all rows where the year column is 31
dtf.loc[dtf['year'] == 30, 'ra'] = ra_value

# Drop all rows where the year column is 31
dtf.drop(dtf[dtf['year'] == 31].index, inplace=True)

# print(dtf.head(32))
dtf['ra1'] = dtf['ra']
dtf['ralinear'] = dtf['ra']
dtf['rapolynomial'] = dtf['ra']
dtf['rageometric'] = dtf['ra']
dtf['ra1'].ffill(axis = 0, inplace=True)
dtf['ralinear'].interpolate(method='linear', limit_direction='forward', inplace=True)
dtf['rapolynomial'].interpolate(method='polynomial', order=2, inplace=True)


# Let's create a new column that is a geometric appoximation of the RA

# Find the indices of the missing values
missing_indices = dtf.index[dtf["rageometric"].isna()].tolist()
# missing_indices = list(set(missing_indices))
# Loop over each missing index and calculate the geometric mean
values = []
for i in missing_indices:
    # Get the previous and next non-missing values
    prev_val = dtf.loc[:i, "rageometric"].dropna().iloc[-1]
    next_val = dtf.loc[i:, "rageometric"].dropna().iloc[0]
    # Calculate the geometric mean
    interval = next_val - prev_val
    geometric_mean = (prev_val * next_val) ** 0.5
    # The formula for geometric approximation of a missing value is:
    # x_i = sqrt(x_{i-1} * x_{i+n})
    #
    # where x_i is the missing value that you want to fill, x_{i-1} is the previous value in the series,
    # and x_{i+n} is the next non-missing value after the missing value you want to fill. sqrt refers to the square root function.
    #
    # This formula assumes that the missing values follow a geometric progression. It works by taking the geometric mean
    # of the two nearest known values to the missing value, which is a reasonable estimate of what the missing value should be
    # if the values are indeed following a geometric progression.
    values.append(geometric_mean ** (interval / (len(missing_indices) + 1)))
    # G(t) = G(t-1) * (1 + r)^(interval in years)
    # where G(t-1) is the last observed value of the geometric mean, 
    # r is the geometric return, and 
    # the interval is the time between the last observation and the missing value in years.


# Fill in the missing values
dtf.loc[missing_indices, "rageometric"] = values


writer = pd.ExcelWriter('RAs.xlsx', engine='xlsxwriter')
dtf.to_excel(writer, index=False)
writer.save()

