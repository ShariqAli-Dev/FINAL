import random
import matplotlib.pyplot
import seaborn
from random import seed
from random import randint
from statistics import pvariance, pstdev
import statistics
import statistics as st 
import seaborn as sns
import matplotlib.pyplot as plt


def mean():
    #mean
    Grades = [34, 65, 23, 89, 59]
    Mean = sum(Grades)/len(Grades)
    print("Mean =", Mean)


def median():
    #median
    grades = [43, 65, 26, 45, 12, 67]
    sortedgrades = sorted(grades)
    print("Sorted grades =", sortedgrades)
    if(len(sortedgrades) % 2):
      median = sortedgrades[len(sortedgrades)//2]
    else:
      median = (sortedgrades[len(sortedgrades)//2]+ sortedgrades[len(sortedgrades)//2 -1])/2
      print("Median =", median)


def mode():
    #mode
    grades = [1, 3, 5, 7, 2, 4, 7, 2, 9, 3, 7, 6, 5]
    mymean = statistics.mean(grades)
    mymedian = statistics.median(grades)
    mymode = statistics.mode(grades)
    print("Mean =", mymean,"\t", "Median =", mymedian, "\t","Mode =", mymode)




# seed random number generator
seed(1)
# generate some integers
votes = randint(0, 10, 50)
print(votes)
mymean = statistics.mean(votes)
mymode = statistics.mode(votes)
print("Mean =", mymean,"\t","Mode =", mymode)
myvar = pvariance(votes)
mymedian = st.median(votes)
# nce = {:2.3} StDev = {:2.3} ' .format(myvar, mystdev))

yvalues = [mymean, mymedian, mymode, myvar, mystdev]
xvalues = Statistics' mean ' , ' median ' , ' mode ' , ' variance ' , ' standard deviation ' ]
title = ' st '
sns.set_style( ' whitegrid ' )
axes = sns.barplot(x = xvalues, y=yvalues, palette= ' bright ' )
axes.set_title(title) # Set the title of the graph
axes.set(xlabel= ' votes ' , ylabel= ' frequencies ' ) # Set the x and y labels
axes.set_ylim(top=max(yvalues)*1.10) # Set the maximum y value in the graph

axes.set_ylim(top=max(yvalues)*1.10) # Set the maximum y value in␣plt.show() 