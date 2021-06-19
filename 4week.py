# def 함수지정 definition (input 매개변수, 파라미터)
def print3times(): # output리턴값
    print("hello")
    print("world")
    print("bye")

print3times() #calling

def prints(n):
    for i in range(n):
        print("Hello")

prints(3)

def four_op(m,n):
    print(m+n)
    print(m-n)
    print(m*n)
    print(m/n)
a=6
b=3
four_op(a,b)
four_op(8,4)   

def printList(lst):
    for x in lst:
        print(x)
a=[1,3,5,7,9]
printList(a)    


import math
def root(a,b,c):
    n = math.sqrt(b*b-4*a*c)
    return n

a = int(input('a='))
b = int(input('b='))
c = int(input('c='))

x1=(-b+root(a,b,c)) / (2*a)    
x2=(-b-root(a,b,c)) / (2*a) 

student = []

while True:
    name = input("name:")
    if name == "":
        break
    eng = input("eng:")
    mat = input("mat:")
    d = {"name":name, "eng":eng, "mat":mat}
    student.append(d)

student = []
def getpoint(x):
    eng = input("eng:")
    mat = input("mat:")
    d = {"name":name, "eng":eng, "mat":mat}
    return d  

while True:
    name = input("이름:")
    if name == "":
        break
    student.append(getpoint(name))
print(student)

