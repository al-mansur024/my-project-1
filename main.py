# Напиши программу, которая принимает два числа и
# выводит меньшее из них (использовать условие if).
a = int(input("Enter your number: "))
b = int(input("Enter your number: "))

if (a > b):
    print("Smaller number = ", b)
elif (b > a):
    print("Smaller number = ", a)
else:
    print("Numbers are equal!")
