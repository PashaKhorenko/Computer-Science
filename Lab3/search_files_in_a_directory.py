#поиск файлов по каталогу

import os

def passage(file_name, folder):
    for element in os.scandir(folder):
        if element.is_file():
            if element.name == file_name:
                yield folder
        else:
            yield from passage(file_name, element.path)

print(*passage('game over 2.0.py', os.getcwd()))
