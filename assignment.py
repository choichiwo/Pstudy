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