# 05_data_structure I

## string
### 조회/ 탐색
1. `.find(x)` -> 오류나면 -1 로 반환
2. `.index(x)` -> 오류나면 오류코드가 뜬다
   
   => 둘 다 찾으려는 값의 인덱스를 알려줌.

```py
a = 'apple'

a.find('p')  # -> 1
a.index('p')  # -> 1
```

## 문자열 변경
-> 문자열 = `immutable`(변경할 수 없고),` ordered`, `iterable`

1. `.replace(old, new, count)`
2. `.strip('chars')` -> 기본은 공백, 원하는 글자 지정 가능.
      1. `.rstrip(x)`
      2. `.lstrip(x)`
3. `.split('chars')` -> 문자열을 `리스트로 반환`
4. `'seperator'.join(iterable)` -> `문자열로 반환`
5. `.capitalize()`, `.title()`, `.upper()`
6. `.lower()`, `.swapcase()`
7. 참/ 거짓 반환
      1. `.isalpha()`
      2. `.isdecimal()`
      3. `.isdigit()`
      4. `.isnumeric()`



## 리스트 변경
-> 리스트 = `mutable`(변경할 수 있고), `ordered`, `iterable`

1. `.append(x)` 
   1. ( )안에 있는 모양 그대로 넣어줌.
   2. ( )안에 문자열 추가해도, 그대로 넣어짐.
   3. ( )안에 하나만 가능
   
2. `.extend(iterable)` 
   1. ( )안에 문자열 추가하면, 문자열이 하나씩 쪼개져서 추가 됨. 
   2. ( )안에 [ ]리스트에 문자열을 넣어서 추가해야 안 쪼개짐.
   3. 이런식으로 두개 넣을 수 있음.
   4. ( )안에 list, range, tuple가능


3. `.insert(i, x)` -> 인덱스[i] 위치에 x 추가
4. `remove(x)` -> 값 x를 삭제
5. `.pop(i)` -> [i] 위치를 삭제. 
6. `.clear()` -> 리스트를 삭제. 빈 리스트로 만들어준다.


## 탐색 및 정렬
1. `.count(x)` -> 원하는 값 모두 삭제도 가능.

   ```py
   a = [5, 3, 1, 4, 1, 9]
   for _ in range(a.count(1)):  # -> 1 이 몇개있는지 확인하는 이유 : 1있는 숫자만큼 조건문 반복하려고.
        a.remove(1)
   ```
2. 