#Giải nén tệp
from zipfile import ZipFile

def decompress_file(zip_filename, output_directory):
    with ZipFile(zip_filename, 'r') as zip:
        zip.extractall(output_directory)
    
    print(f"Tệp đã được giải nén thành công vào {output_directory}")

decompress_file('output.zip', 'thư_mục_đích')
