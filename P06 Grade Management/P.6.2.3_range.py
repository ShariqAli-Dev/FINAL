#P6.2.3
import numpy as np
import pandas as pd

df = pd.read_excel('data.xlsx')

test1 = df["test1"]
test2 = df["test2"]
final = df["final"]

#feed a list of columns
def theRange(L):
    minimum = min(L)
    maxiumum = max(L)
    print(f"Range: {maxiumum - minimum}")

theRange(test1)
theRange(test2)
theRange(final)