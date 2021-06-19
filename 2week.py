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
