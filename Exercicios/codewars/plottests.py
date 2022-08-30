import numpy as np
import matplotlib.pyplot as plt
from random import randint

year = []
population = []

for n in range(0,100):
    year.append(1950+n)
for n in range(0,100):
    rand = randint(50,400)
    population.append(5000+n*rand)
print(year)
print(population)

plt.scatter(year, population) #aqui plota
#plt.xscale('log') #aqui da a escala
plt.show() #print do mathplot

plt.clf()
plt.hist(population, bins=3)
plt.show() #print do mathplot
