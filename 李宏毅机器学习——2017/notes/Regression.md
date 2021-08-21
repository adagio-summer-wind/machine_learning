[TOC]



# 线性回归（Regression）的步骤

## 1、Model

a set of functions

**linear model**
$$
\widehat{y} = b + \sum_{i=1}^n (w_i * x_i)
$$

## 2、Loss function

$$
L(f) = L(w, b) = \sum_{t=1}^m (y^t - \widehat{y}^t)^2 \\
=\sum_{t=1}^m (y^t - (b + \sum_{i=1}^n (w_i * x^t_i)))^2
$$

## 3、Optimization

$$
w^*, b^* = argminL(w, b) = argmin(\sum_{t=1}^m (y^t - (b + \sum_{i=1}^n (w_i * x^t_i)))^2)
$$

寻找使 **L(f)** 最小的 w, b 的方法：

​	**Gradient Descent**：

> 1、initialize (随机为w选择一个初始值 w~0~ )
>
> 2、compute gradient at w~0~ ($\frac{dL}{dw}|_{w=w_0}$)
>
> 3、update w to w1 ($w1 = w_0 - lr*\frac{dL}{dw}|_{w=w_0}$)
>
> 4、repeat 2 and 3

**saddle point** 

**local minima**: 实际训练时，参数很多，对所有参数的偏微分全为零的概率很小，local minima 几乎不存在

## 4、Generalisation（test on new datas）



# 调整模型

## 1、使用更加复杂的模型

1.1 
$$
model-2\\
\widehat{y} = b + \sum_{i=1}^n (w_{1i} * x_i) + \sum_{i=1}^n (w_{2i} * x_i^2)\\
model-3\\
\widehat{y} = b + \sum_{i=1}^n (w_{1i} * x_i) + \sum_{i=1}^n (w_{2i} * x_i^2) + \sum_{i=1}^n (w_{3i} * x_i^3)\\
model-4\\
\widehat{y} = b + \sum_{i=1}^n (w_{1i} * x_i) + \sum_{i=1}^n (w_{2i} * x_i^2)\\ + \sum_{i=1}^n (w_{3i} * x_i^3) + \sum_{i=1}^n (w_{4i} * x_i^4)\\
model-5\\
\widehat{y} = b + \sum_{i=1}^n (w_{1i} * x_i) + \sum_{i=1}^n (w_{2i} * x_i^2) + \sum_{i=1}^n (w_{3i} * x_i^3)\\ + \sum_{i=1}^n (w_{4i} * x_i^4) + \sum_{i=1}^n (w_{5i} * x_i^5)
$$
随着模型复杂度提高，开始时模型在训练集和测试集效果提升；但更加复杂时，训练集效果变好，但测试集效果明显变差，出现过拟合（overfitting）

## 2、如何处理Overfitting

1、use more features

2、regularization

新的Loss Function
$$
L(w,b) = \sum_{t=1}^m(y^t - (b^t + \sum_{i=1}^n(w_i^t * x_i^t))) + \lambda * \sum(w_i^t)^2
$$
其中 $\lambda * \sum(w_i^t)^2$ 为正则化项；

​		Why?   

> 新的 L(w, b) 使训练后的 **w** 的取值更小，函数更平滑，即模型变简单；
>
> 而且smoother function is more likely to be correct.

​		仅对 w 正则化，不对 b 正则化

> 因为 b 对model的平滑度和复杂度没有影响





# 术语

model

feature

weight

bias

gradient descent

overfitting

regularization 













