# Разворот строки. Программа принимает строку и выводит её
# в обратном порядке.

text = input("Enter your text: ")
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text
print("Reversed:", reversed_text)
