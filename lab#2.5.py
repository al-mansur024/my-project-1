# Факториал числа. Пользователь вводит число N. Найти факториал
# числа N с помощью цикла.

N = int(input("Enter your number: "))
fact = 1

for i in range(1, N + 1):
    fact *= i

print(N, '!', '=', fact)
