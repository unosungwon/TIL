## csv 파일 불러오기
```py
df = pd.read_csv('파일위치', index_col='인덱스로 쓰고 싶은 column')
```

## pandas.mean( ) / np.mean(numpy)

```py
# numpy
np.mean(scores)

# pandas
scores_df.mean()
```

## pandas.median( ) / np.median(numpy)

```py
# numpy
np.median(scores) 

# pandas
scores_df.median()
```

## pandas.mode( )
```py
scores_df.mode()
```

## deviation 편차
* `점수 - 평균`

```py
scores = np.array(df['english'])[:10] 

eng_dv = scores - np.mean(scores)
# array 형태로 나옴

scores_copy = scores_df.copy()
scores_copy['deviation'] = eng_dv
# scores_copy 테이블에 deviation 열이 추가.
```

## variance 분산
* np.var( )
* pandas.var(ddof=0)
* `(편차 ** 2) 의 평균`

```py
# numpy variance
np.var(scores)

# pandas variance
socres_df.var(ddof=0)
```

## standard deviation 표준편차
* `variance ** 0.5 (루트씌우기)`

```py
np.std( )
```

## IQR
* Inter Quartile Range
* `전체 자료의 50%`를 포함하는 범위

```py
scores_Q1 = np.percentile(scores, 25)
scores_Q3 = np.percentile(scores, 75)
scores_IQR = scroes_Q3 - scores_Q1
```


## pandas.describe( )

```py
df.describe()

#       english	mathematics
# count	50.00	50.000
# mean	58.38	78.880
# std	9.80	8.414
# min	37.00	57.000
# 25%	54.00	76.000
# 50%	57.50	80.000
# 75%	65.00	84.000
# max	79.00	94.000

```

## normalization




