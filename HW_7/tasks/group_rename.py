import os

def group_rename_files(final_name, digit_count, source_extension, final_extension, name_range):
    directory = r"C:\Users\пк\Desktop\Погружение в Python (advanced)\HW_7\files"
    files = os.listdir(directory)
    filtered_files = [file for file in files if file.endswith(source_extension)]

    counter = 0

 
    for file in filtered_files:
        counter_str = str(counter).zfill(digit_count)
        name_part = file[name_range[0]-1 : name_range[1]]

        new_name = ""
        if final_name:
            new_name = final_name

        new_name += name_part + "_" + counter_str + final_extension

        source_file_path = os.path.join(directory, file)
        dest_file_path = os.path.join(directory, new_name)
        os.rename(source_file_path, dest_file_path)
        counter += 1

if __name__ == '__main__':
    group_rename_files("new_file_test", 3, ".txt", "doc", [3, 6])





