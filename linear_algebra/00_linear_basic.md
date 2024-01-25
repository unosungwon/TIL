참고 자료 : https://datascienceschool.net/intro.html


# 1장: 수학 기호
## Sequence 수열
* index 가 있음. == "~번쩨" 라고 부를 수 있다
  * off index : index 0 부터 시작
  * index : index 1 부터 시작 

## set 집합
* 순서 (index) 가 없다.
* 고유한 id 를 갖고 있음
* 실수들의 집합
  * $x∈R$ 


## sequence sum, product
* 시그마
$$
\begin{align}
\sum_{i=1}^N x_i = x_1 + x_2 + \ldots + x_N
\end{align}
$$

* 곱
$$
\begin{align}
\prod_{i=1}^N x_i = x_1 \cdot x_2 \cdot \ldots \cdot x_N
\end{align}
$$

* 중첩 가능
  * 중첩시, for문 중첩처럼 반복된다
$$ 
\begin{align}
\begin{aligned}
\sum_{i=1}^2 \sum_{j=1}^3 ( i+j ) 
&= \sum_{i=1}^2 \left( \sum_{j=1}^3 ( i+j ) \right) \\
&= \sum_{i=1}^2 \big( (i+1) + (i+2) + (i+3) \big) \\
&= \big((1 + 1) + (1 + 2) + (1 + 3)\big) + \big((2 + 1) + (2 + 2) + (2 + 3)\big)
\end{aligned}
\end{align}
$$


# 2장 데이터와 행렬

## 데이터 유형
* 스칼라
  * 0차원 데이터 
$$
\begin{align}
x \in \mathbf{R} 
\end{align}
$$

* 벡터
  * 1차원 데이터
  * 데이터 증가 가능
  * 밑의 경우, `N개의 표본에 대한 1가지 데이터` 로 볼수 있음
    $$ 
    \begin{align}
    x = \begin{bmatrix}
    x_{1} \\
    x_{2} \\
    \vdots \\
    x_{N} \\
    \end{bmatrix}
    \end{align}
    $$


    $$
    \begin{align}
    x \in \mathbf{R}^N
    \end{align}
    $$

  * 벡터를 행렬처럼 표현도 가능
    $$ 
    \begin{align}
    x \in \mathbf{R}^{4\times 1}
    \end{align}
    $$


* 행렬
  
  * 2차원 데이터
  * 행렬을 pandas 의 dataframe 으로,
  * 행렬의 열을 pandas의 series 로 볼 수 있음. 
    $$ 
    \begin{align}
    X \in \mathbf{R}^{6\times 4}
    \end{align}
    $$

    $$
    \begin{align}
    X = 
    \begin{bmatrix}
    \boxed{\begin{matrix} x_{1, 1} & x_{1, 2} & x_{1, 3} & x_{1, 4}\end{matrix}}  \\
    \begin{matrix} x_{2, 1} & x_{2, 2} & x_{2, 3} & x_{2, 4}\end{matrix} \\
    \begin{matrix} x_{3, 1} & x_{3, 2} & x_{3, 3} & x_{3, 4}\end{matrix} \\
    \begin{matrix} x_{4, 1} & x_{4, 2} & x_{4, 3} & x_{4, 4}\end{matrix} \\
    \begin{matrix} x_{5, 1} & x_{5, 2} & x_{5, 3} & x_{5, 4}\end{matrix} \\
    \begin{matrix} x_{6, 1} & x_{6, 2} & x_{6, 3} & x_{6, 4}\end{matrix} \\
    \end{bmatrix}
    \end{align}
    $$



## 전치 연산 (transpose)
* 행렬의 열과 행을 바꾸는 연산
$$
\begin{align}
x \;\; \rightarrow \;\; x^T
\end{align}
$$

