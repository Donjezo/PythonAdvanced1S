studentat = ["Eldoni","Suela","Rudina","Liza","Dua","Ylli","YlliC","Uniku","Trimi"]

print(studentat)
print(studentat[0])
print(studentat[1])
print(studentat[8])

#studentat.reverse()


studentat.append("Donjeta")
studentat.insert(5,"Donjeta")

print(studentat.count("Donjeta"))
studentat.remove("Trimi")


lista2 = studentat.copy()
lista2.clear()
print(lista2)
print("ylli eshte ne pozicionin e : ",studentat.index("Ylli"))

print(studentat)