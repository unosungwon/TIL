# 01_data_container

>
>   1. container = data structure
>       - Sequence (=나열된) 형 container
>           - list(), tuple(), range(), string(), binary()
> 
>       - Non-Sequence container
>           - set()
>
>
>

## 1. Container (=data sstructure)
- `container` ? `여러 개의 값 저장`할 수 있는 것. 
- Sequence = ordered
- Non-Sequence = unordered

## 1.1. Sequence Container
- 데이터가 `순서대로 나열` 되어있다. 
 
    =/= 데이터가 정렬 되어있다.
- ordered = `index` 가 있다. = `특정 위치의 데이터 가리킬 수 있다.` 

## 1.1.1. list
- list 만들기
```PYTHON
# 1. 
my_list = [value1, value2, value3]
print(my_list)

# 2. 
another_list = list(another_list)
```
----

- list 특정 값 가리키기 = index
```PYTHON
# 원소를 포함한 list를 만들어 봅시다.
# 변수명이 location인 list에 지역 5곳을 원소로 포함해 만들어 봅시다.
# 변수 locations과 타입을 출력해 봅시다.
# location의 첫번째 값과 마지막 값을 인덱스로 접근해 봅시다.

locations = ['서울', '부산', '강릉', '포항', '여수']
print(locations, type(locations)) 
#-> ['서울', '부산', '강릉', '포항', '여수']  <class 'list'>

locations[0] , locations[4] 
# -> ('서울', '여수') <class 'tuple'>
```
```PYTHON
# `생각해볼만 한 것`
locations[0] #-> '서울'
print(locations[0], locations[4]) # -> 서울여수
```

## 1.1.2. tuple
- tuple 활용법
```PYTHON
(value1, value2)
```
---

- tuple은 직접 사용 보단, `파이썬 내부에서 사용`

```PYTHON
# 변수명이 my_tuple인 tuple을 만들어 봅시다. 
# 단, 무작위 정수 2개를 포함하여 만듭니다.
# my_tuple의 타입을 출력해 봅시다.

my_tuple = (2, 3)
print(my_tuple, type(my_tuple))
# -> (2, 3) <class 'tuple>
```

```PYTHON
# 변수 하나에 여러 값을 넣으면, 파이썬이 알아서 tuple로 처리함.

a = 1
print(a, type(a)) # -> 1 <class 'int'>

b = 1, 2, 3
print(b,type(b)) # -> (1, 2, 3) <class 'tuple'>
```

```PYTHON
# 실제로는 파이썬에서 tuple로 처리되고 있었음.
# 1. 
x, y = 1, 2  => (x, y) = (1, 2)
print(x)
print(y)

# 2.
x, y = y, x  => (x, y) = (y, x)
print(x)
print(y)
```

```PYTHON
# 변수명이 empty인 빈 tuple을 만들어 봅시다.

empty = ()
print(empty)  # -> ()

# 변수명이 single_tuple인 하나의 요소(값)로 구성된 tuple을 만들어 봅시다. (길이가 1)

single_tuple = (1, )
print(single_tuple)  # -> (1,)
```
---

## 1.1.3. range
- `숫자의 Sequence` 를 나타내기 위해 사용
- `연속된 정수만` 보여줌

```PYTHON
# 0부터 9까지 값을 가지는 range를 만들고 list로 형 변환을 해 봅시다.

list(range(10))  # -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```PYTHON
# 생각해볼것
1.  list(range(10))
2.  print(list(range(10)))
3.  a = list(range(10))
    print(a)

# 셋 다 나오는 값 모양이 똑같음
```

- `range(start, end, step)`
```PYTHON
# 1.
# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

range(0,-10,-1)

