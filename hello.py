x="Hello"
y="world"
print("Hello")
print(x)

# 변수형에는 정수형(3)int, 실수형(3.14)float, 문자열("Hello")str

print(type(x))

print(7//2) #정수나누기 몫
print(7%2) #나머지연산자 나머지
print(7/3)

print(x+y)

x=3
print(5*"hello") #이항연사자중 *만 정수와 문자열로만 가능 

print("x =", x)


x = 13
y = 25
print("x =", x,",","y =", y,",", "sum =", x+y,",", "multi =" ,x*y,",", "rem =", x%y  )


pi = 3.14159265

r = 5

print("원주율 =", pi)
print("반지름 =", r)
print("원의 둘레 =", 2*pi*r)
print("원의 넓이 =", pi*r*r )

#num = input("숫자를 입력하세요")
#num = int(num)

#print(num +3)

n = str(14)
print(type(n))

x = 12
print('x = {}'.format(x))
print('x = {},y={}'.format(x,12))
print('x = {},y={}'.format(x,24))
print('x = {},y={}'.format(x,12))
y = 5
print('x = {},y={}'.format(x,5))

print('x[{}]'.format(x))

print('x[{:5d}]'.format(x)) # decimal(십진수)

print('x[{}], x[{:5d}]'.format(x,x))

fmtstr = 'x[{}], x[{:5d}]'.format(x,x)

print(fmtstr)
print(type(fmtstr))

pstr = 'x[{}], x[{:5d}]'
fmtstr = pstr.format(x,x)
print(fmtstr)

# m.nf m:소수점을 포함한 전체길이 n: 소수점이하 자리수

from random import shuffle
num = range(1, 12)
num = list(num)
num = shuffle(num)
print(num)