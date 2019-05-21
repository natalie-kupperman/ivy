import glob

myfiles = glob.glob('spreadsheets/ctr-report*.csv')

for file in myfiles:
    lines = open(file).readlines()
    open(file, 'w').writelines(lines[9:])


