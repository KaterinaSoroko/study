from random import randint


name = input("Как Вас зовут? \n")
print(f"Здравствуй, {name}. Я загадаю число от 1 до 100, попробуй угадать. Я буду подсказывать.")

while True:
    number = randint(1, 100)
    print("Загадал")
    num = -1
    count = 0
    while int(num) != number:
        num = input("Ваш вариант: \n")
        count += 1
        if not num.isdigit():
            print("Вы ввели не число")
        elif int(num) > number:
            print("Ваше число больше загаданного")
        elif int(num) < number:
            print("Ваше число меньше загаданного")
    else:
        print(f"Правильно! Я загадал число {number}. Вы угадали с {count} раза")
    flag = input("Хотите сыграть еще? (Y/Д): \n")
    if flag.upper() not in ("Y", "Д"):
        break

print(f"До свиданья, {name}")