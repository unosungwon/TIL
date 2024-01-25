# 선형조합

## 선형조합
* 벡터/행렬에 스칼라값을 곱한 후 더하거나 뺀 것 == `벡터/행렬의 선형조합`
$$
\begin{align}
c_1x_1 + c_2x_2 + c_3x_3 + \cdots + c_Lx_L = x
\end{align}
$$

$$
\begin{align}
c_1A_1 + c_2A_2 + c_3A_3 + \cdots + c_LA_L = A
\end{align}
$$


$$
\begin{align}
c_1, c_2, \ldots, c_L \in \mathbf{R}
\end{align}
$$

$$
\begin{align}
x_1, x_2, \ldots, x_L, x \in \mathbf{R}^M
\end{align}
$$

$$
\begin{align}
A_1, A_2, \ldots, A_L, A \in \mathbf{R}^{M \times N}
\end{align}
$$


## 내적
* 벡터와 벡터의 곱셈
* 벡터 내적의 결과는 `스칼라`가 나온다
$$ 
\begin{align}
x^T y
\end{align}
$$

* `전제조건`
  * 앞의 벡터는 행 벡터, 뒤의 벡터는 열 벡터 => '`ㅓ`' 자 모양
  * 두 벡터의 길이가 같아야 함
    $$
    \begin{align}
    x^T y = 
    \begin{bmatrix}
    x_{1} & x_{2} & \cdots & x_{N} 
    \end{bmatrix}
    \begin{bmatrix}
    y_{1} \\
    y_{2} \\
    \vdots \\
    y_{N} \\
    \end{bmatrix} 
    = x_1 y_1 + \cdots + x_N y_N 
    = \sum_{i=1}^N x_i y_i
    \end{align}
    $$


* 벡터의 내적은 `가중합`을 계산할 때 사용될 수 있음.

  * `가중치`?
    * 결과를 내기 위한 하나의 계수
    * 결과를 결정할 때 부가적인 정보를 의미한다
    * 가중치의 절댓값이 클 수록 결과에 영향을 많이 미친다.

데이터 벡터 : $x=[x_1, \cdots, x_N]$

가중치 벡터 : $w^T=[w_1, \cdots, w_N]$

가중합 : 
$$ 
\begin{align}
w_1 x_1 + \cdots + w_N x_N = \sum_{i=1}^N w_i x_i
\end{align}
$$ 

> ex> 사과 값 1500, 오렌지 값 2000
>
> 사과 2개 사고, 오렌지 3개 사면
>
> $w=[1500, 2000 ]$
>
> $x=[2, 3]$
>
> 가중합 : $w^Tx$


## 유사도
* 내적의 결과값을 해석하려 하지말고, 다른 내적값들과 비교해서 유사성을 찾는것이다.


## 선형회귀 모형
* 독립 미지변수 x 에서 가중치 벡터 w와의 가중합으로 종속변수 y를 `예측`하는 것
* 앞선 `가중합` == 독립변수 x와 가중치 벡터 w로부터의 종속변수 y 값


$$ 
\begin{align}
\hat{y} = w_1 x_1 + \cdots + w_N x_N
\end{align}
$$

$$ 
\begin{align}
\hat{y} = w^Tx
\end{align}
$$

* 예시문제
>
>  * 면적이 1$m^2$ 증가할수록 가격은 500만 원이 증가한다.
>  * 층수가 1층 높아질수록 가격은 200만 원이 증가한다.
>  * 한강이 보이는 집은 1,000만 원의 웃돈(프리미엄)이 존재한다.

=> `가중치 w` = [500, 200, 1000]

=> `독립 미지변수 x` = [면적($x_1$), 층수($x_2$), 한강이 보이는가($x_3$)]

벡터의 내적으로 쓴다면 아래와 같다...

$$ 
\begin{align}
\hat{y} = \begin{bmatrix} 500 & 200 & 1000 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = w^T x
\end{align}
$$


## 제곱합
* 벡터의 내적을 사용해 제곱합이 가능
* 데이터의 분산, 표준편차를 위해서 데이터를 제곱한 뒤 모두 더하는 제곱합이 필요

$$
\begin{align}
x^T x = 
\begin{bmatrix}
x_{1} & x_{2} & \cdots & x_{N} 
\end{bmatrix}
\begin{bmatrix}
x_{1} \\
x_{2} \\
\vdots \\
x_{N} \\
\end{bmatrix} = \sum_{i=1}^{N} x_i^2
\end{align}
$$



## 행렬과 행렬의 곱셈
* 벡터와 벡터의 곱셈은 스칼라가 나오지만, 행렬과 행렬의 곱셈은 행렬이 나온다
* 전제조건:
  * `$A$의 열의 수`와 뒤의 행렬 `$B$의 행의 수`와 같아야 한다.

$$ 
\begin{align}
A \in \mathbf{R}^{N \times L} , \; B \in \mathbf{R}^{L \times M} \;  \rightarrow \; AB \in \mathbf{R}^{N \times M} 
\end{align}
$$

* 곱할때는 `앞 행렬의 1번째 행(행벡터) & 뒤 행렬의 첫번째 열(열벡터)` 을 곱해서 결과 핼렬의 첫번쨰 행의 첫번쨰 열에 기입. 
* 벡터의 곱셈은 스칼라이므로 스칼라가 기입될 것.
* `뒤 행렬의 모든 열을 다 돌았으면`, `다시 앞 행렬의 두번째 행 & 뒤 행렬의 첫번째 열`부터 곱한다.

$$
\begin{align}
\begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33} \\
a_{41} & a_{42} & a_{43} \\
\end{bmatrix}
\begin{bmatrix}
{b_{11}} & b_{12} \\
{b_{21}} & b_{22} \\
{b_{31}} & b_{32} \\    
\end{bmatrix}
=
\begin{bmatrix}
(a_{11}b_{11} + a_{12}b_{21} + a_{13}b_{31}) & (a_{11}b_{12} + a_{12}b_{22} + a_{13}b_{32}) \\
(a_{21}b_{11} + a_{22}b_{21} + a_{23}b_{31}) & (a_{21}b_{12} + a_{22}b_{22} + a_{23}b_{32}) \\
(a_{31}b_{11} + a_{32}b_{21} + a_{33}b_{31}) & (a_{31}b_{12} + a_{32}b_{22} + a_{33}b_{32}) \\
(a_{41}b_{11} + a_{42}b_{21} + a_{43}b_{31}) & (a_{41}b_{12} + a_{42}b_{22} + a_{43}b_{32}) \\
\end{bmatrix}
\end{align}
$$


## 행렬의 교환법칙과 분배법칙
* 교환법칙 불가능, 분배법칙 가능
$$ 
\begin{align}
AB \neq BA  
\tag{2.2.53}
\end{align}
$$

$$ 
\begin{align}
A(B + C) = AB + AC  
\tag{2.2.54}
\end{align}
$$

$$ 
\begin{align}
(A + B)C = AC + BC  
\tag{2.2.55}
\end{align}
$$


## 전치연산의 분배법칙
$$ 
\begin{align}
(A + B)^T = A^T + B^T  
\tag{2.2.59}
\end{align}
$$

$$ 
\begin{align}
(AB)^T = B^T A^T  
\tag{2.2.60}
\end{align}
$$

$$ 
\begin{align}
(ABC)^T = C^T B^T A^T 
\tag{2.2.61}
\end{align}
$$