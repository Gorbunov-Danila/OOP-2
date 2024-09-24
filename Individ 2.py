#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Money:
    MAX_SIZE = 100  # Максимальная длина списка цифр

    def __init__(self, amount):
        """
        Конструктор класса Money. Принимает сумму в виде строки или числа.
        """
        if isinstance(amount, (int, float)):
            amount = f"{amount:.2f}"  # Преобразование к строке с 2 знаками для копеек
        elif not isinstance(amount, str):
            raise ValueError("Сумма должна быть строкой, целым числом или числом с плавающей точкой.")

        # Удаляем точку (десятичный разделитель) из строки
        amount = amount.replace(".", "")

        # Преобразуем строку в список цифр
        digits = [int(char) for char in amount]

        # Проверка на максимальную длину
        if len(digits) > self.MAX_SIZE:
            raise ValueError(f"Длина денежной суммы не должна превышать {self.MAX_SIZE} цифр.")

        self._digits = digits  # Список цифр суммы
        self._count = len(digits)  # Текущая длина списка
        self._size = self.MAX_SIZE  # Максимальный размер списка

    def __getitem__(self, index):
        """
        Перегрузка операции индексирования []. Возвращает цифру по индексу.
        """
        if index < 0 or index >= self._count:
            raise IndexError("Индекс выходит за пределы текущего списка цифр.")
        return self._digits[index]

    def __setitem__(self, index, value):
        """
        Перегрузка операции установки значения по индексу []. Меняет цифру.
        """
        if index < 0 or index >= self._count:
            raise IndexError("Индекс выходит за пределы текущего списка цифр.")
        if not isinstance(value, int) or not 0 <= value <= 9:
            raise ValueError("Значение должно быть целым числом от 0 до 9.")
        self._digits[index] = value

    def size(self):
        """
        Возвращает максимальный размер списка.
        """
        return self._size

    def count(self):
        """
        Возвращает текущее количество цифр в сумме.
        """
        return self._count

    def __str__(self):
        """
        Преобразует список цифр в строковое представление денежной суммы.
        Младшие две цифры — копейки.
        """
        digits_str = "".join(map(str, self._digits))  # Преобразуем цифры в строку
        if len(digits_str) <= 2:
            return f"0.{digits_str.zfill(2)}"  # Добавляем ведущие нули
        return f"{digits_str[:-2]}.{digits_str[-2:]}"  # Отделяем копейки точкой

    def __repr__(self):
        """
        Возвращает строковое представление объекта Money.
        """
        return f"Money('{str(self)}')"

    def add_digit(self, digit):
        """
        Добавляет новую цифру в список. Цифра должна быть от 0 до 9.
        """
        if self._count >= self._size:
            raise ValueError("Достигнута максимальная длина списка цифр.")
        if not isinstance(digit, int) or not 0 <= digit <= 9:
            raise ValueError("Цифра должна быть целым числом от 0 до 9.")
        self._digits.append(digit)
        self._count += 1

    def remove_last_digit(self):
        """
        Удаляет последнюю цифру в списке, если это возможно.
        """
        if self._count == 0:
            raise ValueError("Список пуст, нечего удалять.")
        self._digits.pop()
        self._count -= 1


# Пример использования класса Money
if __name__ == '__main__':
    # Создание объекта Money с суммой 1234.56 руб
    money = Money(1234.56)

    print(f"Денежная сумма: {money}")
    print(f"Размер списка цифр: {money.size()}")
    print(f"Текущая длина: {money.count()}")

    # Пример использования индексации
    print(f"Цифра на индексе 0 (самая младшая): {money[0]}")
    print(f"Цифра на индексе 2: {money[2]}")

    # Изменение цифры по индексу
    money[0] = 9
    print(f"Измененная денежная сумма: {money}")

    # Добавление новой цифры
    money.add_digit(7)
    print(f"После добавления цифры: {money}")

    # Удаление последней цифры
    money.remove_last_digit()
    print(f"После удаления последней цифры: {money}")
