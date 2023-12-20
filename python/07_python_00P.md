# 07_OOP_I
>
> 1. a = Cookie( )
>       - a 는 객체다.
> 
>       - a 는 Cookie의 인스턴스다.
>
> 2. class 도 객체다.
>       - 1 은 int 의 인스턴스.
> 
>       - int 는 type의 인스턴스.
>
> 3. 모든 객체는 무언가의 인스턴스다.



# 1. 객체 object
- `객체 = 모든 것`
- 객체 
  - 타입 : 어떤 연산자와 조작이 가능한가
  - 속성 : 어떤 데이터를 가지는가
  - 조작법 : 어떤 행위를 할 수 있는가


## 타입 type
- list, int, str ...

## 인스턴스 instance
- [], '', 1, '123' (종류라고 생각하면 편함.)
- `모든 객체는 무언가의 인스턴스다.`


## 인스턴스 변수

```py
class Person :

    # 인스턴스의 메소드. (클래스의 메소드 아님!!)
    def __init__(self, name):

        # 인스턴스에 소속된 값/ 변수
        self.name = name  # =>self.변수명

p1 = Person('성원')
p1.name  # => 인스턴스 변수
# -> '성원'
```

## 클래스 변수
```py
class Circle:
    pi = 3.14
```



## 메서드 method
- 특정 개체에 적용할 수 있는 행위
- `<객체>.<메서드>()`
- 객체 : 객체 지향 프로그래밍
  - `Object Oriented Programming`
    : 컴퓨터 프로그램을 객체들의 모임으로 파악하고자 하는 것



## class & instance
  
## class 생성
- 클래스 내부에 데이터, 함수 정의 가능.
- 이때 `데이터 = 속성(attribute)`
- `함수 = 메서드(method)`

```py
class 클래스명:
    pass
```

```py
class Book:
    self.author = ''
    self.title = ''
    # self.author 는 데이터, 데이터는 속성.

    def print_info(self):  #함수는 method
        print(self.author)
```


## instance 생성
- instance = 정의된 class에 속하는 개체
- 클래스의 인스턴스 호출 = 클래스명()

```py
class Person:
    pass

p1 = Person()
#인스턴스 = 클래스()
```


## method 정의
- 특정 클래스의 객체에 공통적으로 적용 가능한 행위(behavior)
- 함수니까 인자 추가 가능.

```py
class Person:
    def talk(self):
        print('안녕')
    def eat(self, menu):
        print(f'{meny}를 냐냠')

p1 = Person()
p2 = Person()
p1.talk() 
p2.eat('피자')
# -> '안녕'
# -> '피자'를 냐냠
```


## self ?
- 인스턴스 메소드(함수)는 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계.


## 생성자(constructor) method
- 인스턴스 객체가 생성될 때 호출되는 함수.
- 따로 지정 안하면, 인스턴스 생성 시 아무것도 안뜸.

```py
class MyClass:
    def __init__(self):
        print('생성')

c1 = MyClass()
# -> '생성' 
```

```py
class Person:
    def __init__(self, name):
        print(f'{name}님이 생성')
    def insa(self):
        print('안녕')

p1 = Person('성원') # -> init함수에 지정인자 있음.
# -> '성원'님이 생성
p1.insa() #-> method 함수에 지정인자 없음.
# -> 안녕
```

```py
class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

b1 = Book('ksw', 'learn python')
b1.author
# -> 'ksw'
```

```py
class Introduct:
    def __init__(self):
        self.name = input('이름을 입력하세요: ')
        self.age = input('나이를 입력하세요: ')
        
i1 = Introduct() # -> 생성하면 input 창 나옴.
self.name
#-> input 에 넣은 값 나옴.
```

## 소멸자(destructor) method
- 인스턴스 객체가 소멸되기 직전에 호출되는 함수.
- 약간, `list.pop( i )` 처럼 `삭제`되면서 `내용도 반환` 

```py
class Person:
    def __init__(self, name):
        print(f'{name}객체 생성')
    def __del__(self):
        print('객체 소멸..')

p1 = Person('you')

# 한번 실행 => 'you'객체 생성

# 두번 실행 => 
# 'you'객체 생성
# 객체소멸


```