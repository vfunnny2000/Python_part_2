# Напишите программу банкомат. 
# ✔Начальная сумма равна нулю 
# ✔Допустимые действия: пополнить, снять, выйти 
# ✔Сумма пополнения и снятия кратны 50 у.е. 
# ✔Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е. 
# ✔После каждой третей операции пополнения или снятия начисляются проценты - 3% 
# ✔Нельзя снять больше, чем на счёте 
# ✔При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной 
# ✔Любое действие выводит сумму денег


import logging
import argparse

logging.basicConfig(filename='bank_atm.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def bank_atm(start_amount):
    # Функция для пополнения счета
    def deposit(amount):
        nonlocal start_amount
        start_amount += amount
        logging.info(f"Пополнение счета на {amount} у.е.")

    # Функция для снятия со счета
    def withdraw(amount):
        nonlocal start_amount
        if amount <= start_amount:
            start_amount -= amount
            logging.info(f"Снятие со счета {amount} у.е.")
        else:
            logging.error("Недостаточно средств на счете.")

    # Функция для расчета процента за снятие
    def calculate_withdraw_fee(amount):
        fee = amount * 0.015
        fee = max(fee, 30)
        fee = min(fee, 600)
        return fee

    # Функция для начисления процентов после каждой третьей операции
    def calculate_interest():
        nonlocal start_amount
        start_amount *= 1.03
        logging.info("Начисление процентов на счет.")

    # Функция для вычисления налога на богатство
    def calculate_wealth_tax(amount):
        tax = amount * 0.1
        return tax

    logging.info("Запуск программы банкомат.")

    while True:
        action = input("Выберите действие (пополнить, снять, выйти): ")
        if action == "пополнить":
            amount = int(input("Введите сумму для пополнения: "))
            if amount % 50 == 0:
                deposit(amount)
                calculate_interest()
            else:
                logging.error("Сумма пополнения должна быть кратна 50 у.е.")
        elif action == "снять":
            amount = int(input("Введите сумму для снятия: "))
            if amount % 50 == 0:
                if start_amount > 5000000:
                    wealth_tax = calculate_wealth_tax(amount)
                    start_amount -= wealth_tax
                    logging.info(f"Вычет налога на богатство {wealth_tax} у.е.")
                fee = calculate_withdraw_fee(amount)
                withdraw(amount + fee)
                calculate_interest()
            else:
                logging.error("Сумма снятия должна быть кратна 50 у.е.")
        elif action == "выйти":
            logging.info("Завершение программы банкомат.")
            break
        else:
            logging.error("Недопустимое действие.")

        logging.info(f"Текущая сумма денег: {start_amount} у.е.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Программа банкомат')
    parser.add_argument('start_amount', type=int, help='начальная сумма денег')
    args = parser.parse_args()
    
    bank_atm(args.start_amount)
