import pandas as pd
import numpy as np
import re
import json
import operator

import scipy.sparse as sps
from collections import defaultdict
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

def convert_token_to_idx(token_ls, token_to_index):
    for tokens in token_ls:
        yield [token_to_index[token] for token in tokens]
    return

def file_reader(file_path):
    text_list = []
    label_list = []

    with open(file_path) as f:
        for i, line in enumerate (f.readlines()[0:]):
            txt, label = line.split('\t')
            text_list.append(txt)
            label_list.append(int(label.replace('\n','')))
    return text_list, label_list


def kidoh_classifier():
    training_set = "../data/pray_test_tab_separated.txt"
    #TODO : Please add test set later
    test_set = ""


    # Load training set
    x_train, y_train = file_reader(training_set)
    print(x_train)
    print(y_train)
    x_test, y_test = ['교회를 위하여 기도합시다. 주님, 교회가 성서안에서 말씀하시는 주님의 음성을 올바로 알아듣고 주님과 이웃을 사랑하는 일에 더욱 충실하고 어두운 곳에 빛과 소금이 될수 있는 교회되게 하소서.'],['1']
    print("Training set loaded ... ")

    #띄어쓰기로 구분
    x_train = [x.split() for x in x_train]
    x_test = [x.split() for x in x_test]

    # 단어마다 고유한 인덱스를 부여하기 위한 dictionary
    token_to_index = defaultdict(lambda: len(token_to_index))

    x_train = list(convert_token_to_idx(x_train, token_to_index))
    x_test = list(convert_token_to_idx(x_test, token_to_index))

    for k,v in sorted(token_to_index.items(), key=operator.itemgetter(1))[:15]:
        print(k, v)

    n_train_reviews = len(x_train)  # 학습용 리뷰의 총 수
    n_test_reviews = len(x_test)
    n_unique_word = len(token_to_index)  # 고유 단어의 갯수 (BOW의 차원의 크기)

    print("Printing out unique word size in kidohmoon")
    print(n_unique_word)

    # 학습용 리뷰 수(150,000) x 고유 단어의 수(450,541)의 크기를 갖는 빈 단어가방 생성
    bow_train = sps.lil_matrix((n_train_reviews, n_unique_word), dtype=np.int8)
    bow_test = sps.lil_matrix((n_test_reviews, n_unique_word), dtype=np.int8)

    for i, tokens in enumerate(x_train):
        for token in tokens:
            # i번 째 리뷰에 등장한 단어들을 세서, 고유 번호에 1씩 더해준다.
            bow_train[i, token] += 1

    for i, tokens in enumerate(x_test):
        for token in tokens:
            # i번 째 리뷰에 등장한 단어들을 세서, 고유 번호에 1씩 더해준다.
            bow_test[i, token] += 1

    model = LogisticRegression()
    model.fit(bow_train, y_train)


    predict = model.predict(bow_test)
    print(predict)


if __name__ == "__main__":
    kidoh_classifier()