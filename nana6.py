import numpy as np
import math as m
import time as t
import random as r

N = 3
if __name__ == "__main__":
    RN1 = np.random.randn(N, N).astype(np.float32)
    RN2 = np.random.randn(N, N).astype(np.float32)
print(f"{RN1}\n")
print(RN2)
print(f"RN1 + RN2:\n {RN1 + RN2}")

a = "A"
b = "B"
print("A = {}, B = {}".format("a", "b"))
print("A = {1}, B = {0}".format("a", "b"))
print("A = {b}, B = {a}".format(a = "A", b = "B"))

num = 3.14519
print("{:2f}".format(num))
print("{:,}".format(num))
#print("{:b}".format(num))
#print("{:o}".format(num))

x = r.randint(1,6)
y = r.random()
# print(r.randrange(0,2))

r_str = [1,2,3,4,5,6,7,8,9,0,"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "M"]
r.shuffle(r_str)
print(r_str)
def mix():
    new_str = ""
    for i in r_str:        
        new_str += str(i)
        if((len(new_str)) % 4 == 0):
            new_str += "-"                
    return new_str

print(mix())

try:
    n = int(input("Enter a number: "))
    if type(n) == int:
        print(n)
except:
    print("숫자 ㄱ")

try:
    num1 = int(input("divide : "))
    num2 = int(input("divided by : "))
except ZeroDivisionError as e:
    print(e)    
    print( "0은 안됨")
except ValueError as e:
    print(e)   
    print("숫자 ㄱ")
except Exception as e:
    print(e)
    print("뭐함?")
else:
    print(f"result : {int(num1 / num2)}")
finally:
    print("FINALLY")