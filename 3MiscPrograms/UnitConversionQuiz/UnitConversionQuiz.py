import random

units = ["cm","km","mm","dm","in"]

unit1 = units[random.randint(0,len(units)-1)]
print("First Unit: " + unit1)

unit2 = unit1

while unit2 == unit1:
    unit2 = units[random.randint(0,len(units)-1)]
    print("Second Unit: " + unit2)

#Dictionary to store conversion factors
ConversionFactors = {
     "mm": {"cm": 1/10, "km": 1/1000000, "dm": 1/100, "in": 0.0394},
     "cm": {"km": 1/100000, "mm": 10, "dm": 1/10, "in": 1/2.54}
     }



