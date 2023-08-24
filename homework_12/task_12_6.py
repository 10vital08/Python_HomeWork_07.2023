# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.

class Range:

    def __init__(self, min_value: int = None, max_value: int = None):

        self.min_value = min_value

        self.max_value = max_value


    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):

        return getattr(instance, self.param_name)

    def __set__(self, instance, value):

        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        print(self.min_value)

        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше или равно {self.min_value}')
        if self.max_value is not None and value >= self.max_value:
            raise ValueError(f'Значение {value} должно быть меньше {self.max_value}')


class rectangle():
    a = Range(1, 50)
    b = Range(2, 40)

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'{self.a} {self.b}'


if __name__ == '__main__':
    pr1 = rectangle(2, 4)
    pr2 = rectangle(60, 10)
    print(f'{pr1 = }')
    print(f'{pr2 = }')
    print(type(pr1.a))