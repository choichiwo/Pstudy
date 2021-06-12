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