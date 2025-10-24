# Максимум в массиве. Пользователь вводит массив чисел
# (например, через пробел). Найти максимальное число в массиве.

numbers = input("Enter numbers sepated by spaces: ").split()
numbers = [int(num) for num in numbers]

max_num = numbers[0]

for num in numbers:
    if max_num < num:
        max_num = num
print("Максимальное число:", max_num)
