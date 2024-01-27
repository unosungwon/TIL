https://datascienceschool.net/02%20mathematics/02.02%20%EB%B2%A1%ED%84%B0%EC%99%80%20%ED%96%89%EB%A0%AC%EC%9D%98%20%EC%97%B0%EC%82%B0.html#id35

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



## 행렬 곱셈의 연결
* 연속된 행렬의 곱셈은 교환법칙만 안될 뿐, 순서가 맞다면 상관 없다. 
$$ 
\begin{align}
ABC = (AB)C = A(BC)
\end{align}
$$

$$ 
\begin{align}
ABCD = ((AB)C)D = (AB)(CD) = A(BCD) = A(BC)D
\end{align}
$$


## 항등행렬의 곱셈
* 항등원 : 연산을 수행했을 떄, 값이 원래 모습대로 나오는 것
  * a * 1 = a
  * 1은 a의 곱셈 항등원
  * a + 0 = a
  * 0 은 a의 덧셈 항등원

* 항등행렬
  *  = 주대각이 1 이고 나머지는 0 인 행렬
  *  = 내적에 대한 항등원

$$ 
\begin{align}
AI = IA = A 
\end{align}
$$


## 행렬과 벡터의 곱
* 행렬$M \in \mathbf{R}^{N \times M}$ 과,  ${v} \in \mathbf{R}^{M\times1}$ 의 곱은 벡터 $Mv \in \mathbf{R}^{N \times 1}$ 가 나온다

$$
\begin{align}
\boxed{\begin{matrix} 
\phantom{} & \phantom{} & \phantom{} & \phantom{} & \phantom{} \\ 
& & M & &\\ 
\phantom{} & \phantom{} & \phantom{} & \phantom{} & \phantom{} \\ 
\end{matrix}} \,
\boxed{\begin{matrix} \phantom{\LARGE\mathstrut} \\ v \\ \phantom{\LARGE\mathstrut} \end{matrix}}

=

\boxed{\begin{matrix} 
\phantom{} \\ 
Mv \\ 
\phantom{}  
\end{matrix}}
\tag{2.2.71}
\end{align}
$$



## 열 벡터의 선형조합
* `행렬을 행벡터로 보고 벡터를 곱하면 내적`
* `행렬을 열벡터로 보고 벡터를 곱하면 선형조합`

$$
\begin{align}
\begin{bmatrix}
\boxed{\begin{matrix} \phantom{\LARGE\mathstrut} \\ c_{1_{\phantom{1}}} \\ \phantom{\LARGE\mathstrut} \end{matrix}} &
\boxed{\begin{matrix} \phantom{\LARGE\mathstrut} \\ c_{2_{\phantom{1}}} \\ \phantom{\LARGE\mathstrut} \end{matrix}} &
\cdots & 
\boxed{\begin{matrix} \phantom{\LARGE\mathstrut} \\ c_M \\ \phantom{\LARGE\mathstrut} \end{matrix}} 
\end{bmatrix} 
\begin{bmatrix}
w_1 \\ w_2 \\ \vdots \\ w_M
\end{bmatrix}
=
\begin{matrix}
w_1\,\boxed{\begin{matrix} \phantom{\LARGE\mathstrut} \\ c_{1_{\phantom{1}}} \\ \phantom{\LARGE\mathstrut} \end{matrix}} & + &
w_2\,\boxed{\begin{matrix} \phantom{\LARGE\mathstrut} \\ c_{2_{\phantom{1}}} \\ \phantom{\LARGE\mathstrut} \end{matrix}}& + & 
\cdots \!\!\!\!& + & 
w_M\,\boxed{\begin{matrix} \phantom{\LARGE\mathstrut} \\ c_M \\ \phantom{\LARGE\mathstrut} \end{matrix}}
\end{matrix}
\tag{2.2.73}
\end{align}
$$


## 여러개의 벡터에 대한 가중합 동시 계산

* `벡터 하나` $x$ 의 가중합 
    
    =>  $y = x^Tw$

  * $x \in \mathbf{R}^{1 \times N}$ 
  * 1 => 표본의 개수 == 타겟의 개수 == data의 개수 (몇명)
  * N => data의 종류 (기준)

$
y =
\begin{bmatrix}
x_{1} & x_{2} & \cdots & x_{N}
\end{bmatrix}
$
$\begin{bmatrix}
w_1 \\ w_2 \\ \vdots \\ w_N
\end{bmatrix}
$

* `여러 벡터` ($x_1, \cdots, x_M$) 에 대해서 동시에 계산하고 싶다 ? 
  
   => $\hat{y} = Xw$

  * $x \in \mathbf{R}^{M \times N}$ 
  * M => 표본의 개수 == 타겟의 개수 == data의 개수 (몇명)
  * N => data의 종류 (기준)

