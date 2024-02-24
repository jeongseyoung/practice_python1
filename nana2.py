import numpy as np
import math as m


N = 5
RN1 = np.random.randn(N, N).astype(np.int8)
RN2 = np.random.randn(N, N).astype(np.int16)
print(f"{RN1}\n")
print(RN2)
print(f"RN1 + RN2:\n {RN1 + RN2}")


pi = 3.14
print(m.floor(pi))

print(pow(pi, 3)) # pow -> 제곱
print(m.floor(pi*pi*pi))

print(m.sqrt(pi)) # square root -> 루트!

array = [1,2,3,4,5]
x = 1
y = 2
z = 3
print(max(array))
print(min(x,y,z))

name = "aaa bbb"
name_first = name.split(" ")[1]
print(name_first)
print(name[5])

print(name_first)
print(name[0:2]) # aaa -> aa

brocode = "Bro Code!!!"
print(brocode[0:3])
print(f"{brocode[:3]} {brocode[4::2]}") # 0 : 4 : 2   0시작 : 4끝 : every second 두번째마다 출력 / start : stop : step
print(brocode[::-1]) # reversed

webpage = "http://naver.com"
s = slice(7, -4)
print(webpage[slice(7, -4)])
print(webpage[s])

temp = int(input("what temp is now?"))
def t():
    if temp >= 15 or temp <= 25: # or / and
        print("it's nice to go outside")
    elif temp >= 26:
        print("terrible")
    else:
        print("not good")
t()

my_name = ""
while len(my_name) == 0:
     my_name = input("What is your name?\n")

print(f"hi {my_name}")
my_name2 = ""
while not my_name2:
    my_name2 = input("What is your name?\n")             
print(f"hizz {my_name2}")
