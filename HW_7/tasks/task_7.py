# Задание №7 
# ✔Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п. 
# ✔Каждая группа включает файлы с несколькими расширениями. 
# ✔В исходной папке должны остаться только те файлы, которые не подошли для сортировки.



import os
import shutil

def sort_files_by_extension(folder_path):
    video_extensions = ['.mp4', '.avi', '.mov']
    image_extensions = ['.jpg', '.png', '.gif']
    text_extensions = ['.txt', '.docx', '.pdf']

    video_folder = os.path.join(folder_path, 'Видео')
    image_folder = os.path.join(folder_path, 'Изображения')
    text_folder = os.path.join(folder_path, 'Текст')

    os.makedirs(video_folder, exist_ok=True)
    os.makedirs(image_folder, exist_ok=True)
    os.makedirs(text_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            _, extension = os.path.splitext(filename)
            if extension.lower() in video_extensions:
                shutil.move(os.path.join(folder_path, filename), os.path.join(video_folder, filename))
            elif extension.lower() in image_extensions:
                shutil.move(os.path.join(folder_path, filename), os.path.join(image_folder, filename))
            elif extension.lower() in text_extensions:
                shutil.move(os.path.join(folder_path, filename), os.path.join(text_folder, filename))

folder_path = r"C:\Users\пк\Desktop\Погружение в Python (advanced)\HW_7\files"

# if __name__ == '__main__':
sort_files_by_extension(folder_path)