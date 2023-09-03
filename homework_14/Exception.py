class ValFormatError(Exception):
    def __str__(self):
        return f"Error: Невозможно сравнить матрицы разных размеров!!!"
