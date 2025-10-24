# Сумма чисел от 1 до N. Пользователь вводит число N. Используя
# цикл, найти сумму всех чисел от 1 до N.

N = int(input("Enter your number: "))
count = 0

for i in range(1, N):  # Для каждого числа i в диапазоне от 1 до n включительно — делай
    count += i

print("The sum of numbers from 1 to", N, "is", count)
