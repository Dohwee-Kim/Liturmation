*Software and cathedrals are much the same – first we build them, then we pray.  
소프트웨어 개발과 대성당의 공통점 - 일단 만들고 나서, 기도한다.*  
-___Sam Redwine___  
  
# Toy project : Liturmation
Liturgy-Automation for SADP   
보편지향기도 모아서 1,2,3,4 주제 classifier 만들기  

궁극적인 목표는 나를 대신해줄 보편지향기도 생성기 만들기!!!  


## 각 모듈 및 Directory 설명
* 각종 소스 파일 : /src
* data : /data

## Work flow
1. Making master data
2. Preprocessing
  - 형태소 분석 툴
3. Sentence or Word embeding (select one for each work iteration)
  - BOW
  - Word2Vec
  - BERT
4. Model development (select one for each work iteration)
  - Logistic regression
  - TF-IPF
  - CNN
  - RNN (LSTM)
  - Transformer
  - Other customized model
5. Evaluation and back to 1

## Install the environment
cuda 10.1 install if you want to use GPU  
```conda create -n py3 python==3.7.2```  
```conda install pytorch torchvision -c pytorch```  
```pip install scipy```  
```pip install sklearn```  
```conda install pandas```  
```conda install jupyter```  
```python -m ipykernel install --user --name py3 --display-name "py3"```
