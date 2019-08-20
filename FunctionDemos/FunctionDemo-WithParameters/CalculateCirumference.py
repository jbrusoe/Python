#Circumference Calculation with Function

Pi = 3.14

def CalculateCircumference(Radius):
    print ("Radius: " + str(Radius))

    return 2*Pi*Radius


for i in range(1,11):
    print("Circumference: " + str(CalculateCircumference(i)) + "\n")
