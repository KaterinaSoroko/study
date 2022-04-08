# Сделать функцию для фильтрации емейла (регуляркой)
# Правила валидации имейлов «username@hostname»:
# username может в себе содержать:
# 	- латиницу
# 	- цифры
# 	- знаки ! # $ % & ‘ * + — / = ? ^ _ ` { | } ~
# 	- точку, за исключением первого и последнего знака,
#   	которая не может повторяться (может быть только 1 точка или не быть)
# hostname состоит из нескольких компонентов, разделённых точкой и не
# превышающих 63 символа. Компоненты, в свою очередь, состоят из латинских
# букв, цифр и дефисов, причём дефисы не могут быть в начале или в конце компонента.


# Создать генератор геометрической прогрессии
"""
>>> func_1 = geometric_progression_generator(2, 2)
>>> print(next(func_1))
2
>>> print(next(func_1))
4
>>> print(next(func_1))
8
>>> print(next(func_1))
16
>>> func_2 = geometric_progression_generator(2, 100)
>>> print(next(func_2))
2
>>> print(next(func_1))
32
>>> print(next(func_2))
200
"""


def geometric_progression_generator(number, step=2):
    while True:
        yield number
        number *= step


a = geometric_progression_generator(1, 5)
for item in range(11):
    print(f"5 в степени {item} равно {next(a)}")


if __name__ == "__main__":
    import doctest
    doctest.testmod()



