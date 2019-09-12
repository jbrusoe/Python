#Python OOP Inheritance Demo
#Written by: Jeff Brusoe
#Last Updated: September 12, 2019

#Base Class
class Planet:

    def __init__(self,name,solar):
        self.name = name
        self.solar = solar

    def GetName(self):
        return self.name

    def SetName(self,name):
        self.name = name

    def InSolarSystem(self):
        return self.solar

#Sub Class
class Mars(Planet):

    def __init__(self):
      Planet.__init__(self,"Mars",True)

print("Creating instance of the Mars class")
MyPlanet = Mars()
print("Planet Name: " + MyPlanet.GetName())
print("Solar System: " + str(MyPlanet.InSolarSystem()))

print("\nCreating instance of the Planet class")
MyPlanet2 = Planet("Vulcan",False)
print("Planet Name: " + MyPlanet2.GetName())
print("Solar System: "+ str(MyPlanet2.InSolarSystem()))


        

    
