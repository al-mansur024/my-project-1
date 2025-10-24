# Сумма элементов массива. Найти сумму всех элементов массива.

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

count_num = 0

for num in numbers:
    count_num += num
print("Sum_numbers: ", count_num)
