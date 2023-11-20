# ## 
# 

# Напишите код, который запрашивает число и сообщает является ли оно простым
# или составным. Используйте правило для проверки: «Число является простым,
# если делится нацело только на единицу и на себя». Сделайте ограничение на
# ввод отрицательных чисел и чисел больше 100 тысяч.
# 


import sys
import logging
from datetime import datetime

logging.basicConfig(filename='prime_checker.log', encoding='utf-8', level=logging.INFO)

def is_prime(num):
    if num < 0 or num > 100_000:
        error_message = "Введено недопустимое число. Допустимы числа от 0 до 100_000."
        logging.error(f"{num} {error_message} (Время: {datetime.now()})")
        return error_message

    if num == 1 or num == 0:
        info_message = "Число не является ни простым, ни составным."
        logging.info(f"{num} {info_message} (Время: {datetime.now()})")
        return info_message

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            info_message = "Число составное."
            logging.info(f"{num} {info_message} (Время: {datetime.now()})")
            return info_message
    
    info_message = "Число простое."
    logging.info(f"{num} {info_message} (Время: {datetime.now()})")
    return info_message

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python script.py <число>")
        sys.exit(1)

    try:
        input_num = int(sys.argv[1])
    except ValueError:
        print("Ошибка: Введенное значение не является целым числом.")
        sys.exit(1)

    result = is_prime(input_num)
    # print(result)


# Использование модуля datetime для получения текущего времени.
# Добавление времени в сообщения логирования.
# Обработка ошибки, если введенное значение из командной строки не является целым числом.
# Замена ввода числа из input() на параметр функции is_prime(num).