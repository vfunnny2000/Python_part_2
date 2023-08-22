# Напишите программу банкомат. 
# ✔Начальная сумма равна нулю 
# ✔Допустимые действия: пополнить, снять, выйти 
# ✔Сумма пополнения и снятия кратны 50 у.е. 
# ✔Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е. 
# ✔После каждой третей операции пополнения или снятия начисляются проценты - 3% 
# ✔Нельзя снять больше, чем на счёте 
# ✔При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной 
# ✔Любое действие выводит сумму денег


initial_balance = 0
balance = initial_balance
transaction_count = 0

def calculate_withdrawal_fee(amount):
    fee = amount * 0.015
    return max(min(fee, 600), 30)

def calculate_tax(amount):
    tax = amount * 0.1
    return tax

while True:
    print("Доступные действия:")
    print("1. Пополнить")
    print("2. Снять")
    print("3. Выйти")
    
    choice = input("Выберите действие: ")
    
    if choice == "1":
        deposit_amount = int(input("Введите сумму для пополнения (кратную 50): "))
        if deposit_amount % 50 == 0:
            balance += deposit_amount
            transaction_count += 1
            if transaction_count % 3 == 0:
                interest = balance * 0.03
                balance += interest
            print("Баланс:", balance)
        else:
            print("Сумма пополнения должна быть кратна 50.")
    
    elif choice == "2":
        withdrawal_amount = int(input("Введите сумму для снятия (кратную 50): "))
        if withdrawal_amount % 50 == 0:
            if withdrawal_amount <= balance:
                if balance >= 5000000:
                    tax = calculate_tax(balance)
                    balance -= tax
                withdrawal_fee = calculate_withdrawal_fee(withdrawal_amount)
                balance -= (withdrawal_amount + withdrawal_fee)
                transaction_count += 1
                if transaction_count % 3 == 0:
                    interest = balance * 0.03
                    balance += interest
                print("Баланс:", balance)
            else:
                print("Недостаточно средств на счете.")
        else:
            print("Сумма снятия должна быть кратна 50.")
    
    elif choice == "3":
        print("Выход из программы.")
        break
    
    else:
        print("Неверный выбор. Попробуйте снова.")





