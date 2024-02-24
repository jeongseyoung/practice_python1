import numpy as np
import math as m


print("aa " + str(50) + "입니당d")
print(f"20 days are {50} minutes") 
print('200 is great number')
print(200 * 200)
print("곱하기 :  {200} * {200}")
print(f"곱하기 :  {200} * {200}")
print("곱하기 " + str(50 * 50))
print(f'곱하기 {50 * 50}')
to_seconds = 24 * 60 * 60
print(to_seconds)
abc = 24 * 60 * 60
print(abc)
to_First = 10
print(to_First)
print(f"{abc * to_First}")
name_of_part = "tbhh"
print(f"{1 + 2} {name_of_part}")
print(round(1.2))
def test(str):
    abcd = "abcd"
    print(abcd)
    if str == "tbh":
        print("ok!!!!!!!!!")
    else: print("not tbh!")

test("tbh")

def boolean_test(son):
    print(abc)
    if son != True: print("FALSE")
    else: print("TRUE")

abb = False
boolean_test(abb)

a = "A"
b = ""
result = a + b
print(result)
str = "*"
str.__add__("*")

print(str)
aff = ""

get_input = input("아무거나 입력해보셈\n")
print(get_input)
def c(num):
    sum = int(get_input) + 2 + num
    return sum
result2 = c(2) + 2
print(f"결과는?! {result2} 입니당!ㅋㅋ;")

num = 10
num2 = 0
for i in range(0, num):
    num2 += 1
    print(num2)
print(f"num2결과는 {num2}")

def aqq():
    num = 5
    num2 = 0
    for i in range(0, num):
        num2 += 1
        print(f"for num2: {num2}")
    print(f"def num2 result: {num2}")
aqq()    
nn = int(10)    

def aww(num):
    print(f"aww: {num > 0}")
aww(1)
N = 5
RN1 = np.random.randn(N, N).astype(np.int8)
RN2 = np.random.randn(N, N).astype(np.int16)
print(f"{RN1}\n")
print(RN2)
print(f"RN1 + RN2:\n {RN1 + RN2}")
"""
bbb
aaa
ccc
"""
#ccc

human = False #false -> x
print(human)
print(type(human))
        
#dog, cat, rabbit = "a", "b", "c"
dog=cat=rabbit = "A" 
print(dog)
print(cat)
print(rabbit)
nameof = "aabbbbbb"
print(nameof.lower())
print(nameof.upper())
print(len(nameof))
print(nameof.capitalize()) #첫글자를 대문자로
print(nameof.count("b"))
print(nameof  * 3) # 3번 반복

num5 = 1.2
num5 = int(num5)
print(num5)

x = 1.9
y = 2.0
z = "3"
x = int(x)
y = int(y)
z = float(z)
print(x)
print(f"{y} {z*5}")
print(type(z))


pi = 3.14159
print(m.floor(pi))
