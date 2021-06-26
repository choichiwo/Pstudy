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