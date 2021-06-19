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

#break 해당 조건이 충족되면 밖으로 빠져나옴, 가장 안쪽의 반복문 탈출

for i in range(10):
    if i > 7:
        break
    print(i)
i = 0
while i < 10:
    print(i)
    if i >7:
        break
    i = i+1

#continue 해당 조건이 충족 되면 다시 위에 조건을 실시

for a in range(10):
    if a > 7:
        continue
    print(a)

while a < 10:
    print(a)
    if a >7:
        continue #잘못 사용시 무한루프에 걸림
    a = a+1

student = []

x = input('이름: ')

while x != "":
    student.append({'name':x})
    x = input('이름: ')

print(student) 

student = []
a = 0
b = 0
c = 0
d = 0

x = input('이름: ')
y = int(input('영어점수:'))
z = int(input('수학점수:'))


while x != "":
    student.append({'name':x,'영어점수':y,'수학점수':z})
    a = a+y
    b = b+z

    x = input('이름: ')
    if x != "":
        y = int(input('영어점수:'))
        z = int(input('수학점수:'))
        
c = a / len(student)
d = b / len(student)        
 
print("영어점수총합{}, 수학점수총합{}, 영어평균{:.1f}, 수학평균{:.1f}".format(a,b,c,d))