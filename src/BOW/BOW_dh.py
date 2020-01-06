import pandas as pd
import numpy as np
import re
import json
import operator
import sklearn

import scipy.sparse as sps
from collections import defaultdict
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

def convert_token_to_idx(token_ls, token_to_index):
    for tokens in token_ls:
        yield [token_to_index[token] for token in tokens]
    return

def file_reader_label_and_content_only(file_path):
    df = pd.read_csv(file_path)

    pd_series_content=df['content']
    pd_series_label = df['label']

    x_train, x_test, y_train, y_test = train_test_split(pd_series_content, pd_series_label, test_size=0.2, random_state=42)
    """
    with open(file_path) as f:
        for i, line in enumerate (f.readlines()):
            if i ==0:
                continue
            else:
                label, _, content = line.split(',')
                label_list.append(int(label.replace('\n','')))
                content_list.append(content)
    """

    return x_train, x_test, y_train, y_test


def kidoh_classifier():
    training_set = "../../data/pray1.csv"
    test_set = ""

    # Load training set
    x_train, x_test, y_train, y_test = file_reader_label_and_content_only(training_set)
    print("1st data sampling ...")
    print(x_train[0])
    print(y_train[0])

    print("length of Train : " , len(x_train))
    print("length of Test : " , len(x_test))
    print("Training set loaded ... ")

    #띄어쓰기로 구분
    x_train = [x.split() for x in x_train]
    x_test = [x.split() for x in x_test]

    # 단어마다 고유한 인덱스를 부여하기 위한 dictionary
    token_to_index = defaultdict(lambda: len(token_to_index))

    x_train = list(convert_token_to_idx(x_train, token_to_index))
    x_test = list(convert_token_to_idx(x_test, token_to_index))

    print("indexing result check ... ")
    for k,v in sorted(token_to_index.items(), key=operator.itemgetter(1))[:25]:
        print(k, v)

    n_train_reviews = len(x_train)  # 학습용 리뷰의 총 수
    n_test_reviews = len(x_test)
    n_unique_word = len(token_to_index)  # 고유 단어의 갯수 (BOW의 차원의 크기)

    print("Printing out unique word size in kidohmoon")
    print(n_unique_word)

    # 학습용 리뷰 수 x 고유 단어의 수의 크기를 갖는 빈 단어가방 생성
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
    accuracy = accuracy_score(y_test, predict)

    print('Accuracy : ' , accuracy)
    print(classification_report(y_test, predict))
    #print(classification_report(y_train, predict))
    print(predict)


if __name__ == "__main__":
    kidoh_classifier()