#Python JSON File Input
#Written by: Jeff Brusoe
#Last Updated: September 8, 2019
#
#Data taken from - https://www.climate.gov/maps-data/dataset/global-temperature-anomalies-graphing-tool

import json

print("Attemping to import temperature anomalies JSON file")

JSONFile = open('C:\\Users\\jbrus\\Documents\\GitHub\\Python\\JSON\\TemperatureAnomalies.json',"r")
TempAnomalies = json.load(JSONFile)
JSONFile.close()

print(TempAnomalies)
print("Type: " + str(type(TempAnomalies)))


print("Successfully loaded json file")

print("\nLooping through data values")
for k,v in TempAnomalies['data'].items():
    print("Year: " + k)
    print("Temp Anomaly: " + v)
