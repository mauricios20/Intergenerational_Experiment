import os
import pandas as pd
import numpy as np
import stata_setup
stata_setup.config('/Applications/Stata', 'be')
from pystata import stata
from sfi import Scalar, Matrix

# Import data
path = """/Users/mau/Dropbox/Mac/Documents/Dissertation/Intergenerational_Exp/Data"""
os.chdir(path)

dtf = pd.read_csv('Full_panel.csv')

dtf.frac_stocks
stata.pdataframe_to_data(dtf, force=True)
stata.run('describe, numbers')
stata.run('destring, replace ignore(.)')
stata.run('describe')
stata.run('fracreg probit frac_stocks belief bab_L1 age educ exper gen2negdum')
stata.run('margins, dyex(_all)')
