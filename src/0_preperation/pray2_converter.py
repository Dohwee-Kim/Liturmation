import re
import json


def text_file_reader(file_path):

    src_file_name = file_path.split('/')[-1].strip('.txt')
    dst_file_name = src_file_name + "_1.txt"

    raw_read_result = []

    #Load files and remove lines
    with open(file_path, 'r', encoding='utf-8-sig') as src:
        for line in src:
            #Remove all new lines
            if not line.strip():
                continue
            raw_read_result.append(line.strip())
        src.close()

    for i, itr in enumerate(raw_read_result):
        temporary_string_buffer = ''
        space_removed_result = []
        filter_value1 = '보편'

        #filter out 보편지향기도 lines
        if itr.startswith(filter_value1):
            continue

        if itr[0].isdigit():


            #if temporary_string_buffer != '':
            #    space_removed_result.append(temporary_string_buffer)
            #else:
            #    temporary_string_buffer = ''
            #    temporary_string_buffer += itr










def convert():

    pray_file_path = '../data/pray2.txt'
    text_file_reader(pray_file_path)



if __name__=="__main__":
    convert()