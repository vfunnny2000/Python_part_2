# Задание №7
 
# ✔Функция получает на вход словарь с названием компании в качестве ключа и списком
# с доходами и расходами (3-10 чисел) в качестве значения. 

# ✔Вычислите итоговую прибыль или убыток каждой компании. Если все компании прибыльные, верните истину, а если хотя бы одна убыточная — ложь.



def calculate_profit_loss(company_data):
    result = {}
    is_profitable = True

    for company, data in company_data.items():
        expenses = sum(data[:len(data)//2])
        earnings = sum(data[len(data)//2:])

        profit_loss = earnings - expenses
        result[company] = profit_loss

        if profit_loss < 0:
            is_profitable = False

    return result, is_profitable


company_data = {
    "Company A": [1000, 2000, 3000, 4000],
    "Company B": [5000, 6000, 7000, 8000],
    "Company C": [9000, 10000, 11000, 12000],
    "Company D": [13000, 14000, 15000, -16000]
}

result, is_profitable = calculate_profit_loss(company_data)

print("Results:")
for company, profit_loss in result.items():
    print(f"{company}: {profit_loss}")

print("All companies are profitable:", is_profitable)
