import os
import json
import csv
import pickle

def process_directory(directory, output_directory):
    result = []
    total_size = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            total_size += file_size
            result.append({
                'path': file_path,
                'type': 'file',
                'size': file_size,
                'parent_directory': root
            })

        for dir in dirs:
            dir_path = os.path.join(root, dir)
            dir_size = get_directory_size(dir_path)
            total_size += dir_size
            result.append({
                'path': dir_path,
                'type': 'directory',
                'size': dir_size,
                'parent_directory': root
            })

    json_file_path = os.path.join(output_directory, 'result.json')
    with open(json_file_path, 'w') as json_file:
        json.dump(result, json_file)

    csv_file_path = os.path.join(output_directory, 'result.csv')
    with open(csv_file_path, 'w', newline='') as csv_file:
        fieldnames = ['path', 'type', 'size', 'parent_directory']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(result)

    pickle_file_path = os.path.join(output_directory, 'result.pickle')
    with open(pickle_file_path, 'wb') as pickle_file:
        pickle.dump(result, pickle_file)

    return total_size

def get_directory_size(directory):
    total_size = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)

    return total_size

directory = r'C:\Users\пк\Desktop\Погружение в Python (advanced)\HW_8'
output_directory = r'C:\Users\пк\Desktop\Погружение в Python (advanced)\HW_8'
total_size = process_directory(directory, output_directory)
print(f'Total size: {total_size} bytes')





