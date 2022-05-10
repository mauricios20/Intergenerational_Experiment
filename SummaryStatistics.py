
import os
import pandas as pd
import numpy as np
import stata_setup
stata_setup.config('/Applications/Stata', 'be')
from sfi import Scalar, Matrix
from pystata import stata
# Define Functions


def dstats(data, x, n):
    # 15 blocks takes 10 observations, decades
    command = 'summarize ' + x + ', ' + 'detail'
    list_of_stats = []
    stata.pdataframe_to_data(data, force=True)
    stata.run(command)
    # Get stats for each block
    N = Scalar.getValue('r(N)')
    mean = Scalar.getValue('r(mean)')
    min = Scalar.getValue('r(min)')
    max = Scalar.getValue('r(max)')
    sd = Scalar.getValue('r(sd)')
    var = Scalar.getValue('r(Var)')
    kurt = Scalar.getValue('r(kurtosis)')
    skw = Scalar.getValue('r(skewness)')

    # Append results to stats list_df
    list_of_stats.extend((mean, max, min, sd, var, kurt, skw, N))

    df = pd.DataFrame.from_dict(list_of_stats)
    df.rename(index={7: "N", 0: "Mean", 1: "Max",
                     2: "Min", 3: "Sd", 4: "Var",
                     5: "Kurtosis", 6: "Skewness"}, columns={0: n},
              inplace=True)
    # Rename columns DO NOT FORGERT
    return df


# Import data
path = '/Users/mau/Dropbox/Mac/Documents/Dissertation/Intergenerational_Exp/Data'
os.chdir(path)

dtf = pd.read_csv('DataNoPractice.csv')
dtfg1 = dtf.loc[dtf['Condition'].isin(["Gen1"])]
dtfg2Neg = dtf.loc[dtf['Condition'].isin(["Gen2Neg"])]
dtfg2Pos = dtf.loc[dtf['Condition'].isin(["Gen2Pos"])]
dtfg3NegPos = dtf.loc[dtf['Condition'].isin(["Gen3NegPos"])]
dtfg3PosNeg = dtf.loc[dtf['Condition'].isin(["Gen3PosNeg "])]

# Calculate Summary Statistcs for Percent Allocation
x = 'Belief'
stG1 = dstats(dtfg1, x, 'Gen1')
stG2Neg = dstats(dtfg2Neg, x, 'Gen2Neg')
stG2Pos = dstats(dtfg2Pos, x, 'Gen2Pos')
stG3NegPos = dstats(dtfg3NegPos, x, 'Gen3NegPos')
stG3PosNeg = dstats(dtfg3PosNeg, x, 'Gen3PosNeg')

#  ################ $$ Overall $$ ####################
Genstats = pd.concat([stG1, stG2Neg, stG2Pos, stG3NegPos, stG3PosNeg], axis=1)
print(Genstats.round(3).to_latex(index=True))
