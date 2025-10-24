# Количество гласных. Пользователь вводит строку.
# Посчитать, сколько в ней гласных букв.

text = input("Enter your text: ")
vowels = "EUIOAeuioa"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("number of vowel letters =", count)
