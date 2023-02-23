# 문제 03. 동명이인 찾기

## 문제
- n명의 사람 이름 중에서 같은 이름을 찾아 집합으로 만들어 돌려주는 알고리즘을 만들어 보라.

## 입력
- n명의 사람 이름

## 출력
- n개의 이름 중 중복되는 이름들만 담은 집합
- ex) `["Tom", "Jerry", "Mike", "Tom"]` 을 입력하면, `{"Tom"}`을 출력.


## 풀이 1(answer1.py)
- 이중 반복문을 사용하여, i번째 이름과 그 뒤에 있는 이름들을 하나씩 하나씩 전수 비교한다.
- 이때, 맨 마지막 이름은 이미 앞의 이름들과 모두 비교를 했고, 그 뒤에는 더 이상 비교할 이름이 없으므로, 첫 번째 반복문이 맨 마지막 index에 해당하는 값에는 도달하지 않도록 한다.