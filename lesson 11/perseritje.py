"""file = open("example.txt","r")

content = file.read()

print(content)

file.close()


"""
import os
with open("example2.txt","r") as file:
    content = file.read()
    print(content)

#with open("example2.txt","w") as file:
 #   file.write("hello donjeta")


with open("example2.txt","a") as file:
    file.write("\nhello donjeta")


if os.path.exists("gg.txt"):
    print("file ekziston")
else:
    print("fili nuk ekziston")