def plus(n):
    output = 0
    for i in range(1, n+1):
        output = output+1
    return output

x = plus(10)
print(x)        

def pluss(n):
    if n== 1:
        return 1
    else:
        return n+pluss(n-1)
print(pluss(10))        

