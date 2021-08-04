import numpy as np
import pandas as pd

df = pd.read_excel('data.xlsx')

test1 = df["test1"]
test2 = df["test2"]
final = df["final"]


def average(L):
    return round(L.mean())

print(f"Test 1 :{average(test1)}%")
print(f"Test 2 :{average(test2)}%")
print(f"Final  :{average(final)}%")
