z = int(input("Скільки слів ви хочете ввести? "))
words = [input(f"Введіть слово {i+1}: ") for i in range(z)]
max_length = max(len(word) for word in words)
equal_length_words = [word.rjust(max_length, '&') for word in words]
print("Слова, вирівняні до однакової довжини:")
for word in equal_length_words:
    print(word)