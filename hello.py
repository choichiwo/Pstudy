#file = open("d:/menu.txt","w")
with open("d:/menu.txt","w") as file: #close를 안써두 됨
file.write("모카 3500\n") #\n 줄바꿈
file.write("라떄 3000\n")
file.write("카푸치노 3700\n")
#file.close()


file = open("d:/menu.txt","r")
line=file.read()
print(line)
file.close()