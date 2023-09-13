# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, 
# ставка int, премия str с указанием процентов вида «10.25%». В результате получаем словарь с именем в качестве 
# ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии 


names = ['Ivanov', 'Sidorov', "Petrov"]
salaries = [15000, 20000, 25000]
awards = ['10.0%', '7.25%', '5%']
# print(f'исходные данные:\n{names}\n{salaries}\n{awards}')
print({name: salary * float(award[:-1]) / 100 for name, salary, award in zip(names, salaries, awards)})


# ****************************************************************
# from pprint import pprint

# name_employee = ('Sidorov', 'Ivanov', 'Petrov')
# salary = (1000, 150, 50)
# bonus = ('2.5%', '1.5%', '5%')

# bonus = {name_employee[i]: salary[i] + salary[i] * (float(bonus[i][:-1]) / 100) for i in range(len(name_employee))}

# pprint(bonus)

# **********************************************************************

names = ['Sidorov', 'Ivanov', 'Petrov']
rates = [1000, 2000, 1500]
bonuses = ['10.25%', '5%', '12.5%']

result = {name: rate * float(bonus.strip('%')) / 100 for name, rate, bonus in zip(names, rates, bonuses)}
print(result)

