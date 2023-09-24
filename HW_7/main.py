from tasks.group_rename import group_rename_files
from tasks.task_7 import sort_files_by_extension

if __name__ == '__main__':
    group_rename_files("new_file_test", 3, ".txt", "doc", [3, 6])
    sort_files_by_extension(r"C:\Users\пк\Desktop\Погружение в Python (advanced)\HW_7\files")
 