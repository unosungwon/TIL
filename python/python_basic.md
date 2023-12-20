# PYTHON
### 설명
>
> - pip install ? 
>   
>   이미 만들어 놓은 라이브러리를 설치하는 것. 
>
>   위치 어디서 입력하던지 상관 없다!!
>   
> - pip ?
>
>   다운 받고 싶은 라이브러리를 일일이 접속, 검색, 다운받는 번거로움을 없애는 명령어.
>
>   `즉, pip = 파이썬 패키지 관리 시스템`
>
---
- 터미널 단축기 = CTRL + ` 
- 터미널에서 파이썬 실행 = `$python 파일명.py`


- `import`
```python
    import calendar
    혹은
    from calendar import prmonth

    -> 두가지 다 모듈을 불러온 건 맞음. 
    -> 다른 점은, 첫번째는 모든 모듈을 불러와서, 모듈 안의 변수 사용시 `모듈.변수=` 이렇게 써야함.

    -> 두번째는 모듈 안의 변수를 콕 집어서 불러온 것이기에 `변수=` 만 사용할 수 있음. 
```

```PYTHON
- # requests = 브라우저를 대체해주는 것. 실행 시 브라우저 안의 것을 가져다 주는 역할
    import requests
    from bs4 import BeautifulSoup

- # 분해할 url 변수로 저장
     a = 'url'

- # requests 라이브러리의 함수인 requests.get()을 사용해서 url 데이터를 변수로 저장
    b = requests.get(a)

- # 변수 b (url 내용) 의 페이지 속성 확인하는 방법
    b.text

- # parsing (구문해석/분석)
  # beautifulsoup는 requests로 불러온 html 소스를 분석,추출하는 데 쓰임.
    c = beautifulsoup (b.text, 'html.parser')

- # beautifulsoup 로 파싱할 페이지소스에서 하나만 추츨할거고, 그걸 변수 설정.
    d = c.select_one('추출하길 원하는 부분 복붙')

- # 찾을 데이터 출력
    print(d)
```


