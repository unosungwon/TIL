# pandas

준비과정...

```py
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
```

# Array VS Series

* `Array(배열)`: 데이터 요소들의 집합을 저장하는 자료구조. 동일한 데이터 타입의 요소들로 구성. 메모리에 연속적으로 저장

* `Series` : pandas (주로 데이터 분석 및 조작을 위해 사용)라이브러리에서 제공하는 자료구조. `1차원 array 와 같아보이지만, index가 부여`됨. 인덱스 부여되어 있어서 `데이터에  라벨링과 접근이 가능`


# Series

### 기본틀
  * Series ( [values], index=[ index ] )

```py
s = Series(range(5), index = list('abcde'))
s

# a    0
# b    1
# c    2
# d    3
# e    4

date = ['sunday', 'monday', 'tuesday','wendnesday','thursday','friday','saturday']
day = Series(date, index=list('1234567'))
day

# 1        sunday
# 2        monday
# 3       tuesday
# 4    wendnesday
# 5      thursday
# 6        friday
# 7      saturday
```

### value 값 찾기 가능 (라벨링 가능)
  * series[index]

```py
day['1']
# 'sunday'

day[['1','2','3']]
# 1     sunday
# 2     monday
# 3    tuesday

day['1':'3']
# 1     sunday
# 2     monday
# 3    tuesday

'1' in day
# True
```

### series value 에 dictionary 도 넣을 수 있음.

```py
dict = {'a' : [1 , 10], 'b' : [2, 20], 'c' : [3, 30]}
s2 = Series(dict)
s2

# a    [1, 10]
# b    [2, 20]
# c    [3, 30]
```

### series index 에도 다른 dictionary 넣을 수 있음. 

```py
pollution = {'서울' : 130, '대전' : 100, '부산' : 125}
city = {'서울' : 130, '대전' : 100, '부산' : 125, '대구' : 100}

city_pollution = Series(pollution, index=city)
city_pollution

# 서울    130.0
# 대전    100.0
# 부산    125.0
# 대구      NaN

# => index dictionary의 key 값이 values dictionary의 value 개수보다 많아서 NAN 나옴.
```

### series 이름과 index 이름 짓기 가능

```py
city_pollution.name = '미세먼지'
city_pollution.index.name = '도시'
city_pollution

# 도시
# 서울    130.0
# 대전    100.0
# 부산    125.0
# 대구      NaN
# Name: 미세먼지, dtype: float64
```

### index 변경 가능
```py
city_pollution.index = list('가나다라')
city_pollution.index.name = '한글'
city_pollution

# 한글
# 가    130.0
# 나    100.0
# 다    125.0
# 라      NaN
```

# DataFrame 
* 표/스프레드시트. 여러칼럼 / 데이터 로우(레코드)

## 기본틀

> DataFrame(value,  columns=[ ], index=[ ])

```py
DataFrame(np.arange(20).reshape(4,5),
        columns=list('abcde'),
        index=np.arange(1,5))

# 	a	b	c	d	e
# 1	0	1	2	3	4
# 2	5	6	7	8	9
# 3	10	11	12	13	14
# 4	15	16	17	18	19

data = {
    'state' : ['Ohio', 'California', 'NewYork', 'NewYork', 'Boston'],
    'year' : [2000, 2001, 2002, 2002, 2003],
    'pop' : [1.5, 3.2, 4.0, 2.2, 2.9]
}

frame = DataFrame(data)
frame


#   state	year	pop
# 0	Ohio	2000	1.5
# 1	California	2001	3.2
# 2	NewYork	2002	4.0
# 3	NewYork	2002	2.2
# 4	Boston	2003	2.9
```

### column 변경 및 추가 가능

```py
# column 순서 변경
DataFrame(data, columns=['pop','state','year'])

# 	pop	state	year
# 0	1.5	Ohio	2000
# 1	3.2	California	2001
# 2	4.0	NewYork	2002
# 3	2.2	NewYork	2002
# 4	2.9	Boston	2003


# column 추가
DataFrame(data,
    columns=[x for x in data]+['dept'],
     index=['one', 'two', 'three', 'four', 'five'])

# 	    state	year	pop	dept
# one	Ohio	2000	1.5	NaN
# two	California	2001  3.2 NaN
# three	NewYork	2002	4.0	NaN
# four	NewYork	2002	2.2	NaN
# five	Boston	2003	2.9	NaN
```

