'''
pray4_old.txt를 pray4_new.txt로 변환
'''

import re

def run(src_filepath, dst_filepath):
    with open(src_filepath, 'r', encoding='utf-8') as f:
        full_text = f.read()

    full_text = full_text.replace("\n", ' ')
    full_text = re.sub('기도합시다 ', '기도합시다. ', full_text)
    full_text = re.sub('소서 ', '소서. ', full_text)

    full_text = re.sub(" \d{1,2}\.^\d", '\n\g<0>', full_text)
    full_text = re.sub('기도합시다\. ', '기도합시다.\n', full_text)
    full_text = re.sub('소 서', '소서', full_text)
    full_text = re.sub('소서\. ', '\g<0>\n', full_text)
    full_text = re.sub(" \n", '\n', full_text)
    full_text = re.sub("\n ", '\n', full_text)
    print(full_text)
    prays = re.findall(r'\d{1,2}\..*기도합시다\.\n.*소서\.', full_text)

    new_text = ''
    for pray in prays:
        new_text += pray + "\n\n"

    with open(dst_filepath, 'w', encoding='utf-8') as f:
        f.write(new_text)

if __name__ == "__main__":

    src_filepath = '../../data/pray4_old.txt'
    dst_filepath = '../../data/pray4_new.txt'
    run(src_filepath, dst_filepath)

    src_filepath = '../../data/pray5_old.txt'
    dst_filepath = '../../data/pray5_new.txt'
    run(src_filepath, dst_filepath)

    src_filepath = '../../data/pray6_old.txt'
    dst_filepath = '../../data/pray6_new.txt'
    run(src_filepath, dst_filepath)