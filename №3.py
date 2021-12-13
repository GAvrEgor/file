import os
import pathlib
from pathlib import Path
# total = os.listdir('total')

paths = []
names = []
path1 = Path('total', '1.txt')
name1 = os.path.basename(path1)
names.append(name1)
paths.append(path1)
path2 = Path('total', '2.txt')
name2 = os.path.basename(path2)
names.append(name2)
paths.append(path2)
path3 = Path('total', '3.txt')
name3 = os.path.basename(path3)
names.append(name3)
paths.append(path3)
def read (names):
    count = 0
    total = {}
    for i in paths:

        n = os.path.basename(i)
        with open(i, encoding='utf8') as f:
            line = 0
            for l in f:
                line += 1
        total[n] = line
            # print(f'{n} {line}')
        sort = sorted(total.items(),key=lambda x: x[1])
        a = dict(sort)
    for key, value in a.items():
        count += 1
        print(f'{key}\n {count}\n строка номер {line}')
read('name')