### Series 와 마찬가지로 인덱싱 가능.
* Series[index] = value
* DataFrame[column] = value (series 형태로 나옴.)
* DataFrame.iloc[integar index] = value
* DataFrame.loc[labeling index] = value

```py
frame2['state']
frame2.state

# one         Ohio
# two      NewYork
# three    NewYork
# four     NewYork
# five      Boston


frame.iloc[2]
frame.loc['three']

# state    NewYork
# year        2002
# pop          4.0
# dept         NaN
```

### row value 변경, column 추가 및 column value 추가 및 변경 가능

```py
#column 추가 column value도 같이 추가
frame2['dept'] = np.arange(5)
frame2

# 	    state	year	pop	dept
# one	Ohio	2000	1.5	0
# two	California	2001	3.2	1
# three	NewYork	2002	4.0	2
# four	NewYork	2002	2.2	3
# five	Boston	2003	2.9	4


# row value 변경
frame2.loc['two'] = ['NewYork', 2003, 3.3, 4]

#       state	year	pop	dept
# one	Ohio	2000	1.5	0
# two	NewYork	2003	3.3	4
# three	NewYork	2002	4.0	2
# four	NewYork	2002	2.2	3
# five	Boston	2003	2.9	4
```
### column index 전치 가능
* DataFrame.T
```py
df1= DataFrame(np.arange(12).reshape(3,4), columns=list('abcd'), index=list('가나다'))
df.T

# 	가	나	다
# a	0	4	8
# b	1	5	9
# c	2	6	10
# d	3	7	11
```

### dictionary 중첩 가능
```py
* Series({i1 : v1, i2 : v2, i3 : v3})
* DataFrame({col1 : v1, col2 : v2, col3 : v3})
* DataFrame({col1 : {i1 : v1, i2 : v2}},
            {col2 : {i1 : v3, i2 : v4}},
            {col3 : {i1 : v5, i2 : v6}})
```
```py
pop ={
    'seoul' : {2001 : 2.4, 2001 : 5.5, 2003 : 4.4},
    'daejeon' : {2000 : 4.4, 2001 : 6.6, 2003 : 3.5},
    'daegu' : {2000 : 5.5, 2001 : 6.0, 2003: 2.9},
    'busan' : {2001: 2.9, 2003 : 8.8}
}

frame3 = DataFrame(pop)
frame3


#       seoul	daejeon	daegu	busan
# 2001	5.5	    6.6	    6.0	    2.9
# 2003	4.4	    3.5	    2.9	    8.8
# 2000	NaN	    4.4	    5.5	    NaN


DataFrame(pop, index = [2000, 2001, 2003, 2002])
# 	    seoul	daejeon	daegu	busan
# 2000	NaN	    4.4	    5.5	    NaN
# 2001	5.5	    6.6	    6.0	    2.9
# 2003	4.4	    3.5	    2.9	    8.8
# 2002	NaN	    NaN	    NaN	    NaN
```

### values, index 값을 array로 반환
* Series.values => array로 반환
* DataFrame.values => n차원 arrat로 반환
```py
frame3.values

# array([[5.5, 6.6, 6. , 2.9],
#        [4.4, 3.5, 2.9, 8.8],
#        [nan, 4.4, 5.5, nan]])

frame3.index

# Index([2001, 2003, 2000], dtype='int64', name='year')
```

# Index
- pandas 에서 쓰는 index 자료형
- .index[ ]는 변경이 안됨.

## Series

### series.index[ ]
* `파이썬 인덱스와는 다름`. 
* Python; [a : b] 일 경우 b-1 인덱스까지만 출력
* Series; `[a : b]` 일 경우 `b 까지 다 출력`

```py
obj = pd.Series(range(3), index=list('abc'))

# a    0
# b    1
# c    2

obj['a']
# value 출력 0

obj.index[0]
# index 출력 'a'

obj.index[1:]
# Index(['b', 'c'], dtype='object')
# index 자료형

```
