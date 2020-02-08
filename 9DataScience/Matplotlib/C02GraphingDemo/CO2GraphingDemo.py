#Graphing Demonstration from CSV
#Filename: 05-CSVGraphingDemo.py
#Version 1.0
#Language: Python 3.6.4
#
#Written by: Jeff Brusoe (jbrusoe@gmail.com)
#Last Updated: February 20, 2018
#
#The purpose of this file is to take data stored as a CSV file
#and graph this with Pyplot.
#
#The sample data was taken from this site.
#https://www.esrl.noaa.gov/gmd/ccgg/trends/full.html

import csv
import matplotlib.pyplot as plt
import numpy as np

CO2DataFile = "CO2.csv"

from collections import namedtuple

with open(CO2DataFile) as CO2Data:
    CSVReader = csv.reader(CO2Data)

    #Get field names
    #Note: Assumes that there are no spaces in names.
    #The correction on this page should be here to 
    #account for this possibility: https://www.alexkras.com/how-to-read-csv-file-in-python/.
    FirstRow = namedtuple('Data', next(CSVReader))
    data = [FirstRow(*r) for r in CSVReader]

#These arrays will hold the CSV data for graphing
Date = []
CO2ppm = []

print("Generating x and y values from CSV data...")
for i in range(0,len(data)):
    #print(data[i].DecimalDate,data[i].Average)
    Date.append(float(data[i].DecimalDate))
    CO2ppm.append(float(data[i].Average))

    if CO2ppm[i] <= 0:
        CO2ppm[i] = float(data[i].Interpolated)

    #print("DecimalDate:",Date[i])
    #print("CO2ppm:",CO2ppm[i])

#At this point, there should be two valid arrays with 
#the date(x) and CO2 concentrations (y) in them.
#Now, plot the data.

plt.plot(Date,CO2ppm)

plt.xlabel('Date',fontsize=25)
plt.ylabel('CO2ppm',fontsize=25)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.title('Pyplot CO2 Concentration vs. Time', fontsize = 40)
plt.grid(True)
plt.savefig("CO2Concentration.png")
plt.show()

