class Menu:
    def __init__(self):
        self.menulist=[]
        self.pricelist=[]
    
    def getMenu(self):
        name = input("메뉴명:")
        price = input("가격:")
    
    def addMenu(self,menuname,price):
        self.menulist.append(menuname)
        self.pricelist.append(price)
    
    def printList(self):
        for i in range(len(self.menulist)):
            print(self.menulist[i],self.pricelist[i])    