#  [3, 5, 7, 9]
range(3,10,2)
```

### 시퀀스에서 사용할 수 있는 연산자/ 함수

|operation|설명|
|---------|---|
|x `in` s	|containment test|
|x `not in` s|containment test|
|s1 `+` s2|concatenation|
|s `*` n|n번만큼 반복하여 더하기
|`s[i]`|indexing|
|`s[i:j]`|slicing|
|`s[i:j:k`]|k간격으로 slicing|
|len(s)|길이|
|min(s)|최솟값|
|max(s)|최댓값|
|s.count(x)|x의 개수|

- `STR`은 `컨테이너` 이면서 `시퀀스` 이다.
```PYTHON
my_string = 'string', 'a'
'a' in my_string  # -> True
```

- `시퀀스`는 str과 같이 + 로 `concantenation 가능`
```PYTHON
# 문자열 '안녕'과 문자열 '하세요'를 더하고 결과를 출력해 봅시다.

'안녕' + '하세요'   # -> '안녕하세요'
print('안녕' + '하세요')  # -> 안녕하세요


# 정수 1과 2를 포함한 tuple과 정수 5와 6을 포함한 tuple을 더하고 결과를 출력해봅시다.
(1, 2) + (5, 6)   # -> (1, 2, 3, 4, 5)


# 리스트도 가능

['안녕'] + ['하세요']  
# -> ['안녕', '하세요']
# 리스트 값끼리 concant 한거니까 값은 리스트로 나온다.

['안녕'] , ['하세요']
# -> (['안녕'] , ['하세요'])
# 리스트가 나열된 것이니까 tuple로 묶임.
```

- `*` 으로 list 안의 값들 `반복 가능`.
```PYTHON
# [0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10]

a = [0, 10]
a * 6 

# 혹은 [] * 6 도 가능.
[0, 10] * 6
```

- `index` 
```PYTHON
# 변수명은 locations, 원소는 무작위 지역 5곳을 문자열로 작성합니다.
# locations의 첫번째 원소에 index로 접근해 봅시다.

locations = ['서울', '경기도', '부산', '전주', '포항']
locations[0]  # -> '서울'

print(location[0])  # -> 서울
```

- `slicing` - 1
```PYTHON
# 두번째, 세번째 값만 가져와봅시다.
# slicing을 사용합니다.

locations[1:3]   # -> '경기도', '부산'
```

-`slicing` -  2
```PYTHON
# list[start: end: step]
# 0부터 30까지 3씩 증가하는 값을 가지는 새로운 list를 만들어 봅시다.
# 새롭게 생성한 list를 출력해 봅시다.

nums = list(range(0, 31))
# -> [0, 1, 2, 3, ..., 30]

new_nums = nums[0:31:3]
new_nums  
# -> [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
```

- len, min, max, .count
```PYTHON
len(new_nums) # -> 11
min(new_nums), max(new_nums)  # -> (0, 30)


sample = ['봄', '여름', '가을', '겨울']
sample.count('봄') 
# -> 1
```

## 1.2. Non- Sequence Container
- 시퀀스가 아닌 컨테이너는 index 접근 안된다!!! 

### 1.2.1. set
- 순서가 없는 집합.
- 보따리 같은 느낌이라고 생각.
- 정렬 안되어있음
- `결과값이 정렬된것 처럼 보이는 거지, 실제로 파이썬에서는 정렬 안된것임.` 
- 중복된 값 없음. 


```PYTHON
s = {value1, value2, value3}
```

```PY
# 차집합 -
# 교집합 &
# 합집합 |

a = {5, 3, 9}
b = {4, 2, 3, 0}
a | b # -> {0, 2, 3, 4, 5, 9}
```

```PY
# set으로 중복된 값을 제거해봅시다.
# 정수 1, 2, 3, 1, 1, 2를 원소로 가지는 list를 만듭니다.
# 생성한 list를 set으로 형 변환 합니다.

a = list({1, 2, 3, 1, 1, 2})
# -> [1, 2, 3]

set(a)
# -> {1, 2, 3}
```

-` s.add() method`
```PY
# set()는 시퀀스가 아니기에, index도 안되지만, mutable은 가능. = 변경가능.

s = {1, 2, 3}
s.add(4)
s

# -> {1, 2, 3, 4}
```

### 1.2.2. dictionary
- `{key : value}`
- `key 값`에는 `immutable`(변경 불가능한)= `value type 데이터 만` 가능. 
    ex> `immutable : str, int, float, boolean, tuple, range`
- `value 값`에는 `list, dic 포함한 모든 것` 다 가능


```PY
a = {}
b = dict()
```

- `key는 중복 되면 안됨` = 지문이라고 생각
- value 는 중복 가능 = 동명이인
- `.items()` -> 메소드를 통해 key, value 목록 확인 가능
- `list(dic)` -> `key들만 list화` 됨
- dic[key] = value -> 딕셔너리 value 변경 가능. 