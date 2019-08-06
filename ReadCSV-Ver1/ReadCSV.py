#Filename: CO2.py
#Written by: Jeff Brusoe (jbrusoe@gmail.com)
#Last Updated: February 20, 2018
#
#Note: There are other ways to do this. Also, see the CSV import with pandas file.

import csv
import sys
import os.path

print("Python file name:",sys.argv[0],"\n")
print("Number of command line arguments:",len(sys.argv)-1,"\n")

#Note: sys.argv[0] is the .py file name
if len(sys.argv) > 2:
    print("Invalid number of command line arguments.")
    print("Program is exiting.")
    sys.exit()
elif len(sys.argv) == 2:
    CO2DataFile = sys.argv[1]
else:
    CO2DataFile = "CO2.csv"

#Have file name at this point. Verify that it exists.
print("CO2 Data File:", CO2DataFile)
if os.path.isfile(CO2DataFile):
    print("CSV File Exists... Opening file\n")
else:
    print("CSV File Does Not Exist... Program is exiting...\n")
    sys.exit()

#Begin to parse up file

###################
#Method 2
###################
from collections import namedtuple
with open(CO2DataFile) as f:
    f_csv = csv.reader(f)
    Row = namedtuple('Row', next(f_csv))
    for r in f_csv:
        row = Row(*r)
        # Process row
        print(row)


    



