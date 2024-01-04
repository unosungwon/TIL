
> Understanding HTML hierarchy is important because child elements can `inherit` `behavior and styling` from their parent element. 
>
>자식 요소는 부모 요소의 속성을 상속받는다. 

## [!DOCTYPE html]
- declaration "선언" : 브라우저에게 html 버전을 지정하는 선언

## [html][/html]
- 이제부터 사용하는 코드들을 html 로 해석(interpret) 하겠다.

## head 태그 
### ! + tab
- [!DOCTYPE html], [head], [body] 태그 자동으로 생성.
- `metadata`를 포함한다.    
  - 브라우저에게 이 페이지 자체에 대한 정보를 주는 곳


## body 태그
### [h][/h]
- 마크다운의 # 역할과 비슷.

### [br]
- break 태그
- 줄 바꿀 때 사용. 
- 줄을 여러 줄 바꾸고 싶다 해서 태그를 여러개 사용하면 안됨.

### [div][/div]
- 분할, 레이아웃 나누기
- 같은 내용끼리 묶기 위해 사용. 
- 속성 추가 가능. `div id = ""` 으로 분할된 부분에 이름 부여 가능.
- 따로 보여지는 `시각적인 속성은 없음. `

### [span][/span]
- 문단이나 문장 안에 강조하고 싶은 부분에 사용


### [p][/p]
- paragraph
- 문단으로 분리하고 싶을 때 사용

### [pre][/pre]
- 내가 소스에 적은 모습 그대로 보여지길 원할 때
```html
<p>
    def func(x, y):
        return x + y
</p>
<!-- 띄어쓰기 없이 한줄로 코드가 보여짐 -->

<pre>
    def func(x, y):
        return x + y
</pre>
<!-- 문단 나누고 들여쓰기 한 부분 그대로 보여짐 -->
```

### [a][/a]
1. 일반적인 a태그
* [a href="https://google.com"]GOOGLE[/a] 
    * 오프닝 태그 옆에 있는 `href=""` 는 `attribute` 속성임.
    * 태그 사이에 있는 google 이 링크를 품고 있게 됨. 

2. 새탭에서 열고 싶음
```html
<a href="https://naver.com" target="_blank">NAVER</a>
```

3. 비어있는 링크 a태그
* [a href="#"]목적지미정[/a]

### [ol][/ol] , [ul][/ul], [li][/li]
* ol : 순서가 있는 리스트
* ul : 순서가 없는 리스트

```html
<ol>
    [li]집에서 나오기[/li]
        [ul]
            [li]차 키[/li]
            [li]물병 챙기기[/li]
        [/ul]
    [li]병원가기[/li]
    [li]마트가기[/li]
</ol>

<!-- 
1. 집에서 나오기
   - 차 키
   - 물병 챙기기
2. 병원가기
3. 마트가기 
-->
```

### [table][/table], [thead][/thead], [tbody][/tbody]

```html
<table>
    <thead> # column 적을 곳
        <tr>
            <th> 컬럼1 </th>
            <th> 컬럼2 </th>
            <th> 컬럼3 </th>
        </tr>
    </thead>

    <tbody> # value 적을 곳
        <tr>
            <td> aaa1 </td>  # row 기준으로 작성
            <td> bbb1 </td>
            <td> ccc1 </td>
        </tr>
        <tr>
            <td> aaa2 </td>
            <td> bbb2 </td>
            <td> ccc2 </td>
        </tr>
        <tr>
            <td> aaa3 </td>
            <td> bbb3 </td>
            <td> ccc3 </td>
        </tr>
    </tbody>
</table>
```

### [style][/style]
- 테이블 양식 변경 가능
- `head` 에 작성.

```html
<style>
    table{
        border: 표 바깥 테두리;
        width: 표 너비;
        border-collapse: 표 내부 빈칸 없애기 collapse;
    }
    th, td{
        border: value 테두리;
        padding: 각각 value 칸 너비;
        text-align: 가운데 정렬
    }
</style>

```

### [form][/form]



```HTML
<form action="아래 데이터를 보낼 목적지 URL">
    <!-- 회원가입창 보면, action=""여기에 회원가입 내용들을 보낼 서버가 들어간다. -->
    <div id="해당 태그에 유일하게 붙이고 싶은 이름">
        <label for="username">아이디</label>
        <input id="username" type="text">
        <!-- label for == input id 이면, label 누를시 input 창에 자동으로 포커싱 활성화. -->
        <!-- input 에 유형 선택가능. 그 유형이 아닐 시 입력 불가능 -->
    </div>
    <div>
        <label for="password">비번</label>
        <input id="password" type="password">
    </div>
    <div>
        <label for="age">나이</label>
        <input id="age" type="number">
    </div>
    <div>
        <label for="email">이메일</label>
        <input id="email" type="email">
    </div>
    <div>
        <label for="name">자기소개</label>
        <textarea name="" id="bio" cols="30" rows="10"></textarea>
    </div>
    <div>
        <input type="submit">
    </div>
</form>
```

### id=""
- `태그에 유일한 이름`을 붙이고 싶을 때 사용.
- `중복 불가`.
- 특정 요소에 이름을 붙이는 데 사용
- id 속성 사용하고 싶을땐 `'#'` 으로 선택

### class
- `같은 유형으로 반복되는 태그들`을 유형별로 `동일한 class를 사용해 분류`하고 싶을 때 사용. 
- `중복 가능`.
- class 속성 사용하고 싶을땐 `'.'` 으로 선택