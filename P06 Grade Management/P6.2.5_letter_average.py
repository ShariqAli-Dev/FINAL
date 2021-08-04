import numpy as np
import pandas as pd

df = pd.read_excel('data.xlsx')

test1 = df["test1"]
test2 = df["test2"]
final = df["final"]

def letter_average(L):
    average = round(L.mean())

    if average >= 90 and average <= 100:
        return "A"
    elif average >= 75 and average < 90:
        return "B"
    elif average >= 60 and average < 75:
        return "C"
    else:
        return "F"

print(f"Test 1: {letter_average(test1)}")
print(f"Test 2: {letter_average(test2)}")
print(f"Final:  {letter_average(final)}")