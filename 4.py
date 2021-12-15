import os
from os import path
import pathlib
from pathlib import Path
from contextlib import redirect_stdout

def read (name, path):
    with open(path, encoding='utf8') as file:
        name = os.path.basename(name)
        name_split = os.path.splitext(name)[0]
        lines = 0
        # print(f'{name}')
        for line in file:
            lines += 1
            print(f'строка номер {lines} файла {name_split}')
        # all_lines.append(lines)
        # print(all_lines)
# read('1.txt', Path('total', '1.txt'))


path1 = Path('total', '1.txt')
path2 = Path('total', '2.txt')
path3 = Path('total', '3.txt')

count_line={}
with open(path1, encoding='utf8') as file_1:
    file_line = 0
    for l1 in file_1:
        file_line += 1
    count_line[os.path.basename(path1)] = file_line
with open(path2, encoding='utf8') as file_2:
    file_line = 0
    for l1 in file_2:
        file_line += 1
    count_line[os.path.basename(path2)] = file_line
with open(path3, encoding='utf8') as file_3:
    file_line = 0
    for l1 in file_3:
        file_line += 1
    count_line[os.path.basename(path3)] = file_line
sorted_count_line = sorted(count_line.items(), key=lambda x: x[1])
# print(dict(sorted_count_line))
d_sorted = dict(sorted_count_line)
def write():
    for key, value in d_sorted.items():
        if key == '1.txt':
            print(f'{key}\n {value}')
            read('1.txt', Path('total', '1.txt'))
        elif key == '2.txt':
            print(f'{key}\n {value}')
            read('2.txt', Path('total', '2.txt'))
        elif key == '3.txt':
            print(f'{key}\n {value}')
            read('3.txt', Path('total', '3.txt'))

with open('4.txt', 'w') as file_4:
    with redirect_stdout(file_4):
        write()
