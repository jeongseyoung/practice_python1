import numpy as np
import math as m
import time as t

N = 5
RN1 = np.random.randn(N, N).astype(np.int8)
RN2 = np.random.randn(N, N).astype(np.int16)
print(f"{RN1}\n")
print(RN2)
print(f"RN1 + RN2:\n {RN1 + RN2}")

get_name = input("N A M E ?")

while True:
    if get_name == "A":
        print(get_name)
    else: 
        print("다음기회에~")    
    break



def t1():
    while True:
        str = input("enter ur name\n->")
        if str != "":
            print(f"니가 입력한 건 {str} 입니다!")
        break

t1()

def t2():
    str = "AAAAAAbbbbbbb"
    
    for i in str:
        if i == str.upper():
            continue
        print(i, end="")


phone_number = "010-0000-0000"        
for i in phone_number:
        if i == "-":
            continue
        print(i, end=".")
             
print("\n")                 
t2()
        