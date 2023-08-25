# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [1, 2, 1, 2, 3, 4, 4, 5, 5, 55, 108]

def remove_duplicates(lst):
    return list(set(lst))
result = remove_duplicates(my_list)
print(result)


# ----ВАРИАНТ-------------

# def find_duplicates(lst):
#     return list(set([x for x in lst if lst.count(x) > 1]))

# lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# print(find_duplicates(lst))