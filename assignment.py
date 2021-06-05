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