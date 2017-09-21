import sys
from random import choice as choose

mealList=[]

f = open('meals.txt', 'r')
for line in f:
    mealList.append(line)
    
meal = choose(mealList)
print 'Tonight you should make: '+str(meal)
