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

