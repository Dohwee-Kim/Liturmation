import re
import json
import pandas as pd


def text_file_reader(file_path):
    raw_read_result = []
    list_of_dict_converted_result = []

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
            continue

        #if line starts with a label digit
        if itr[0].isdigit():
            dict_pray = {}
            dict_pray["label"] = itr[0]
            dict_pray["subject"] = itr[2:]
            #dict_pary["content"] = itr

        #if line starts with KOR character
        if re.match("^[ㄱ-ㅎ가-힣]+" , itr[0]) is not None:
            if dict_pray:
                dict_pray["content"] = itr
                list_of_dict_converted_result.append(dict_pray)

    return list_of_dict_converted_result


def convert():
    # pray_file_path = '../data/pray1.txt'
    # result_dict = text_file_reader(pray_file_path)

    pray4 = text_file_reader('../data/pray4_v2.txt')
    pray5 = text_file_reader('../data/pray5_v3.txt')
    pray6 = text_file_reader('../data/pray6_v2.txt')

    pray_master = pray4 + pray5 + pray6
    df = pd.DataFrame.from_dict(pray_master)
    csv_file_path = '../data/pray456_v3.csv'
    df[['label', 'subject', 'content']].to_csv(csv_file_path, index=False)


if __name__=="__main__":
    convert()