$$
\begin{align}
\begin{aligned}
\hat{y} = 
\begin{bmatrix}
\hat{y}_1 \\
\hat{y}_2 \\
\vdots \\
\hat{y}_M \\
\end{bmatrix}
&= 
\begin{bmatrix}
w_1 x_{1,1} + w_2 x_{1,2} + \cdots + w_N x_{1,N} \\
w_1 x_{2,1} + w_2 x_{2,2} + \cdots + w_N x_{2,N} \\
\vdots  \\
w_1 x_{M,1} + w_2 x_{M,2} + \cdots + w_N x_{M,N} \\
\end{bmatrix}
\\
&= 
\begin{bmatrix}
x_{1,1} & x_{1,2} & \cdots & x_{1,N} \\
x_{2,1} & x_{2,2} & \cdots & x_{2,N} \\
\vdots  & \vdots  & \vdots & \vdots \\
x_{M,1} & x_{M,2} & \cdots & x_{M,N} \\
\end{bmatrix}
\begin{bmatrix}
w_1 \\ w_2 \\ \vdots \\ w_N
\end{bmatrix}
\\
&= 
\begin{bmatrix}
x_1^T \\
x_2^T \\
\vdots \\
x_M^T \\
\end{bmatrix}
\begin{bmatrix}
w_1 \\ w_2 \\ \vdots \\ w_N
\end{bmatrix}
\\
&= X w
\end{aligned}
\end{align}
$$

즉.

$$ 
\begin{align}
\hat{y} = Xw 
\end{align}
$$



## 에러, 오류, 오차
* 원래 정해져있던 y 값과 예측 y 값이 다를 때 발생
* 실제y - 예측y = 오차
  * `벡터 하나` $x_i$의 가중합 $w^Tx_i$
  * `벡터 하나의 잔차` = 실제값 - 예측값 = $e_i$
  $$ 
  \begin{align}
  e_i = y_i - \hat{y}_i  = y_i - w^Tx_i
  \end{align}
  $$

  * 모든 독립변수 `(여러벡터)` 벡터의 `잔차` = $e$
  $$
  \begin{align}
  \begin{aligned}
  e 
  &=
  \begin{bmatrix}
  e_{1} \\
  e_{2} \\
  \vdots \\
  e_{M} \\
  \end{bmatrix}
  \\ 
  &=
  \begin{bmatrix}
  y_{1} \\
  y_{2} \\
  \vdots \\
  y_{M} \\
  \end{bmatrix}
  -
  \begin{bmatrix}
  x^T_{1}w \\
  x^T_{2}w \\
  \vdots \\
  x^T_{M}w \\
  \end{bmatrix}
  \\ 
  &= y - Xw
  \end{aligned}
  \end{align}
  $$

  $$
  \begin{align}
  e = y - Xw
  \end{align}
  $$



## 잔차의 제곱합 == RSS
* 잔차 크기 구하기 위해 제곱합을 한다.
* 행렬의 제곱합 구하는 것 처럼 $e^Te$ 로 쓸 수 있음

  $$
  \begin{align}
  \sum_{i=1}^{N} e_i^2 = \sum_{i=1}^{N} (y_i - w^Tx_i)^2 = e^Te =  (y - Xw)^T (y - Xw)
  \end{align}
  $$



## 이차형식
* 가능한 조합의 모든 원소들의 곱하고 합한 스칼라를 알 수 있음.
* 전제 조건 : 행렬은 정방행렬이여야 한다. 

$$
\begin{align}
\begin{aligned}
x^T A x 
&= 
\begin{bmatrix}
x_{1} & x_{2} & \cdots & x_{N} 
\end{bmatrix}
\begin{bmatrix}
a_{1,1} & a_{1,2} & \cdots & a_{1,N} \\
a_{2,1} & a_{2,2} & \cdots & a_{2,N} \\
\vdots & \vdots & \ddots & \vdots \\
a_{N,1} & a_{N,2} & \cdots & a_{N,N} \\
\end{bmatrix}
\begin{bmatrix}
x_{1} \\
x_{2} \\
\vdots \\
x_{N} \\
\end{bmatrix} 
\\
&= \sum_{i=1}^{N} \sum_{j=1}^{N} a_{i,j} x_i x_j 
\end{aligned}
\tag{2.2.85}
\end{align}
$$



## 부분행렬
* 전제조건 : 행렬은 정방행렬
* 여러 방법으로 행렬 곱을 구할 수 있다


$$
\begin{align}
A = 
\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{bmatrix}
,\;\;
B = 
\begin{bmatrix}
b_{11} & b_{12} \\
b_{21} & b_{22}
\end{bmatrix}
\tag{2.2.90}
\end{align}
$$

