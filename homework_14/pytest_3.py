import pytest

from homework_14.Exception import ValFormatError
from homework_14.matrix_1 import Matrix

'''  Проверка сложения двух матриц '''


def test_sum():
    assert (str(Matrix([[1, -2], [25, -5]]) + Matrix([[11, -8], [15, 0]]))) == '[12, -10][40, -5]', "Неверная сумма!"


''' Проверка произведение двух матриц '''


def test_mul():
    assert (str(Matrix([[1, -2], [25, -5]]) * Matrix(
        [[11, -8], [15, 0]]))) == '[-19, -8][200, -200]', "Неверное произведение!"


''' Проверка выброса исключений на неправильный формат матриц '''


def test_format():
    with pytest.raises(ValFormatError):
        Matrix([[1, -2], [25, -5]]) + Matrix([[11, -8], [15, 0], [16, 10]])
        Matrix([[1, -2], [25, -5]]) * Matrix([[11, -8], [15, 0], [16, 10]])


if __name__ == '__main__':
    pytest.main(['-v'])