$$
\begin{align}
X = 
\begin{bmatrix}
\boxed{\begin{matrix} x_{1, 1} & x_{1, 2} & x_{1, 3} & x_{1, 4}\end{matrix}}  \\
\begin{matrix} x_{2, 1} & x_{2, 2} & x_{2, 3} & x_{2, 4}\end{matrix} \\
\begin{matrix} x_{3, 1} & x_{3, 2} & x_{3, 3} & x_{3, 4}\end{matrix} \\
\begin{matrix} x_{4, 1} & x_{4, 2} & x_{4, 3} & x_{4, 4}\end{matrix} \\
\begin{matrix} x_{5, 1} & x_{5, 2} & x_{5, 3} & x_{5, 4}\end{matrix} \\
\begin{matrix} x_{6, 1} & x_{6, 2} & x_{6, 3} & x_{6, 4}\end{matrix} \\
\end{bmatrix}
\;\; \rightarrow \;\;
X^T = 
\begin{bmatrix}
\boxed{\begin{matrix} x_{1, 1} \\ x_{1, 2} \\ x_{1, 3} \\ x_{1, 4}\end{matrix}} &
\begin{matrix} x_{2, 1} \\ x_{2, 2} \\ x_{2, 3} \\ x_{2, 4}\end{matrix} &
\begin{matrix} x_{3, 1} \\ x_{3, 2} \\ x_{3, 3} \\ x_{3, 4}\end{matrix} &
\begin{matrix} x_{4, 1} \\ x_{4, 2} \\ x_{4, 3} \\ x_{4, 4}\end{matrix} &
\begin{matrix} x_{5, 1} \\ x_{5, 2} \\ x_{5, 3} \\ x_{5, 4}\end{matrix} &
\begin{matrix} x_{6, 1} \\ x_{6, 2} \\ x_{6, 3} \\ x_{6, 4}\end{matrix} &
\end{bmatrix}
\end{align}
$$

* 벡터 또한 전치 가능
  * 벡터의 경우 defalut 값은 열벡터
  * 벡터의 t는 행벡터
$$ 
\begin{align}
x = 
\begin{bmatrix}
x_{1} \\
x_{2} \\
\vdots \\
x_{N} \\
\end{bmatrix}
\; \rightarrow \;
x^T = 
\begin{bmatrix}
x_{1} & x_{2} & \cdots & x_{N}
\end{bmatrix}
\end{align}
$$

## 영벡터
* 모든 원소가 0인 N차원 벡터
$$ 
\begin{align}
\mathbf{0}_N = \mathbf{0} = 0 =
\begin{bmatrix}
0 \\
0 \\
\vdots \\
0 \\
\end{bmatrix}
\end{align}
$$

$$ 
\begin{align}
0 \in \mathbf{R}^{N \times 1}
\end{align}
$$

## 일벡터
* 모든 원소가 1인 N차원 벡터
$$ 
\begin{align}
\mathbf{1}_N = \mathbf{1}  = 1 = 
\begin{bmatrix}
1 \\
1 \\
\vdots \\
1 \\
\end{bmatrix}
\end{align}
$$

$$ 
\begin{align}
1 \in \mathbf{R}^{N \times 1}
\end{align}
$$

## 정방행렬
* 행과 열의 개수가 같은 행렬
* 대각행렬이 생기는데, transpose 는 대각행렬을 기준으로 원소들을 뒤집어준다
$$ 
\begin{align}
D = 
\begin{bmatrix}
d_{1} & 0 & \cdots & 0 \\
0 & d_{2} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & d_{N} \\
\end{bmatrix}
\end{align}
$$

$$ 
\begin{align}
D \in \mathbf{R}^{N \times N}
\end{align}
$$


## 벡터&행렬의 덧셈, 뺼셈

* 전제조건 : 크기가 같을 것.
* 방법 : 두 벡터, 행렬에서 같은 위치에 있는 원소 끼리
$$
\begin{align}
x + y =
\begin{bmatrix}
10 \\
11 \\
12 \\
\end{bmatrix}
+
\begin{bmatrix}
0 \\
1 \\
2 \\
\end{bmatrix}
=
\begin{bmatrix}
10 + 0 \\
11 + 1 \\
12 + 2 \\
\end{bmatrix}
=
\begin{bmatrix}
10 \\
12 \\
14 \\
\end{bmatrix}
\end{align}
$$

$$
\begin{align}
x - y =
\begin{bmatrix}
10 \\
11 \\
12 \\
\end{bmatrix}
-
\begin{bmatrix}
0 \\
1 \\
2 \\
\end{bmatrix}
=
\begin{bmatrix}
10 - 0 \\
11 - 1 \\
12 - 2 \\
\end{bmatrix}
=
\begin{bmatrix}
10 \\
10 \\
10 \\
\end{bmatrix}
\end{align}
$$

## 스칼라와 벡터&행렬의 곱셈
* 분배 방식으로 곱셈 가능
$$
\begin{align}
c
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}
=
\begin{bmatrix}
cx_1 \\
cx_2
\end{bmatrix}
\end{align}
$$


$$
\begin{align}
c
\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{bmatrix}
=
\begin{bmatrix}
ca_{11} & ca_{12} \\
ca_{21} & ca_{22}
\end{bmatrix}
\end{align}
$$
