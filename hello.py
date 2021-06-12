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

# :d (decimal:십진수,정수)
pstr = 'x[{}], x[{:5d}]'
fmtstr = pstr.format(x,x)
print(fmtstr)

print('z[{:5.2f}]'.format(3.14))
# m.nf m:소수점을 포함한 전체길이 n: 소수점이하 자리수 f:실수

x = "Hello"
print(x)
print(x.upper())
x = x.upper()
#upper: 대문자로 변환  lower: 소문자로 전환  <- mathod 메소드, 함수
print(x.lower())

#strip: 불필요 공백 삭제 l좌 r우
x = "  Hello World    "
print('['+x+']')
print(x.strip())
#is000 체킹 함수
print("TrainA10".isalnum()) #문자열이 알파벳 또는 숫자로 구성되는시 확인
x = "Hello world"
# find: 왼쪽부터 rfind: 오를쪽부터   모든 문자열은 배열.(인덱스번호를 갖는다.)
print(x.rfind('l'))
# in = contain(포함)

# split() 문자열 자르기 공백을 기준으로 자르기,  (',') ,기준으로 자르기

# 불 연산자 비교연산자 == 같다 , != 다르다, 
# >크다, <작다, <=작거나 같다 >=크거나 같다  b=true; b=false;
a=1
b=2

if(a==b):
    print(a)
else: 
    print(b)

# 불 논리연산자 not(반대로), and(둘다)~이고~고~그리고, or(둘중하나)~거나~또는~혹은
# 문자열 사전에 나오는 순서 "a" < "z" true "a" < "aa" true "abyss" < "abroad" false 
# "HelloWorld" < "Hello World" false   "공백"ABCD...Zabcd....z   순서대로 (공백<대문자<소문자)

# if 논리비교: 조건문
# elif 또 다른 조건
# else 아니면
if a != 1:
    print('true')
else:
    print('false')

import datetime
now = datetime.datetime.now()
print("{}년 {}월 {}일".format(now.year,now.month,now.day))

if 5< now.month <9:
    print("이번달은 {}월로 봄입니다".format(now.month))

x = input("x=")
y = input("y=")

x=int(x)
y=int(y)
5
if x < y:
    print(x)
else:
    print(y)


number = input("입력해주세요")
last_character = number[-1]
print(type(last_character))
last_number = int(last_character)

if last_number == 0 \
    or last_number == 2 \
    or last_number == 4 \
    or last_number == 6 \
    or last_number == 8:
    print("짝수입니다")    
else:
    print("홀수입니다")    

a = input("a=")
b = input("b=")
a = int(a)
b = int(b)
if a == b*4:
    print(a)
else:
    print(b)
 
val = input("val = ")
val = int(val)
if val%3 == 0:
    print("3의 배수")
else:
    print("3의 배수 아님")      

    a = int(input("a= "))
if a%3 ==0 and a%2 ==0:
    print(a,"3과2의 공배수")
else:
    print(a)    


i = 0
while i < 5:
    print("{}번쨰 반복입니다".format(i))
    i += 2    


x = input('x=')
x = int(x) 

if x%3 == 0:
    print(x, '는 3의 배수')
elif x%5 == 0:
    print(x, '는 5의 배수')
elif x%2 == 0:
    print(x, '는 2의 배수')          
else:
    print(x, '해당없음')      

# 빈칸(null)이거나 0 이면 false로 인식    

number = input("정수입력")
number = int(number)

#pass 넘어가기
if number > 0:

    pass
else:
    pass

print(number)

#pop의 예시 지우기만 하는게 아니라 값을 리턴도 해준다. del과 다른점
b = ['a', 'b', 'c']
x=b.pop()
print(x)
print(b)

#for문 기본 형태 for i in range(10): print(i)  (0,13,2)형태는 (시작,끝+1,간격) 이때 -1 하면 작아짐

array = [12, 23 ,52]
for ee in array:
    print(ee)


for i in range(0,101,3):
    print(i)

#range 리스트를 만드는 함수 a = list(range(3,9))  == [3,4,5,6,7,8] 


sum = 0
for i in range(1,11):
    sum += i
print(sum)

# while 
c = 0
i = 0
s = 0
while i <10:
    c = c +i
    i = i +1    
print(c)    


for i in range(10):
    s = s+i
print(s)

i = -1
while i < 30:
    print(i)
    i=i+3


for i in range(3):
    for j in range(2):
        print(i,j)

for a in range(2,10):
    for b in range(1,10):
        print("{}X{}={}".format(a,b,a*b))

d=1
while d <10:
    g=1  
    while g <10:       
        print("{} X {} = {}".format(d,g,d*g))
        g+=1
    print()
    d+=1        
