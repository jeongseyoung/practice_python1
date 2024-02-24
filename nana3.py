import numpy as np
import math as m
import time as t

N = 5
RN1 = np.random.randn(N, N).astype(np.int8)
RN2 = np.random.randn(N, N).astype(np.int16)
print(f"{RN1}\n")
print(RN2)
print(f"RN1 + RN2:\n {RN1 + RN2}")
K = 10
for i in range(1,10+1,2): # 한다리 건너 하나만 출력
    print(i)

for i in "ABC A B C":
    print(i)    

for i in range(10,0-1,-1):
    print(i)
    #t.sleep(1) # 1초
print("HAPPY NEW YEARRRRRRRRRR")

ROW = int(input("How many rows?"))
COLUMN = int(input("How many columns?"))
SYMBOL = input("what's your favorite Symbol?")
for i in range(0,ROW):
    for j in range(0,COLUMN):
        print(SYMBOL, end="1") #  *1*1*1*1 -> "" 면 ****
    print(ROW)


