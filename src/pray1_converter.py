import pandas as pd
import numpy as np
import re
import json

## TODO: ../data/pray1.txt -> ../data/pray1_formated.csv

## Format: "{0:title}","{1:content}","{2:label}"
# title : "누구누구를 위하여" 처럼 기도 맨 처음에 나오는 부분
# content : 기도 본문
# label : 1혹은 2 혹은 3 혹은 4 - 기도주제 분류를 위한 label

## Ex)s
# 예시 > pray1 의 첫번째 기도
# "교회를 위하여 기도합시다.", "주님, 구원의 말씀을 전하는 교회가 주님의 말씀안에서 생활하며 많은 이들을 주님의 품으로 인도하게 하소서.", "1"
# 맨앞의 숫자 등 기타 특수기호 다 없어야 함.


def src2tmp1(src_file, dst_file):
    result_lines = []
    
    # 파일 로드 및 빈 라인 제거
    with open(src_file, 'r') as f_src:
        for line in f_src:
            if not line.strip(): ## 빈 라인 전부 제거
                continue
            result_lines.append(line.strip())
        f_src.close()

    ### pray 유닛 단위로 저장
    prays = []
    default_pray = {
        "title": None,
        "contents": "",
        "label": None,
    }
    pray = default_pray.copy()

    # 필요한 패턴 변수들
    kor_pattern = r"[ㄱ-ㅎ가-힣]+"
    num_pattern = r"\d"
    for_pattern = r"위하여"

    for line in result_lines:
        # print(line)
        if re.findall(num_pattern, line): ### title pattern 이 나온 경우
            ## Add and reset previous unit
            if pray['title'] is not None:
                print(pray)  # 확인
                prays.append(pray)
                pray = default_pray.copy()

            ## Start unit
            pray['title'] = line
        else:
            pray['contents'] += (" " + line.strip())
    prays.append(pray)
    
    ## Json 파일 저장
    with open(dst_file, 'w', encoding='utf-8') as fp:
        json.dump(prays, fp)

    ### 나머지는 다음 시간에....


def run():
    src_file = "../data/pray1.txt"
    tmp_file = "../data/pray1_tmp1.json"
    dst_file = "../data/pray1_formated.csv"

    src2tmp1(src_file, tmp_file)

if __name__ == "__main__":
    run()

