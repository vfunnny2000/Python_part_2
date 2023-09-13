# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


import os

def split_file_path(file_path):
    path, filename = os.path.split(file_path)
    filename, extension = os.path.splitext(filename)
    return path, filename, extension

file_path = "C:/Users/Python/Python_2/HomeWork_5/1.py"
path, filename, extension = split_file_path(file_path)
print("Path:", path)
print("Filename:", filename)
print("Extension:", extension)



# file_path = "/home/user/files/document.txt"
# result = split_file_path(file_path)
# print(result)