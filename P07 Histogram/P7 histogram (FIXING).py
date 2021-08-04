import random
import seaborn
from random import seed
from random import randint
from statistics import pvariance, pstdev
import statistics as st
import seaborn as sns
import matplotlib.pyplot as plt


def mean(Grades):
    # mean
    # Grades = [34, 65, 23, 89, 59]
    Mean = sum(Grades) / len(Grades)
    print("Mean =", Mean)
    return Mean


def median(grades):
    # median
    # grades = [43, 65, 26, 45, 12, 67]
    sortedgrades = sorted(grades)
    print("Sorted grades =", sortedgrades)
    if (len(sortedgrades) % 2):
        median = sortedgrades[len(sortedgrades) // 2]
    else:
        median = (sortedgrades[len(sortedgrades) // 2] + sortedgrades[len(sortedgrades) // 2 - 1]) / 2
        print("Median =", median)


def mode(grades):
    # mode
    # grades = [1, 3, 5, 7, 2, 4, 7, 2, 9, 3, 7, 6, 5]
    mymean = st.mean(grades)
    mymedian = st.median(grades)
    mymode = st.mode(grades)
    print("Mean =", mymean, "\t", "Median =", mymedian, "\t", "Mode =", mymode)
    return mymode


# seed random number generator
seed(1)
# generate some integers
votes = []
for i in range(50):
    votes.append(randint(0, 10))

print(votes)
mymean = mean(votes)
mymode = mode(votes)

print("Mean =", mymean, "\t", "Mode =", mymode)
myvar = pvariance(votes)
mystdev = pstdev(votes)
mymedian = st.median(votes)
print(' Variance = {:2.3} StDev = {:2.3} '.format(myvar, mystdev))

yvalues = [mymean, mymedian, mymode, myvar, mystdev]
xvalues = [' mean ', ' median ', ' mode ', ' variance ', ' standard deviation ']
title = ' st '
sns.set_style(' whitegrid ')
axes = sns.barplot(x=xvalues, y=yvalues, palette=' bright ')
axes.set_title(title)  # Set the title of the graph
axes.set(xlabel=' votes ', ylabel=' frequencies ')  # Set the x and y labels
axes.set_ylim(top=max(yvalues) * 1.10)  # Set the maximum y value in the graph
plt.show()
