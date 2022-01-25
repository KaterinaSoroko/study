while True:
    name = input("Введите ваше имя: \n")
    age = input("Введите ваш возраст: \n")
    if not age.isdigit() or int(age) <= 0:
        print("Ошибка, повторите ввод")
    elif int(age) < 10:
        print(f"Привет, шкет {name}")
    elif int(age) <= 18:
        print(f"Как жизнь, {name}?")
    elif int(age) < 100:
        print(f"Что желаете, {name}?")
    else:
        print(f"{name}, вы лжете - в наше время столько не живут...")
