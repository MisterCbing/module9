def create_operation(operation):
    if operation == "multiply":
        def multiply(x, y):
            return x * y
        return multiply
    elif operation == "division":
        def division(x, y):
            try:
                return x / y
            except:
                return 'Error: Division by zero'
        return division
print('Задача 1: Фабрика Функций')
my_func_mul = create_operation('multiply')
my_func_div = create_operation("division")
print(my_func_mul(3, 2))
print(my_func_div(2, 1))
print(my_func_div(2, 0))

print('Задача 2: Лямбда-Функции')
squaring = lambda x: x ** 2
print(squaring(4))
def squaring(x):
    return x ** 2
print(squaring(4))

class Rect():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(f'Стороны прямоугольника равны {a} и {b}')

    def __call__(self):
        return f'Площадь прямоугольника равна {self.a * self.b}'

print('Задача 3: Вызываемые Объекты')
abcd = Rect(2, 4)
print(abcd())