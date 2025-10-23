# Напиши программу, которая принимает два числа и
# выводит меньшее из них (использовать условие if).

a = int(input("Enter your number: "))
b = int(input("Enter your number: "))

if (a < b):
    print("Smaller number = ", a)
elif (a > b):
    print("Smaller number = ", b)
else:
    print("Numbers are equal!")
