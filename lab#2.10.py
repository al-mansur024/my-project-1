# Поиск элемента в массиве. Пользователь вводит массив чисел
# и одно число X. Проверить, содержится ли число X в массиве.

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

x = int(input("Enter number X:"))

if x in numbers:
    print("Number", x, "is in the array")
else:
    print("Number", x, "not in array")
