"""1.Доработаем задачи 5-6. Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики."""


class Animals:
    def __init__(self, name):
        self.name = name

    def animal_name(self):
        return f'Имя: {self.name}'


class Fish(Animals):
    def __init__(self, name, depth):
        super().__init__(name)
        self.depth = depth

    def get_info(self):
        return f'Глубина обитания {self.name} = {self.depth} m'


class Birds(Animals):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def get_info(self):
        return f'Размах крыльев {self.name} = {self.wingspan} sm'


class Reptiles(Animals):
    def __init__(self, name, length):
        super().__init__(name)
        self.length = length

    def get_info(self):
        return f'Длина тела {self.name} = {self.length} m'


class FabricAnimal:
    def __init__(self, animal_class: str, *args, **kwargs):
        self.animal_class = animal_class

        for key, value in kwargs.items():
            if key == 'name':
                self.name = value
            if key == 'depth':
                self.depth = value
            if key == 'wingspan':
                self.wingspan = value
            if key == 'length':
                self.length = value

    def get_info_animal(self):
        if self.animal_class == 'Fish':
            return Fish(self.name, self.depth)
        elif self.animal_class == 'Birds':
            return Birds(self.name, self.wingspan)
        elif self.animal_class == 'Reptiles':
            return Reptiles(self.name, self.length)


if __name__ == '__main__':
    animal_1 = FabricAnimal(animal_class='Fish', name='Форелька', depth=5).get_info_animal()
    print(animal_1.get_info())

    animal_2 = FabricAnimal(animal_class='Reptiles', name='Рептилия_из_Mortal_Kombat', length=2).get_info_animal()
    print(animal_2.get_info())
