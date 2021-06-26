# for문 
# range(값1) 0~값-1, +1
# range(값1,값2) 값1~값2-1, +1
# range(값1,값2,값3) 값1~값2-1, +값3

#함수
# 1.반환값이 없는 함수 
# 2.반환값이 있는 함수 ~~ return value
# 정의, 호출



# for i in range(2,10):
#     for j in range(1,10):
#         #print(i,'X',j,'=',i*j)
#         def output(x,y):
#         print(x,"X",y,"=",x*y)
#         output(x,y)


def output(a,b):
    return a*b

# for i in range(2,10):
#     for j in range(1,10):
#         #print(i,'X',j,'=',i*j)
#         z = output(a,b)
#         print(a,"X",b,"=",z)         

#재귀함수: recursive
# 팩토리얼 !   예 5! = 5*4*3*2*1 

def factorial(n):
    output =1
    for i in range(1, n+1):
        output *= i
    return output
print("1!:", factorial(1))
print("2!:", factorial(2))    
print("3!:", factorial(3))    
print("4!:", factorial(4))

def factor(n):
    if n==1:
        return 1
    else:
        return n*factor(n-1)    

print("4!:", factor(4)) 

def plus(n):
    output = 0
    for i in range(1, n+1):
        output = output+i
    return output

x = plus(100)
print(x)        

def pluss(n):
    if n== 0:
        return 0
    else:
        return n+pluss(n-1)
print(pluss(100))      

# return 1 값을 반호나 return 값
#        2 함수종료 return

# 매개변수:  <=매개변수갯수
# def f1(a=3, b=5, c=10):
# f1(2,3)   = f1(2,3,10)
# f1() = f1(3,5,10)
# print(fi)

# 가변 매개변수: >=매개변수갯수
# def f1(a, *n):
#     sum = 0
#     for i in n:
#         sum = sum + i
#         print(sum)

# f1(1,2,3)        
# f1(1,3)
# f1(1)
# f1(1,23,4,2,6,8,7,9,12)

f = open("c:/document/menu.txt","w") #.w = for write(없으면 생성하고 열기, 있으면 기존내용 삭제하구 열기), .a = for append(없으면 생성하고 열기, 기존내용 유지 뒤에 새 내용 추가), .r = for read()

file = open("basic.txt","w")
file.write("Hello Python Programming...")
file.close()


file = open("basic.txt","r")
line=file.read()
file.close()