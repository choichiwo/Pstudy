import menu2 
m = menu2.Menu()

name = input("메뉴명: ")
while name != "":
    price = input("가격: ")
    m.addMenu(name, price)
    name = input("메뉴명: ")

m.printList()
m.saveList()