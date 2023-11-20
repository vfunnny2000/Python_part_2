import argparse
import logging

logging.basicConfig(filename='remove_duplicates.log', encoding='utf-8',level=logging.DEBUG)

def remove_duplicates(lst):
    try:
        unique_list = list(set(lst))
        logging.info("Успешно удалены дубликаты.")
        return unique_list
    except Exception as e:
        error_message = f"Ошибка при удалении дубликатов: {str(e)}"
        logging.error(error_message)
        return error_message

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove duplicates from a list.")
    parser.add_argument('input_list', nargs='+', type=int, help='List of integers with duplicates.')

    args = parser.parse_args()
    input_list = args.input_list

    result = remove_duplicates(input_list)
    print(result)
# Изменения включают в себя:

# Добавление модуля argparse для обработки аргументов командной строки.
# Замена жестко закодированного списка my_list на аргумент командной строки input_list.
# Обертывание кода в функцию remove_duplicates для обработки ошибок и добавления логирования.
# Использование logging.error и logging.info для записи информации в лог.


