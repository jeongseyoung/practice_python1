import numpy as np
import math as m
import time as t

N = 3
if __name__ == "__main__":
    RN1 = np.random.randn(N, N).astype(np.float32)
    RN2 = np.random.randn(N, N).astype(np.float32)
print(f"{RN1}\n")
print(RN2)
print(f"RN1 + RN2:\n {RN1 + RN2}")

food = ["hamburger", "cheese", "chicken"]
dessert = ["cake", "ice cream"]
beverage = ["coke", "coffe", "juice"]

food.append("pizza")
print(food[0])

food[0] = "galbi"
print(food)
food.remove("pizza")
print(food)
print(food.pop(1)) #해당 배열에서 완전 빼내기
#food.insert(0, "ramen")
print(food)
food.insert(1, "ramen")
print(food)

for i in food:
    print(i)
    
#RN_Array = [RN1, RN2]

storage = [food, dessert, beverage]
print(storage[1][1])
print(RN1[0][2])
#print(RN_Array)
#print(RN_Array[0][0][0])

student = ("bro",10,"male") #-> tuple 튜플 collection which is ordered and unchangeable, used to group together related data.

print(student.index("bro"))
print(student.count("male")) # male인 거 몇개인지 (index 아님)
for i in student:
    print(i)
str = "bro"
# if str in student:
#     print("ㅇㅋ 있음")
# else:
#     print("없음;")    
#print(str in student ? "ㅇㅋ있음" : "ㄴㄴ없음" )
print("ㅇㅋ있음") if str in student else print("ㄴㄴ없음")

if __name__ == "__main__":
    print("__name__")

# {"", ""} -> set
# set -> collection which is unordered, unindexed. No duplicate values.
utensils = {"f", "s", "k"}
dishes = {"a", "b", "k"}

utensils.add("t")
# utensils.update(dishes)

table = utensils.union(dishes)

for x in table:
    print(x) # -> f s k 는 set -> 인덱스가 없음. -> 출력하면 출력순서가 계속 바뀜.

print(utensils.difference(dishes))
print(utensils.intersection(dishes)) # 같은 거만


# dictionary -> value : key

capitals = {
    "Korea" : "Seoul",
    "Japan" : "Tokyo",
    "UK" : "London",
    "USA" : "Washington DC"
}

#print(capitals["Korea"])
#print(capitals.get("China"))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.pop("USA"))
#print(capitals.popitem())
#print(capitals)

print(f"items {capitals.items()}")

capitals.update({"France" : "Paris"})
capitals.update({"Germany" : "Hamburg"})
#capitals.clear()
for k,v in capitals.items():
    print(k, v)


#index operator [] = gives access to a secquence's element.(str, list, tuples)
my_name = "bro Code"
my_name[0].upper() #if my_name[0].islower() else my_name[0].lower()
print(my_name.capitalize())
abc = "abcdefg"
print(abc[2:-2])
print(abc[3:5])
print(abc[1:-3])
print(abc[1:4])

print(my_name[0:3])
print(my_name[4:8])
print(my_name[:-1])

print(my_name[-1])
#for i in 10:
#   print(i)
print(len(my_name))

def myname():
    my_name = "abc"
    print(my_name)

myname()
print(my_name)


def storage(*pocket): #튜플형식으로 받음.-> unchangeable.
    sum = 0
    pocket = list(pocket) # list로 바꿔야 pocket[0] = 0 이 먹힘
    pocket[0] = 100
    for i in pocket:
        sum += i
    print(sum)
    
storage(1,2,3,4,5,6)

def what(**box):  # **kwargs -> key : value 로 받음 
    print(box)

what(str1="a",str="b")

def ttt(**box):
    for key, value in box.items():
        #print(key, value)
        print(value, end=" ")

ttt(str1="a",str2="b")