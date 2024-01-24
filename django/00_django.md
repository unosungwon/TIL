## 장고의 순서

1. 프로젝트 폴더 생성

    ```py
    $ django-admin startproject 프로젝트폴더
    $ python manage.py runserver  # => `프로젝트 폴더에서` 가동시켜야 함
    ```
   - django 생성하면 생성시 만든` 이름과 똑같은 폴더`와` manage.py` 가 `자동으로 생김`
   - 생성한 이름(프로젝트 폴더)은 바꿔도 ok
   - 자동으로 생성된 똑같은 이름을 가진 폴더는 건들면 안됨

2. app을 터미널에서 만들고 app 생성시 `master/settings 에 installed_apps 에 app 등록`시켜야함!!!
   
    ```py
    $ python manage.py startapp <app_name>
    ```

3. app 폴더에 urls.py 파일 생성

4. `프로젝트폴더/urls.py`에 기본url 뒤에 string1/ 을 붙였을때 app 폴더의 urls.py로 포워딩
   ```py
   path('string1/', include(app.urls))
   ```

5. `app/urls.py 에`
   ```py
   from django.urls import path 
   from . import views
   ```
    불러오기

    두번째 줄은 같은 폴더 (apps 폴더) 내에 views 파일을 import 하겠다는 말.
   
    ```py
    urlpatterns = [
        path('string2/', views.함수이름)
    ]
    ```
    url/atring1/ 뒤에 붙일 string2 이랑, 그 url 을 받았을 때 함수활동을 할 곳을 적기
   
6.  app 폴더의 views.py에 자동으로 불러와져 있음. 
    ```py
    from django.shortcuts import render
    ```
    
    함수를 통해 url/string1/string2 를 눌렀을때 보여주고픈 모습? 을 적으면 됨.

    ```py
    def 함수명(request):
        return render(request, 'html 파일명')
    ```

7. ` html 파일`은 꼭 `app 폴더내의 templates 폴더 생성`해서 만들어야 함. 




## 장고 반복되는 html head 부분 자동 처리하기
1.  project folder 바로 아래에 templates 라는 폴더 만들기. 
1.  그 폴더 아래에 base.html 파일 생성.

1.  templates 라는 폴더를 나중에 base_dir 가 templates 를 찾을때 이 폴더도 포함해서 찾아달라고 해줘야 함. 
  - base_dir ( 프로젝트 폴더) > settings.py > templates 에서 'DIRS' 에 [BASE_DIR/ 'templates'] 이라고 작성.

1.  base.html 에 block 요소 적기
```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>BASE.html</h1>
    
    {% block content %}
    {% endblock content %}
    
</body>
</html>
```

1.  이제 apps > templates 에서 html 만들 시 
```html
{% extends "base.html" %}  => 이게 파일의 최상단에 있어야 한다. 

{% block content %}
  <!-- 여기에 원하는 글씨 적으면 됨.  -->
{% endblock content %}
```



## url/변수 
- url/string1/ 하고 뒤에 변수가 와서, 특정 string 말고 다른 불특정한 글자를 넣어도
넣은 글자 그대로 보고 싶음.

1. apps > urls.py 에 
```py
urlpatterns = [
    path('greeitng/<str:name>/', views.greeting),
]
# domain/greeting/홍길동 => 을 주소창에 썻을때, greeting 함수로 넘어가라.
```

2. apps > views.py 에서

```py
def greeting(request, name):
        # 원래 써야하는 request, 뒤에는 url 뒤에 들어올 변수명('홍길동')을 parameter 로 갖기

    return render(request, 'var_routing/greeting.html',{
        'name' : name
    })

    # django 가 html 을 찾을때,  installed_apps 에 먼저 쓰여져 있는 순서대로 templates 폴더를 찾는다. 같은 이름의 html 을 다른 app 에 사용하고 싶다면, templates 에 하위 폴더를 또 만들어야 함. 

    # render 시, 바로 html 파일 이름을 적는 것이 아니라, django 가 먼저 templates 폴더 내에 적은 하위 폴더명을 찾도록 만들고, 그 다음 html 파일을 찾도록 만든다!! 
```




