#Enter temperature data
#Written by: Jeff Brusoe
#Last Updated: September 8, 2018
#
#The purpose of this program is to enter temperature data to a MySQL database. I'm
#investigating is there is a simple way to correlat this data with the official data
#published by NASA or NOAA. If that is possible, then it might be a way to allow
#K-12 students to derive very important results from fairly easily obtained data.

#To do:
#1. Look into ways of automatically pulling temperature information.
#2. Clean up input validation section and write functions to handle some of that work.
#3. Convert to web page for easier data input.

import mysql.connector
import datetime
import sys
import EnterTemperatureFunctions as etf

debug = False

mydb = mysql.connector.connect(
  host="localhost",
  user="peruser",
  passwd="MyPassword",
  database="climatechange"
)

DateInputString = "Enter Date (Default is " + str(datetime.date.today()) + "): "
CurrentDate = input(DateInputString)

City = input("Enter city (Default is Morgantown): ")
State = input("Enter state (Default is WV): ")
ZipCode = input("Enter zip code(Default is 26505): ")
Country = input("Enter country (Default is US): ")
Source = input("Enter data source (Default is Windows Weather App): ")
ActualHighTemp = input("Enter actual high temp: ")
ActualLowTemp = input("Enter actual low temp: ")
AverageHighTemp = input("Enter average high tenp: ")
AverageLowTemp = input("Enter average low temp: ")
RecordHighTemp = input("Enter record high temp: ")
RecordHighTempYear = input("Enter record high temp year: ")
RecordLowTemp = input("Enter record low temp: ")
RecordLowTempYear = input("Enter record low temp year: ")

print("Data to be entered into database:")
print("*********************************")

############################################
#The following block of code is for validation of information that the
#user has entered before it is put into the database.
############################################

if CurrentDate == "":
    CurrentDate = datetime.date.today()
print("Date to be entered:",CurrentDate)

if City == "":
    City = "Morgantown"
print("City:",City)

if State == "":
    State = "WV"
print("State:",State)

if ZipCode == "":
    ZipCode="26505"
print("Zip Code:",ZipCode)

if Country == "":
    Country="US"
print("Country:",Country)

#Validation checking for ActualHighTemp
if etf.is_int(ActualHighTemp):
    print("Acutal High Temp:", ActualHighTemp)
    intActualHighTemp = int(ActualHighTemp)
    
    #Verify that the high temperature that is entered is a reasonable value.
    #Use machine learning to figure out possible values of high temperatures?
    if intActualHighTemp < 0:
        print("Invalid high temperature has been entered.")
        sys.exit()
    
else:
    print("Actual High Temp is not an integer. Program is exiting.")
    sys.exit()

#Validation checking for RecordHighTempYear
if etf.is_int(RecordHighTempYear):
    print("Record high temp year",RecordHighTempYear)

    #At this point, this value is a valid integer. Now check to see if is a valid year.
    #A valid year is assumed to be an integer between 1800 and 2100.
    #Can this be done with machine learning?
    intRecordHighTempYear = int(RecordHighTempYear)

    if (intRecordHighTempYear >= 1800 and intRecordHighTempYear <= 2100):
        print("Record high temp year is valid.")
    else:
        print("Record high temp year is invalid.")
        sys.exit()
else:
    print("Record high temp year is not an integer. Program is exiting.")
    sys.exit()

print("Data validation is complete.")
print("*********************************")

if (not debug):
    mycursor = mydb.cursor()
    sql = "INSERT INTO dailytemperature (TemperatureDate,City,ActualHighTemp,ActualLowTemp,AverageHighTemp,AverageLowTemp,RecordHighTemp,RecordHighTempYear,RecordLowTemp,RecordLowTempYear) VALUES (%s, %s,%s, %s,%s,%s,%s,%s,%s,%s)"
    val = (CurrentDate, "Morgantown",ActualHighTemp,ActualLowTemp,AverageHighTemp,AverageLowTemp,RecordHighTemp,RecordHighTempYear,RecordLowTemp,RecordLowTempYear)

    mycursor.execute(sql,val)
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
else:
    print("Debug mode is on. Data has not been written to database.")
