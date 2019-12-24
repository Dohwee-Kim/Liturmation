import re
import json
import pandas as pd

def text_file_reader(file_path):

    src_file_name = file_path.split('/')[-1].strip('.txt')
    dst_file_name = src_file_name + "_CSV.csv"

    raw_read_result = []

    #Load files and remove lines
    with open(file_path, 'r', encoding='utf-8-sig') as src:
        for line in src:
            #Remove all new lines
            if not line.strip():
                continue
            raw_read_result.append(line.strip())
        src.close()

    for itr in raw_read_result:
        if not itr.strip():
            dict_pray = {}

        #if line starts with a label digit
        if itr[0].isdigit():
            dict_pray["label"] = itr[0]
            dict_pray["subject"] = itr[2:]
            #dict_pary["content"] = itr

        #if line starts with KOR character
        if re.match("^[ㄱ-ㅎ가-힣]+" , itr[0]) is not None:
            if not dict_pray:
                dict_pray["content"] = itr
        raw_read_result.append(dict_pray)

    print(raw_read_result)




def convert():
    pray_file_path = '../data/pray1.txt'
    result_dict = text_file_reader(pray_file_path)

    df = pd.DataFrame.from_dict(result_dict)
    csv_file_path = '../data/pray1.csv'
    df.to_csv(csv_file_path)


if __name__=="__main__":
    convert()