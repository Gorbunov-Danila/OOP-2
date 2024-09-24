#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Money:
    valid_nominals = [1, 2, 5, 10, 50, 100, 500, 1000, 5000]  # допустимые номиналы

    def __init__(self, first, second):
        # Проверка корректности номинала
        if first not in self.valid_nominals:
            raise ValueError(f"Неверный номинал: {first}. Допустимые значения: {self.valid_nominals}")
        # Проверка корректности количества купюр
        if not isinstance(second, int) or second <= 0:
            raise ValueError("Количество купюр должно быть целым положительным числом.")
        self.first = first  # Номинал купюры
        self.second = second  # Количество купюр

    def summa(self):
        """Метод для вычисления общей суммы."""
        return self.first * self.second

    def __str__(self):
        """Строковое представление объекта."""
        return f"Номинал: {self.first} руб., Количество: {self.second} шт."

    # Перегрузка оператора сложения (+)
    def __add__(self, other):
        if isinstance(other, Money) and self.first == other.first:
            return Money(self.first, self.second + other.second)
        else:
            raise ValueError("Нельзя сложить купюры разного номинала.")

    # Перегрузка оператора вычитания (-)
    def __sub__(self, other):
        if isinstance(other, Money) and self.first == other.first:
            if self.second >= other.second:
                return Money(self.first, self.second - other.second)
            else:
                raise ValueError("Нельзя вычесть большее количество купюр, чем имеется.")
        else:
            raise ValueError("Нельзя вычесть купюры разного номинала.")

    # Перегрузка оператора умножения (*) для умножения на целое число
    def __mul__(self, multiplier):
        if isinstance(multiplier, int) and multiplier > 0:
            return Money(self.first, self.second * multiplier)
        else:
            raise ValueError("Умножение возможно только на положительное целое число.")

    # Перегрузка оператора сравнения (==)
    def __eq__(self, other):
        if isinstance(other, Money):
            return self.summa() == other.summa()
        return False

    # Перегрузка оператора сравнения (!=)
    def __ne__(self, other):
        return not self.__eq__(other)

    # Перегрузка оператора сравнения (<)
    def __lt__(self, other):
        if isinstance(other, Money):
            return self.summa() < other.summa()
        return False

    # Перегрузка оператора сравнения (>)
    def __gt__(self, other):
        return other.__lt__(self)

    # Перегрузка оператора сравнения (<=)
    def __le__(self, other):
        return not self.__gt__(other)

    # Перегрузка оператора сравнения (>=)
    def __ge__(self, other):
        return not self.__lt__(other)


# Пример использования
if __name__ == '__main__':
    money1 = Money(100, 5)  # 5 купюр по 100 рублей
    money2 = Money(100, 3)  # 3 купюры по 100 рублей
    money3 = Money(50, 10)  # 10 купюр по 50 рублей

    # Демонстрация перегрузки операторов
    print(f"money1: {money1}")
    print(f"money2: {money2}")
    print(f"Сумма money1: {money1.summa()} руб.")
    print(f"Сумма money2: {money2.summa()} руб.")

    # Сложение
    money_sum = money1 + money2
    print(f"money1 + money2: {money_sum} (Общая сумма: {money_sum.summa()} руб.)")

    # Вычитание
    money_sub = money1 - money2
    print(f"money1 - money2: {money_sub} (Общая сумма: {money_sub.summa()} руб.)")

    # Умножение
    money_mul = money1 * 2
    print(f"money1 * 2: {money_mul} (Общая сумма: {money_mul.summa()} руб.)")

    # Сравнение
    print(f"money1 == money2: {money1 == money2}")
    print(f"money1 > money2: {money1 > money2}")
    print(f"money1 < money3: {money1 < money3}")
