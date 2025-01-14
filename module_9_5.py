# Домашнее задание по теме "Итераторы"

# объявление класса StepValueError , который наследуется от ValueError.
class StepValueError(ValueError):
    def __init__(self, message):
        self.message = message
        # pass


# объявление класса Iterator
class Iterator:
    # метод инициализации атрибутов класса
    def __init__(self, start, stop, step=1):
        # присвоение self.step значения step при условии не равенства 0
        if self._step(step):
            self.step = step
        # присвоение остальных значений атрибутам класса
        self.start = start
        self.stop = stop
       
    # метод проверки значения step на равенство 0 и формирование исключения
    def _step(self, stp):
        if stp == 0:
            raise StepValueError('шаг не может быть равен 0')
        # возврат при валидности значения
        return True

    # метод __iter__, сбрасывающий значение pointer на start
    def __iter__(self):
        # присвоение значения start атрибуту self.pointer
        self.pointer = self.start
        # возврат метода атрибут pointer
        return self

    # метод __next__, увеличивающий атрибут pointer на step
    def __next__(self):
        # присвоение res значения pointer
        res = self.pointer
        # условие проверки знака step и достижения pointer атрибута stop
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            # выход из итерации при выполнении условия
            raise StopIteration()
        # увеличение pointer на step
        self.pointer += self.step
        # возврат работы метода
        return res


# исходные данные и вывод на консоль при помощи цикла for
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError as exc:
    print('Шаг указан неверно')
    print(exc.message)

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
