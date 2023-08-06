"""BfG Cardplay utilities."""
import os

BASE_DIR = '/home/jeff/.virtualenvs/cprig/lib/python3.9/site-packages/bfgcardplay/source'

FILE = 'fourth_seat_defender.py'

with open(os.path.join(BASE_DIR, FILE), 'r') as f_python:
    text = f_python.read()
    data = text.split('\n')
    new_data = []
    for index, line in enumerate(data):
        if line.strip().startswith('log'):
            pos_start = line.find("f'{")
            pos_end = line.find("}'")
            new_check_text = line[pos_start+3: pos_end]
            pos_start = data[index+1].find("return")
            if pos_start:
                old_check_text = data[index+1][pos_start+7:]
                if new_check_text == old_check_text:
                    data[index+1] = data[index+1].replace('return', '# return')
                else:
                    print(f'mismatch at {index+1} {old_check_text} {new_check_text}')
            line = line.replace('log', 'return log')
            line = line.replace("f'{", '')
            line = line.replace("}'", '')
        # if line.strip().startswith('return') and new_data[index-1].strip().startswith('return'):
        #     line = line.replace('return', '# return')
        new_data.append(line)
new_text = '\n'.join(new_data)


with open(os.path.join(BASE_DIR, 'xxx.py'), 'w') as f_python:
    f_python.write(new_text)
print(f'original {len(data)} lines')
print(f'processed {len(new_data)} lines')
