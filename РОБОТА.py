input_string = input("Введіть рядок слів, розділених пробілами: ")
words = input_string.split()
max_count = 0
word_with_max_a = ""
for word in words:
    count_a = word.count('а')  # Рахуємо кількість 'а' у слові
    if count_a > max_count:
        max_count = count_a
        word_with_max_a = word
if word_with_max_a:
    print(f"Слово з найбільшою кількістю літер 'а': {word_with_max_a}")
else:
    print("У жодному слові немає літери 'а'.")