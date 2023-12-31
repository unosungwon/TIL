# 마크다운 기초

Markdown 은 .md 확장자로 생성

## heagind (제목)
제목은 # 으로 시작하며, 한 칸 띄고 작성한다.
총 6개의 하위 제목까지 작성 가능.
편의상 H1~ H6로 지칭하며, #의 개수 구분 가능.
# H1
## H2
### H3
#### H4
##### H5
###### H6


## 리스트
### ordered list
1. *(순서 쓸 때 1. 1. 이렇게 쓰는 걸 권장)*
1. 손 씻기
    1. *(엔터 치고 탭 키 누르면 안으로 들어온다)*
    1. 물을 틀고 
    1. 손을 적시고
    1. 비누를 칠하고
2. 식당 가기
3. 밥 먹기
    - 김찌
    - 된찌
1. 돈 내기
1. 양치하기


### unoredered list
- -,* 둘다 가능 
- 짜장면
    * 짜장
    * 짬뽕
- 중국집
* 일식집

## 인라인 강조
중요한 것은 **굵게 표시** , 주의할 것은 *기울이고* , 코드나 명령어는 `강조하고`, 취소할 것은 ~~취소선을 긋는다~~.
- bold -> **
- italic -> *
- code -> ``
- cancel -> ~~

## paragraph (내용)
줄바꿈을 하고 싶으면
한번으로는 안되고

두번으로 해야 가능


## 블럭 강조

### table (표)
|id|이름|나이|지역|
|---|---|---|---|
|1|김김김|23|대구|
|2|`이이이`|25|강원도|
|3|박박박|20|의정부|


### code block (코드)
`백틱 3개로` 감싸고, 처음에 쓰는 언어를 명시하면 
문법 표기도 됨. 

```python 
def funcrion(x,y):
    return x + y
```

```sql
select * from users;
```


### latex (수식)
`$` 마크를 사용함

#### 인라인 수식
$x+y$

#### 블럭 수식
$$
\mathbb{N} = \{ a \in \mathbb{Z} : a > 0 \}
$$


## 기타
### QUOTE (인용문)
' > ' 이걸 사용하면 됨

> 우리집 강아지가 최고당
>
> 진짜 최고당

### 가로선
' - ' 3개 작성하면 됨

---

### 이미지/링크
```
링크
[표식텍스트](링크)

이미지
![대체텍스트](이미지링크)
```

링크 : [GOOLGE](http://google.com)

이미지 : ![멋드러진 사진](https://cdn.travie.com/news/photo/first/201710/img_19975_1.jpg)


로컬 사진 : 해당 폴더 안에 사진이 들어와야 있어야 함. 

```
로컬사진
![대체텍스트](파일이름)
```





## 오늘 배운 것
**1. 백틱 (`)**
   
`코딩언어 강조하고 싶으면 하나 쓰고`

``
두개는 뭐더라..? 두개도 강조임
``

```python
세개는 코딩박스
```

**2. 하이픈 (-)**
   
- 하나는 unordered
  
-- 두개는..? 없음

---
세개는 가로선

**3. 별표 (*)**

*`'*'` 하나는 이탈릭*

**`'**'` 두개는 볼드**

**4. 기타**

|표|를|그|리|고|
|--|--|--|--|--|
|싶|으|면|
|이|렇|게|써|라|

>
>인용문은
>
> `'>'` 써서
> 
> 하면된당


수식 쓰고 싶으면 `'$'` 써서 

$10x+y = 5$

### 메모장

>
>**이름 : 김성원**
>
>**나이 : 27**
>

**데이터분석 33회차**

|번호|이름|나이|
|---|---|---|
||||
|1|김성원|27|
|2|||
|3|||

`색깔이 예쁘다`


```python
print('rlatjddnjs')
```

```
링크 갖고오기
[텍스트](링크)
```