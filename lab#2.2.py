# Четное или нечетное. Пользователь вводит число. Определить,
# четное оно или нет, и вывести соответствующее сообщение.

a = int(input("Enter your number: "))

if (a % 2) == 0:
    print("even number!")
else:
    print("odd number!")
