# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант.
# ✔*Верните все возможные варианты комплектации рюкзака.


backpack_capacity = int(input('Введите грузоподъемность рюкзака: '))

list_of_equipment = {'Еда': 5,
                     'Вода': 2,
                     'Палатка': 6,
                     'Мяч': 0.5,
                     'Шампуры': 1,
                     'Одежда': 5,
                     'Снасти': 2.5,
                     'Средства личной гигиены': 1,
                     'Топор': 3.5,
                     'Телевизор-)))': 25}


def sort_list(some_set: set):
    global global_list
    if len(some_set) == 1:
        return some_set
    else:
        for item in some_set:
            new_set = some_set.copy()
            new_set.remove(item)
            global_list.add(tuple(sort_list(new_set)))
    return some_set


list_of_equipment = dict(sorted(list_of_equipment.items(), key=lambda x: x[1]))
global_list = {tuple(list_of_equipment)}
sort_list(set(list_of_equipment))

print(f'Рюкзак грузоподъемностью {backpack_capacity} кг может вместить:')

for stack in global_list:
    summ_stack = 0
    for item in stack:
        summ_stack += list_of_equipment.get(item)
        if summ_stack > backpack_capacity:
            break
    else:
        print(*stack, 'весом', summ_stack, 'кг')
        
  
#   ------------ВАРИАНТ-------------------
 
# from itertools import combinations

# def find_backpack_contents(items, max_weight):
#     valid_combinations = []
#     for r in range(1, len(items) + 1):
#         for combination in combinations(items, r):
#             total_weight = sum(item[1] for item in combination)
#             if total_weight <= max_weight:
#                 valid_combinations.append(combination)
#     return valid_combinations


# backpack_items = {
#     'Тент': 3,
#     'Спальник': 2,
#     'Еда': 4,
#     'Вода': 5,
#     'Котелок': 1
# }
# max_backpack_weight =10

# result = find_backpack_contents(list(backpack_items.items()), max_backpack_weight)
# for combination in result:
#     print(combination)


