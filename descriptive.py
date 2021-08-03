#mean
Grades = [34, 65, 23, 89, 59]
Mean = sum(Grades)/len(Grades)
print("Mean =", Mean)
#median
grades = [43, 65, 26, 45, 12, 67]
sortedgrades = sorted(grades)
print("Sorted grades =", sortedgrades)
if(len(sortedgrades) % 2):
  median = sortedgrades[len(sortedgrades)//2]
else:
  median = (sortedgrades[len(sortedgrades)//2]+ sortedgrades[len(sortedgrades)//2 -1])/2
  print("Median =", median)
#mode
import statistics
grades = [1, 3, 5, 7, 2, 4, 7, 2, 9, 3, 7, 6, 5]
mymean = statistics.mean(grades)
mymedian = statistics.median(grades)
mymode = statistics.mode(grades)
print("Mean =", mymean,"\t", "Median =", mymedian, "\t","Mode =", mymode)

import random
import matplotlib.pyplot
import seaborn
from random import seed
from random import randint
# seed random number generator
seed(1)
# generate some integers
values = randint(0, 10, 50)
print(values)


