# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

    
    
def decimal_to_hex(decimal):
    hex_digits = "0123456789ABCDEF"
    result = ""
    
    if decimal == 0:
        return "0"
    
    while decimal > 0:
        remainder = decimal % 16
        result = hex_digits[remainder] + result
        decimal = decimal // 16
    
    return result

# Пример использования программы
decimal_number = int(input("Введите целое число: "))

# Преобразование в шестнадцатеричное представление
hexadecimal_number = decimal_to_hex(decimal_number)
print("Шестнадцатеричное представление:", hexadecimal_number)

# Проверка с использованием функции hex
hex_check = hex(decimal_number).lstrip("0x").upper()
print("Проверка с использованием функции hex:", hex_check)
    
