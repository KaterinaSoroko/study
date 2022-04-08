# калькулятор

class ComplexError(Exception):
    def __init__(self, massage="Результатом вычисления будет комплексное число"):
        super().__init__(massage)


class Calculator:

    def __init__(self, x=1, y=1):
        self.x = x
        self.y = y

    @staticmethod
    def check_args(args):

        def check_numbers(z):
            try:
                z.strip(",")
                if z.isdigit() or z[0] == "-" and z[1:].isdigit():
                    z = int(z)
                else:
                    z = float(z)
            except ValueError:
                z = None
            return z

        args = args.strip()
        if args != "":
            lst = args.split()
            lst = list(filter(lambda x: isinstance(x, (int, float)), (map(check_numbers,  lst))))
            return lst

    # сложение
    def add(self, args):
        try:
            args = self.check_args(args)
            x, y = args[0], args[1]
        except IndexError:
            print("Введены некорректные данные")
            x = self.x
            y = self.y
        print(x + y)

    # вычитание
    def sub(self, args):
        try:
            args = self.check_args(args)
            x, y = args[0], args[1]
        except IndexError:
            print("Введены некорректные данные")
            x = self.x
            y = self.y
        print(x - y)

    # умножение
    def mul(self, args):
        try:
            args = self.check_args(args)
            x, y = args[0], args[1]
        except IndexError:
            print("Введены некорректные данные")
            x = self.x
            y = self.y
        print(x * y)

    # деление
    def truediv(self, args):
        try:
            args = self.check_args(args)
            x, y = args[0], args[1]
        except IndexError:
            print("Введены некорректные данные")
            x = self.x
            y = self.y
        try:
            print(x / y)
        except ZeroDivisionError:
            print("Делить на 0 нельзя!")

    # возведение в степень
    def pow_n(self, args):
        try:
            args = self.check_args(args)
            x, y = args[0], args[1]
            result = pow(x, y)
            if isinstance(result, complex):
                raise ComplexError
        except IndexError:
            print("Введены некорректные данные")
            print(pow(self.x, self.y))
        except ComplexError as err:
            print(err)
        else:
            print(result)

    # корень
    def sqrt_n(self, args):
        try:
            args = self.check_args(args)
            x, y = args[0], args[1]
            result = pow(x, 1 / y)
            if isinstance(result, complex):
                raise ComplexError
        except IndexError:
            print("Введены некорректные данные")
            print(pow(self.x, 1 / self.y))
        except ComplexError as err:
            if y % 2 == 1:
                print(-1 * pow(abs(x), 1 / y))
            else:
                print(err)
        else:
            print(result)


calc = Calculator()

while True:
    print("""+ Сложение
- Вычитание
* Умножение
/ Деление
^ Возведение в степень
$ Извлечение корня
0 Выход""")
    action = input("Выберете действие: ").strip()

    operation = {
        "+": calc.add,
        "-": calc.sub,
        "*": calc.mul,
        "/": calc.truediv,
        "^": calc.pow_n,
        "$": calc.sqrt_n
    }

    try:
        if action == "0":
            break
        operation[action](input("Введите 2 числа (1 2): "))
    except KeyError:
        print("Вы ввели некоректные данные")
    print("_" * 20)
