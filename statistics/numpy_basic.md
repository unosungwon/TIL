# numpy ?
- `n차원 배열`을 쉽게 `처리`할 수 있도록 지원하는 `파이썬의 라이브러리`
- 실행속도가 빨라서 사용.


## 배열 ?

- `배열 특징`
1. 시작할 때 `사이즈가 고정`이다.
   -  ex> 식당에서 4인석 자리 옆에 다른 사람들이 앉아있음. 
  
   -  지인이 나중에 와도 옆에 앉은 사람들을 쫓아내고 내 지인을 앉힐 수 없음. 

   - 그래서 자리를 먼저 많이 잡아놓고, 그 자리에 앉는 것임. 

2. 서로 `옆 주소`에 `존재`한다. (물리적으로)

3. 기본적으로 `자료형이 고정`되어있다. 
    - 숫자형이면, 숫자형만. 문자열이면 문자열만. 

    - 정수만, 실수만. 

----

- `리스트 특징`
1. 사이즈가 `가변`이다. 
    - (.append( ), .pop( )으로 배열이 늘어나거나 줄어들 수 있음. )
  
2. 요소간 위치가 무작위다.


# pandas
= 데이터 프레임. (일종의.. 데이터 스프레드)
- 데이터 테이블과 시계열 데이터를 조작하고 운영하기 위애 처리가 가능하게 하는 것.

```py
import pandas as pd

df = pd.read_csv(파일위치/ 파일이름)
```

* pandas DF => numpy Array => Pandas DF

```py
# pandas DF 불러오기
df = pd.read_csv()

# df 을 numpy Array로 가져오기
a = np.array(df['column명'])[:10]

# Array 로 가져온 것을 다시 pandas DF 로 불러와서 테이블로 보기
pd.DataFrame({'array 값들의 column명 정해줌': a}, index = pd.Index([a값 개수 만큼 인덱스 이름 지정], name='index column 명 정해줌'))
```

## df.loc 
=> labeling 된 index 라고 생각.

## df.iloc

> => 위치(`where==index`)라고 생각

```py
# Rows

print(df.iloc[0], type(df.iloc[0])) # => Series

# english        42
# mathematics    65
# Name: 1, dtype: int64 <class 'pandas.core.series.Series'>

print(df.iloc[:5], type(df.iloc[:5]))  # => DataFrame

print(df.iloc[1])

print(df.iloc[2])
```

```py
# columns

print(df.iloc[:,0], type(df.iloc[:,0]))

# student number
# 1     42
# 2     69
# 3     56
# 4     41
# 5     57
# 6     48
# 7     65
# 8     49
# 9     65
# 10    58
# Name: english, dtype: int64 <class 'pandas.core.series.Series'>

print(df.iloc[:,1])

print(df.iloc[:,-1])

print(df.iloc[:, :2], type(df.iloc[:, :2]))

#                 english  mathematics
# student number                      
# 1                    42           65
# 2                    69           80
# 3                    56           63
# 4                    41           63
# 5                    57           76
# 6                    48           60
# 7                    65           81
# 8                    49           66
# 9                    65           78
# 10                   58           82 <class 'pandas.core.frame.DataFrame'>

print(df.iloc[[0,1],[0,1]])

#                 english  mathematics
# student number                      
# 1                    42           65
# 2                    69           80
```

```py
df.loc[df['mathematics']==80, ['english']]

#                 english
# student number         
# 2                    69
```

## np.array( )

```py
arr1 = np.array([[1,2,3 ],[4,5,6 ],[7,8,9 ]])
arr1
# [[1,2,3]
# [4,5,6]
# [7,8,9]]

arr.dtype
# dtype('int32')

arr.shape
# (3,3)

arr.type
# numpy.ndarray


data = np.random.randn(5,5) #(row, column)


l = [1, 2, 3, 4]
arr1 = np.array(l)
# => array([1,2,3,4])
```

## np.arange( )

```py
np.arange(5)
# array([0, 1, 2, 3, 4])
```

## np.zeros, ones( )

```py
np.zeros(5)
# array([0,0,0,0,0])

np.zeros((3,2,4))
#array([[[0,0,0,0],
#       [0,0,0,0]],

#       [[0,0,0,0],
#       [0,0,0,0]],

#       [[0,0,0,0],
#       [0,0,0,0]]])

```
## np.ones_like( )
```py
arr = np.array([[1,2,3],[4,5,6]])
np.ones_like(arr)
# array([1,1,1][1,1,1])

arr = np.arange(5)
np.ones_like(arr)
# array([1,1,1,1,1])
```


## np.astype( )
```py
arr = np.array([1,2,3,4,5])
np.astype(np.float64)
# array([1. , 2., 3. ,4. ,5.])

data = np.random.randn(2,3)
np.astype(int)
```

## 산술연산

## index / slicing

```py
arr = np.arange(10)
# array([0,1,2,3,4,5,6,7,8,9])

arr[5]
# 5

arr[5:8]
# array([5,6,7])

arr[5:8] = 100
arr
# array([0,1,2,3,4,100,100,100,8,9])
```

```py
# numpy에서만 가능

arr = np.array([[1,2,3],[4,5,6]])
arr[0][1]
# 2

arr[0, 1]
# 2
```

## Boolean

```py

```

## 배열전치

```py
arr = np.arange(20).reshape(4,5)
# array([[0,1,2,3,4],
#       [5,6,7,8,9],
#       [10,11,12,13,14],
#       [15,16,17,18,19]])

ARR = arr.T
# array([[0,1,2,3],
#       [4,5,6,7],
#       [8,9,10,11],
#       [12,13,14,15],
#       [16,17,18,19]])

```

## 수학 메소드/ 통계 메소드

```py
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

arr.sum()
# 45

arr.mean()
# 5.0

arr.sum(0)  # 각 열의 합
# array([12, 15,18])

arr.sum(1)  # 각 행의 합
# array([6, 15, 24])
```