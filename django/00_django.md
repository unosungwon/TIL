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