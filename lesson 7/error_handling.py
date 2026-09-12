try:
    result=10/0
except ZeroDivisionError:
    print("OOps you tried to divide by zero")

fruits = {
    "apple":5,
    "banana":7,
    "orange":3
}

try:
    print(fruits["cherry"])

except KeyError:
    print("The key does not exist in the directory")


text = "hello this is not a number"

try:
    text_to_int = int(text)
except Exception as e:
    print("ka ndodh nje error gjat shendrrimit te tekstit ne numer")


try:
    result=10/2
except ZeroDivisionError:
    print("OOps you tried to divide by zero")
else:
    print("Finally block executed")

try:
    result=10/0
except ZeroDivisionError:
    print("OOps you tried to divide by zero")
finally:
    print("Ky line of code ekzekutohet cdo her")