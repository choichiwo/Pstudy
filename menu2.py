import os

class Menu:
    def __init__(self): #생성자가 초기화
        self.menulist=[]
        self.pricelist=[]
        if os.path.isfile("c:/tmp/menu.txt"):           
            with open("c:/tmp/menu.txt", "r") as file:
                for line in file: #한 줄씩 읽어와라
                    name, price = line.split(',')
                    price = price[0: len(price) - 1]
                    self.menulist.append(name)
                    #self.pricelist.append(price)
                    #아래 개선버전 
                    self.pricelist.append(int(price))
            
    
    def addMenu(self, name, price):
        self.menulist.append(name)
        self.pricelist.append(price)
    
    def printList(self):
        for i in range(len(self.menulist)):
            print("{},{}".format(self.menulist[i],self.pricelist[i]))

    def saveList(self):
        with open("c:/tmp/menu.txt","w") as file:
            for i in range(len(self.menulist)):
                file.write("{},{}\n".format(self.menulist[i],self.pricelist[i]))
           