1. 앞의 행렬을 행벡터로 나누어 계산
  $$
  \begin{align}
  A = 
  \begin{bmatrix}
  \boxed{\begin{matrix} \phantom{} & a_1^T & \phantom{} \end{matrix}} \\ 
  \boxed{\begin{matrix} \phantom{} & a_2^T & \phantom{} \end{matrix}} \\ 
  \end{bmatrix}
  \end{align}
  $$

  $$
  \begin{align}
  a_1^T = 
  \begin{bmatrix}
  a_{11} & a_{12} 
  \end{bmatrix}
  ,\;\;
  a_2^T = 
  \begin{bmatrix}
  a_{21} & a_{22} 
  \end{bmatrix}
  \end{align}
  $$

  $$
  \begin{align}
  AB 
  =
  \begin{bmatrix}
  \boxed{\begin{matrix} \phantom{} & a_1^T & \phantom{} \end{matrix}} \\ 
  \boxed{\begin{matrix} \phantom{} & a_2^T & \phantom{} \end{matrix}} \\ 
  \end{bmatrix}
  B
  =
  \begin{bmatrix}
  \boxed{\begin{matrix} \phantom{} & a_1^TB & \phantom{} \end{matrix}} \\ 
  \boxed{\begin{matrix} \phantom{} & a_2^TB & \phantom{} \end{matrix}} \\ 
  \end{bmatrix}
  \end{align}
  $$
---

2. 뒤의 행렬을 열벡터로 나누어 계산

  $$
  \begin{align}
  B = 
  \begin{bmatrix}
  \boxed{\begin{matrix} \phantom{\mathstrut} \\ b_1 \\ \phantom{\mathstrut} \end{matrix}} \!\!\!\! &
  \boxed{\begin{matrix} \phantom{\mathstrut} \\ b_2 \\ \phantom{\mathstrut} \end{matrix}} 
  \end{bmatrix}
  \end{align}
  $$

  $$
  \begin{align}
  b_1 = 
  \begin{bmatrix}
  b_{11} \\
  b_{21} \\
  \end{bmatrix}
  ,\;\;
  b_2 = 
  \begin{bmatrix}
  b_{21} \\
  b_{22}
  \end{bmatrix}
  \end{align}
  $$

  $$
  \begin{align}
  AB 

  ==

  A
  \begin{bmatrix}
  \boxed{\begin{matrix} \phantom{\mathstrut} \\ b_1 \\ \phantom{\mathstrut} \end{matrix}} \!\!\!\! & 
  \boxed{\begin{matrix} \phantom{\mathstrut} \\ b_2 \\ \phantom{\mathstrut} \end{matrix}}
  \end{bmatrix}
  =
  \begin{bmatrix}
  \boxed{\begin{matrix} \phantom{\mathstrut} \\ Ab_1 \\ \phantom{\mathstrut} \end{matrix}} \!\!\!\! &
  \boxed{\begin{matrix} \phantom{\mathstrut} \\ Ab_2 \\ \phantom{\mathstrut} \end{matrix}}
  \end{bmatrix}
  \end{align}
  $$
---

3. 앞의 행령을 열벡터로, 뒤의 행렬을 행벡터로 나눠 스칼라처럼 계산 가능

  $$
  \begin{align}
  AB =
  \begin{bmatrix}
  a_1 & a_2
  \end{bmatrix}
  \begin{bmatrix}
  b_1^T \\ b_2^T
  \end{bmatrix} =
  a_1b_1^T + a_2b_2^T
  \tag{2.2.97}
  \end{align}
  $$

  $$
  \begin{align}
  AB =
  \begin{bmatrix}
  \boxed{\begin{matrix} \phantom{\mathstrut} \\ a_1 \\ \phantom{\mathstrut} \end{matrix}}  \!\!\!\!& 
  \boxed{\begin{matrix} \phantom{\mathstrut} \\ a_2 \\ \phantom{\mathstrut} \end{matrix}}  \!
  \end{bmatrix}
  \begin{bmatrix}
  \boxed{\begin{matrix} \phantom{} & b_1^T & \phantom{} \end{matrix}} \\ 
  \boxed{\begin{matrix} \phantom{} & b_2^T & \phantom{} \end{matrix}} \\ 
  \end{bmatrix}=
  \boxed{\begin{matrix} \phantom{\mathstrut} \\ a_1 \\ \phantom{\mathstrut} \end{matrix}} 
  \boxed{\begin{matrix} \phantom{} & b_1^T & \phantom{} \end{matrix}} +
  \boxed{\begin{matrix} \phantom{\mathstrut} \\ b_1 \\ \phantom{\mathstrut} \end{matrix}} 
  \boxed{\begin{matrix} \phantom{} & b_2^T & \phantom{} \end{matrix}} 
  \tag{2.2.98}
  \end{align}
  $$
