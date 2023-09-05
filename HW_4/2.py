# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.


def keyword_params(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if hashable(key):
            result[key] = value
        else:
            result[str(key)] = value
    return result

def hashable(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False
    
arguments = keyword_params(a=1, b='January', c=[1, 3, 5], d='' )
print(arguments)

# ************************************************************************

# def kwargs_to_dict(**kwargs):
#     result = {}
#     for key, value in kwargs.items():
#         try:
#             result[value] = key
#         except:
#             result[str(value)] = key
#     return result

# print(kwargs_to_dict(name='Nick', sername='Brown',
#                      months=['January', 'February', 'March'],
#                      courses={'python': 'ver 3.11', 'c#': 'ver 2.5'}))