word = input("Введите строку: ")
word_even = word[1::2]
word_odd = word[::2]
print(f"Введенная строка {word.strip()}.", end="\n\n\n")
print(word_odd, word_even, sep="     ", end="\n!!!")

