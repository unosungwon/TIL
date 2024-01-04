## css 부트스트랩
- https://getbootstrap.com/


## box model


- `block`
  - 항상 새로운 라인에서 시작
  - 화면 크기 전체의 가로폭 차지 (width 100%)
  - `프로퍼티 지정 가능` : width, height, padding, margin
  - block 레벨 요소 내에 inline 레벨 요소 포함 가능
  - block 레벨 요소
    - div, h1~6, p, ol, ul, li, hr, table, form 
  
- `inline`
  - 새로운 라인에서 시작 안함. 문장 중간에 들어감. (즉, `줄을 바꾸지 않고 다른 요소와 함께 한 행에 위치`.)
  - content 너비 만큼만 가로폭 차지.
  - `프로퍼티 지정 불가`
    - padding 은 가능. 
    - 상, 하 여백은 line-height로 지정
  - inline 레벨 요소 뒤에 공백이 있는 경우, 정의하지 않은 space가 자동 지정. 
  - inline 레벨 요소
    - span, a, strong, img, br, input, select, textarea, button

- `display: inline-block;`
  - block 요소 + inline 요소
  - 기본적으로 inline 과 같이 줄 안바꾸고 다른 요소와 한 행에 위치 가능
  - block 요소와 같이 프로퍼티 정의 가능
    - width, height, padding, margin, line-height
  - 컨텐트 너비만큼 가로폭 차지
  - inline-box 요소 뒤에 공백이 있는 경우, 정의하지 않은 space가 자동지정


- `display: flex;`

### <flexbox froggy https://flexboxfroggy.com/#ko>


** 근본은 왼->오/ 위->아래 **

## 전체 이동 (박스에 주는 이동)

- `주축 이동`(가로) (왼->오)
  - `justify-content`: flex-start, center, flex-end
  - justify-content: space-between(요소간 거리), space-around (요소간 양팔벌리기)


- `교차축 이동`(세로) (위->아래)
  - `align-items`: flex-start flex-end center baseline stretch


- `주축`의 start, end `방향을 바꾸자` (오->왼)
  - `flex-direction`: row, row-reverse


- `주축을 세로로` 변경 (위->아래)
  - `flex-direction`: column, column-reverse



## 요소 하나만 이동

- 주축 요소 이동 
  - `order`
  - 0보다 작으면 뒤로 이동, 크면 앞으로 이동


- 교차축 요소 이동
  -` align-self`: flex-start flex-end center baseline stretch


- 주축을 기준으로 한줄에 설 만큼 서고 그 다음 요소들을 다음 줄로 넘어가라
  - `flex-wrap`: nowrap (default) wrap wrap-reverse 

- flex-direction과 flex-wrap이 자주 같이 사용되기 때문에, flex-flow가 이를 대신
  - `flex-flow`: column wrap;

- 교차축 간격 조정
  - `align-content`: flex-start flex-end center space-between space-around space-evenly stretch (default)