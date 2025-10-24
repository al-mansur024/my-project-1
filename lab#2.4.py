# Таблица умножения Выведи таблицу умножения для числа N
# (от 1 до 10).

N = int(input("Enter your number: "))
count = 0

for i in range(1, 11):
    print(N, '*', i, '=', (N*i))