## 장고 form 형식 만들어서 정보 입력 시 자동으로 연결된 url 로 이동하기
- tistory 에 정리 => https://genuine-suineg.tistory.com/5



## method = "GET" 과 "POST"

- `GET` : URL 뒤에 내가 입력한 데이터들이 나옴, 세상천하에 다 보여진다..
  - 만약, 비밀번호를 입력했으면 url 창에 다 보여진다
  > http://127.0.0.1:8000/utils/bmi_out/?height=155&weight=55


- `POST` : url 뒤에 입력한 데이터가 나오지 않는다!! 
  - 하지만 아래와 같은 오류가 나옴 
  - 오류 내용은 `보안이슈`
>
> Forbidden (403)
> CSRF verification failed. Request aborted.
>
> You are seeing this message because this site requires a CSRF cookie when submitting forms. >This cookie is required for security reasons, to ensure that your browser is not being hijacked by third parties.
>

=> `GET 요청`은 별거 아니다. 대충 해도 된다. `보안걱정 안된다`.

=> `POST 요청`은 별거. 서버가 바뀔 수 있으며 `보안걱정 된다`. 

- 그래서 forbidden 된 것을 통과시키기 위해선 
  1. `프로젝트폴더 > settings.py 에 MIDDLEWARE` 에서 `'django.middleware.csrf.CsrfViewMiddleware' 을 비활성화` 시킨다. 

  2. 혹은, 비활성화 대신, html에 `token을 활용`해서 가능하게 한다.
    ```html
    <div>
    <form action="/utils/bmi_out/" method="POST">
        {% csrf_token %}
        <div>
    ```

- 그 이후 views.py 에서 `dictionary` 가 GET 에서 `POST` 로 바뀌기 때문에, 이것도 바꿔줘야 함.


## 장고 url 변수화

1. 프로젝트폴더에 url 첫 접두사 작성
   ```py
   urlpatterns = [
    path('string1/', include('app.urls')),
    ]
   ```

2. app에 urls.py 에 app_name 으로 변수 할당하기
   ```py
   app_name = 'asdf'

    urlpatterns = [
    # domain/string1/new/  => asdf:new
    path('new/', views.new, name='new'),
   ```

3. html 에서 url 연결할 시 사용 방법 
   - <app_name : name>
  
    ```html
    "{% url "asdf:new" %}"
    ```


## 장고에서 DB 만들기 
1. APP > models.py 에 class 만들기
   ```py
   from django.db import models

   class Class(models.Model):  # Class 라는 class명이 테이블이름이 됨.
    column1 = models.CharField(max_length = 10)
    column2 = models.TextField()
    
    # class 의 attribute 만들고, 데이터 속성도 정해놓기
   ```

2. DB 청사진 확인하기
   ```py
   $ py manage.py makemigrations app이름
   ```

3. DB 만들기
   ```py
   $ py manage.py migrate app이름
   ```



## POST 로 받은 데이터 DB에 저장하기
1. POST 로 받은 데이터는 dictionary 형태로 있으니 value 값만 추출해서 변수에 저장하기
   ```py
    column1 = request.POST['column1']
    column2 = request.POST['column2']
   ```
2. 변수에 할당한 값들을 class 를 instance 화 시켜서 class attribute 에 저장하기
   ```py
   c = Class()  # => Class instance
   c.column1 = column1
   c.column2 = column2   # => Class 의 attribution 인 column1 과 column2 에 변수에 할당한 값 저장하기
   c.save()     # => instance.save() 해야 DB 에 저장이 된다. 
   ```


## Form Class 사용해서
### 1. 유효성 검사 (Validation)


### 2. 입력 input 태그