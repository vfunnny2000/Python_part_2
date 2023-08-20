# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и *произведение дробей. 
# Для проверки своего кода используйте модуль fractions.

def parse_fraction(fraction):
    numerator, denominator = map(int, fraction.split('/'))
    return numerator, denominator

def add_fractions(fraction1, fraction2):
    num1, den1 = parse_fraction(fraction1)
    num2, den2 = parse_fraction(fraction2)
    numerator = (num1 * den2) + (num2 * den1)
    denominator = den1 * den2
    return str(numerator) + '/' + str(denominator)

def multiply_fractions(fraction1, fraction2):
    num1, den1 = parse_fraction(fraction1)
    num2, den2 = parse_fraction(fraction2)
    numerator = num1 * num2
    denominator = den1 * den2
    return str(numerator) + '/' + str(denominator)

# Пример использования программы
fraction1 = input("Введите первую дробь (в формате a/b): ")
fraction2 = input("Введите вторую дробь (в формате a/b): ")

# Сложение дробей
sum_fraction = add_fractions(fraction1, fraction2)
print("Сумма дробей:", sum_fraction)

# Умножение дробей
product_fraction = multiply_fractions(fraction1, fraction2)
print("Произведение дробей:", product_fraction)


from fractions import Fraction

# Пример использования fractions
fraction1 = Fraction(fraction1)
fraction2 = Fraction(fraction2)

# Сложение дробей
sum_fraction = fraction1 + fraction2
print("Сумма дробей (с использованием fractions):", sum_fraction)

# Умножение дробей
product_fraction = fraction1 * fraction2
print("Произведение дробей (с использованием fractions):", product_fraction)

