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

