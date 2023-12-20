# SQL basic
> SQL RULES
>
> SQL 기본구성
>   - 데이터베이스 생성 / 선택 
>   - 테이블 생성 / COLUMN, ROW 규칙 생성 / 확인 / 삭제
>   - 테이블에 값 추가
>

## SQL RULES
- SQL `고정 명령어는 대문자`로, `내가 만든 이름은 소문자`로.
- 모두 소문자로 적어도 동작은 하나, Rule 을 지키자.
- 띄어쓰기와 줄 바꿈은 적절히 잘. DB은 띄어쓰기와 줄바꿈을 신경 안씀
- 주석 (COMMENTS) 은  '--'
- 반드시 명령어 끝에는 세미콜론 `';'` 적기.
- 실행은 CTRL + ENTER
---

### SQL 기본구성
- SCHEMAS 에 DATABASE 존재.
- DATABASE 에 TABLE 존재.

---> `SCHEMAS > DATABASE > TABLE > FIELD ...` 

- SQL은 위에서부터 코드가 진행되는 것이 아니라, LINE BY LINE 으로 실행되는 것. 
---

- 데이터베이스 생성
```SQL
CREATE DATABASE 이름;
```
---

`*테이블을 만들 데이터베이스를 먼저 선택 해야함*`

- 데이터베이스 선택
```SQL
USE 데이터베이스이름;

혹은 데이터베이스 더블클릭
```
---

- 테이블 생성
```SQL
CREATE TABLE 이름;
```

- 테이블 내에 COLUMN, ROW 규칙 생성
```SQL
CREATE TABLE 이름(
    COLUMN1 VARCHAR(숫자) 
    COLUMN2 VARCHAR(숫자)
    COLUMN3 INT
);
```

- 테이블 확인
```SQL
DESC 테이블이름;
-> 이런 경우, 위에 테이블 생성시 만들었던 규칙들(type) 과 columns(field), null 등
`속성을 알 수 있다`고 보면 됨
```
```SQL
SELECT * FROM 테이블이름
-> 실제 테이블에 넣은 DATA(RECORDS)들이 들어간 표를 보여준다
```


- 테이블 삭제
```SQL
DROP 테이블이름;
```
---
- 테이블에 값 추가
```SQL
먼저 데이터베이스 꼭 확인!!

INSERT INTO 테이블(COLUMN1,COLUMN2,COLUMN3)
VALUES 
    (DATA,DATA,DATA),
    (DATA,DATA,DATA)
    ;

-> 컬럼명은 이미 테이블에 정해놨던 컬럼명 적고,
넣을 값들은 !컬럼의 TYPE 에 맞춰서! 넣어줘야 함.
```
