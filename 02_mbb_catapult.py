# create session_id column from ctr report name
import pandas as pd
import glob, os

files = glob.glob('spreadsheets/ctr-report*.csv')

for file_ in files:
    df2 = pd.read_csv(file_).assign(session_id=os.path.basename(file_).split('.')[0].split('-')[2])
    df2.to_csv(file_, index = False)

