# Nén tệp
import os
from zipfile import ZipFile

def get_all_file_paths(directory):
    file_paths = []
    
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    
    return file_paths

def compress_files(directory, output_filename):
    file_paths = get_all_file_paths(directory)
    
    with ZipFile(output_filename, 'w') as zip:
        for file in file_paths:
            zip.write(file)
    
    print(f"Tệp đã được nén thành công vào {output_filename}")

compress_files('thư_mục_của_bạn', 'output.zip')
