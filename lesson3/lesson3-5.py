from random import randint


name = input("Как Вас зовут? \n")
while name == "" or not name.isalpha():
    print("Вы не ввели имя. Давайте повторим.")
    name = input("Как Вас зовут? \n")
print(f"Здравствуй, {name}. Я загадаю число от 1 до 100, попробуй угадать. Я буду подсказывать.")

while True:
    number = randint(1, 100)
    print("Загадал!")
    num = -1
    count = 0
    while num != number:
        num_str = input("Ваш вариант: \n")
        count += 1
        while not num_str.isdigit():
            print("Вы ввели не целое число. Попробуйте еще раз.")
            num_str = input("Ваш вариант: \n")
        else:
            num = int(num_str)
        if num < 1 or num > 100:
            print("Ваше число не попало даже в диапазон чисел от 1 до 100. Зря потратили попытку")
        elif num > number:
            print("Ваше число больше загаданного")
        elif num < number:
            print("Ваше число меньше загаданного")
    else:
        print(f"Правильно! Я загадал число {number}. Вы угадали с {count} раза.")
    flag = input("Хотите сыграть еще? (Y, Д / N, Н): \n")
    while flag.upper() not in ("Y", "N", "Д", "Н"):
        print("Ваш ответ не понятен.")
        flag = input("Хотите сыграть еще? (Y, Д / N, Н): \n")
    if flag.upper() in ("N", "Н"):
        break

print(f"До свиданья, {name}")
