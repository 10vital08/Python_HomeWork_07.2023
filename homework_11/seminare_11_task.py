# Задача 1

# Создайте класс 'Моя Строка', где:
# будут доступны все возможности str,
# дополнительно хранятся имя автора строки и время создания (time.time).

# import time
# class MyString(str):
#     '''Расширяемый класс str.'''
#
#     def __new__(cls, text, nameAuthor):
#         '''Расширяемый метод new параметрами text и nameAuthor.'''
#         instance = super().__new__(cls, text)
#         instance.nameAuthor = nameAuthor
#         instance.t = time.time()
#         instance.author = nameAuthor
#         return instance
#
#     def __str__(self):
#         '''Переопределенный дандер метод строчного выведения экземпляра класса.'''
#         return self + " " + f'{self.nameAuthor} {self.t}'
#
#
# text = """Author comment"""
# d = MyString(text, "Alex")
# print(d.__dict__)
# # print(d.nameAuthor)
# # print(d.t)
# # print(d.upper())
# # help(d)
# # help(MyString)

# Задача 2

# Создайте класс 'Архив', который хранит пару свойств.
# Например, число и строку.
# При создании нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков архивов,
# list-архивы также являются свойствами экземпляра.

# class Archive():
#     _flag = None
#     """Почему комментарии в самом классе? Потому что это документация ©Зухра"""
#
#
#     def __new__(cls, number, text):
#         """"Непонятная функция заполняет архив старыми значениями."""
#
#         if cls._flag == None:
#             cls._flag = super().__new__(cls)
#             cls._flag.archNumber = []
#             cls._flag.archText = []
#         elif cls._flag != None:
#             cls._flag.archText.append(cls._flag.text)
#             cls._flag.archNumber.append(cls._flag.number)
#         return cls._flag
#
#     def __init__(self, number, text):
#         self.number = number
#         self.text = text
#
#     def __str__(self):
#         return f'{"".join(x for x in self.archText)} - архив,  текущий номер {self.number}'
#
#     def __repr__(self):
#         return f'{self.text}'
#
#     def docs(self):
#         return self.__doc__
#
# t = Archive(12, "jksagdjsagdkjalhsdk aksjdhlka jahdk kjahs")
# t2 = Archive(12, "jksagdjsagdkjalhsdk sadqqqqq qqqq")
# print()
# print(t2)
# print(repr(t2))

# Задача 3

# Добавьте к задачам 1 и 2 строки документации для классов.

# Задача 4

# Доработаем класс 'Архив' из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.

# Задача 5

# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

# class Rectangle:
#     '''Класс прямоугольник, с методами расчета периметра и площади фигуры.'''
#
#     def __init__(self, side_a: int = 1, side_b: int | None = None):
#         '''Метод инициализации прямоугольника со сторонами a и b.'''
#         self._side_a = side_a
#         self._side_b = side_b if side_b else side_a
#
#     def get_perimeter(self):
#         '''Метод расчета периметра прямоугольника.'''
#         return 2 * (self._side_a + self._side_b)
#
#     def get_area(self):
#         '''Метод расчета площади прямоугольника.'''
#         return self._side_a * self._side_b
#
#     def __add__(self, other):
#         '''Переопределенный дандер метод сложения двух прямоугольников.'''
#         return Rectangle(self._side_a + other._side_a, self._side_b + other._side_b)
#
#     def __sub__(self, other):
#         '''Переопределенный дандер метод вычетания двух прямоугольников.'''
#         return Rectangle(abs(self._side_a - other._side_a), abs(self._side_b - other._side_b))
#
#     def __str__(self):
#         '''Переопределенный дандер метод строчного выведения экземпляра класса.'''
#         return f"прямоугольник со сторонами: {self._side_a} и {self._side_b}; периметром: {self.get_perimeter()}"
#
#
# if __name__ == '__main__':
#     rect1 = Rectangle(4, 6)
#     rect2 = Rectangle(2, 3)
#     rect3 = rect1 + rect2
#     print(rect3)
#
#     rect4 = rect1 - rect2
#     print(rect4)
#
#    # help(Rectangle)

# Задача 6

# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади.
# Должны работать все шесть операций сравнения.

class Rectangle:
    '''Класс прямоугольник, с методами расчета периметра и площади фигуры.'''

    def __init__(self, side_a: int = 1, side_b: int | None = None):
        '''Метод инициализации прямоугольника со сторонами a и b.'''
        self._side_a = side_a
        self._side_b = side_b if side_b else side_a

    def get_perimeter(self):
        '''Метод расчета периметра прямоугольника.'''
        return 2 * (self._side_a + self._side_b)


    def get_area(self):
        '''Метод расчета площади прямоугольника.'''
        return self._side_a * self._side_b

    def __add__(self, other):
        '''Переопределенный дандер метод сложения двух прямоугольников.'''
        return Rectangle(self._side_a + other._side_a, self._side_b + other._side_b)

    def __sub__(self, other):
        '''Переопределенный дандер метод вычетания двух прямоугольников.'''
        return Rectangle(abs(self._side_a - other._side_a), abs(self._side_b - other._side_b))

    def __lt__(self, other):
        '''Метод lt используется для определения или реализации функциональности оператора «меньше чем» «<».
        Он возвращает логическое значение в соответствии с условием, т. е. возвращает true, если a<b,
        где a и b — объекты класса.'''
        return self.get_area() < other.get_area()

    def __gt__(self, other):
        '''Метод gt определяет поведение оператора сравнения «больше», >.'''
        return self.get_area() > other.get_area()

    def __eq__(self, other):
        '''Метод eq используется для определения поведения оператора равенства (==) для объектов класса.
        Это позволяет вам указать, как объекты класса должны сравниваться на предмет равенства.'''
        return self.get_area() == other.get_area()

    def __le__(self, other):
        '''Метод lt («меньше равно») может возбудить исключение NotImplemented,
        если сравнение для указанной пары аргументов не реализовано.
        В соответствии с договорённостью, в случае успешного сравнения возвращает True , либо False.'''
        return self.get_area() <= other.get_area()

    def __ge__(self, other):
        '''Метод ge позволяет реализовать проверку на «больше равно» для экземпляров пользовательских типов.
        self : ссылка на экземпляр.
        other : объект с которым следует произвести сравнение (справа от оператора сравнения).'''
        return self.get_area() >= other.get_area()

    def __ne__(self, other):
        '''Метод ne определяет поведение оператора «неравенства».'''
        return self.get_area() != other.get_area()

    def __str__(self):
        '''Переопределенный дандер метод строчного выведения экземпляра класса.'''
        return f"прямоугольник со сторонами: {self._side_a} и {self._side_b}; периметром: {self.get_perimeter()}; площадью: {self.get_area()}"


if __name__ == '__main__':
    rect1 = Rectangle(2, 3)
    rect2 = Rectangle(2, 3)
    rect3 = rect1 + rect2
    print(rect3)

    rect5 = Rectangle(2, 2)
    rect6 = Rectangle(3, 3)
    print(rect1 < rect2)
    print(rect1 > rect2)
    print(rect1 <= rect2)
    print(rect1 >= rect2)
    print(rect1 == rect2)
    print(rect1 != rect2)

    # help(Rectangle)