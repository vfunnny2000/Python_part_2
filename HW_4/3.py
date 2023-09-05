# Возьмите задачу о банкомате из семинара 2. ]
# Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

from datetime import date

bank = 0
count = 0
percent_take = 0.015
percent_add = 0.03
percent_tax = 0.01

def add_bank(cash: float) -> None:
    global bank
    global count
    bank += cash
    count += 1
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("начислены проценты в размере: ", percent_add * bank)

def take_bank(cash: float) -> None:
    global bank
    global count
    bank -= cash
    count += 1

    if cash * percent_take < 30:
        bank -= 30
        print("списаны проценты за обналичивание: ", 30)
    elif cash * percent_take > 600:
        bank -= 600
        print("списаны проценты за обналичивание: ", 600)
    else:
        bank -= cash * percent_take
        print("списаны проценты за обналичивание: ", cash * percent_take)
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("начислены проценты в размере: ", percent_add * bank)


def exit_bank():
    print("Приходите снова!\n")
    exit()

def check_bank() -> int:
    while True:
        cash = int(input("Введите сумму опреации кратно 50\n"))
        if cash % 50 == 0:
            return cash

list_operation = []

while True:
    action = input("1 - снять деньги\n2 - пополнить\n3 - баланс\n4 - вывести историю операций\n5 - выйти\n")

    if action == '1':
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("списан налог на богатство: ", bank * percent_tax)
        cash = check_bank()
        if cash < bank:
            take_bank(cash)

            list_operation.append([str(date.today()), -1 * cash])
        else:
            print("Недостаточно средств\n")
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("списан налог на богатство: ", bank * percent_tax)
        print("Баланс = ", bank)
    elif action == '2':
        cash = check_bank()
        add_bank(cash)
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("списан налог на богатство: ", bank * percent_tax)
        print("Баланс = ", bank)

        list_operation.append([str(date.today()), cash])

    elif action == '3':
        print("Баланс = ", bank)
    elif action == '4':
        print(list_operation)
    else:
        exit_bank()
        
        
        
# ******************************************************************
#                 РЕШЕНИЕ, КОТОРОЕ БЫЛО В Д/З № 2
# ********************************************************************
# initial_balance = 0
# balance = initial_balance
# transaction_count = 0

# def calculate_withdrawal_fee(amount):
#     fee = amount * 0.015
#     return max(min(fee, 600), 30)

# def calculate_tax(amount):
#     tax = amount * 0.1
#     return tax

# while True:
#     print("Доступные действия:")
#     print("1. Пополнить")
#     print("2. Снять")
#     print("3. Выйти")
    
#     choice = input("Выберите действие: ")
    
#     if choice == "1":
#         deposit_amount = int(input("Введите сумму для пополнения (кратную 50): "))
#         if deposit_amount % 50 == 0:
#             balance += deposit_amount
#             transaction_count += 1
#             if transaction_count % 3 == 0:
#                 interest = balance * 0.03
#                 balance += interest
#             print("Баланс:", balance)
#         else:
#             print("Сумма пополнения должна быть кратна 50.")
    
#     elif choice == "2":
#         withdrawal_amount = int(input("Введите сумму для снятия (кратную 50): "))
#         if withdrawal_amount % 50 == 0:
#             if withdrawal_amount <= balance:
#                 if balance >= 5000000:
#                     tax = calculate_tax(balance)
#                     balance -= tax
#                 withdrawal_fee = calculate_withdrawal_fee(withdrawal_amount)
#                 balance -= (withdrawal_amount + withdrawal_fee)
#                 transaction_count += 1
#                 if transaction_count % 3 == 0:
#                     interest = balance * 0.03
#                     balance += interest
#                 print("Баланс:", balance)
#             else:
#                 print("Недостаточно средств на счете.")
#         else:
#             print("Сумма снятия должна быть кратна 50.")
    
#     elif choice == "3":
#         print("Выход из программы.")
#         break
    
#     else:
#         print("Неверный выбор. Попробуйте снова.")