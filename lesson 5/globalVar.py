
def sayHello():
    global mesazhi

    mesazhi = "Hi there!"
    return mesazhi


sayHello()
print(mesazhi)




def fullName():
    global name
    global surname

    name="donjeta"
    surname="zogaj"
    return name+surname

print(fullName())

print(name)