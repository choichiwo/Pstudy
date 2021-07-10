import menu as m

newmenu = m.Menu()

while True:
    newmenu.getMenu()
    if newmenu.menu_name == "":
        break
    else:
        newmenu.addMenu(newmenu.menu_name, newmenu.price)

newmenu.printList()    
    

