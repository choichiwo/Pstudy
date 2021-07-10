class Menu:
    def __init__(self): #생성자가 초기화
        self.menulist=[]
        self.pricelist=[]
        print("메뉴 인스턴스가 생성되었습니다.")
    
    def getMenu(self):
        self.menu_name = input("메뉴명:")
        self.price = input("가격:")
    
    def addMenu(self,menu_name,price):
        self.menulist.append(menu_name)
        self.pricelist.append(price)
    
    def printList(self):
        for i in range(len(self.menulist)):
            print("이름: {}, 가격: {}".format(self.menulist[i],self.pricelist[i]))    