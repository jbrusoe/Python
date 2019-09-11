#Sine Wave Demonstration
#Filename: SineWave.py
#Version 1.0
#Language: Python 3.6.4
#
#Written by: Jeff Brusoe (jbrusoe@gmail.com)
#Last Updated: February 20, 2018
#
#The purpose of this file is to display a sine wave using Pyplot.
#
#The sample data was taken from this site.
#https://www.esrl.noaa.gov/gmd/ccgg/trends/full.html

import matplotlib.pyplot as plt
import numpy as np

#Generate x & y values
x = np.arange(0.0, 4.01, 0.01)
y = np.sin(np.pi*x)

plt.plot(x, y)

#Set properties of the plot
plt.xlabel('x*pi',fontsize=25)
plt.ylabel('sin(x*pi)',fontsize=25)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.title('Pyplot Sine Wave', fontsize = 40)
plt.grid(True)
plt.savefig("SineWave.png")

plt.show()
