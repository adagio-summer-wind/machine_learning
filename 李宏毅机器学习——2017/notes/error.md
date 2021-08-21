[toc]

# 没有看懂，先记结论

> 1、模型的误差可分为 **bias** 和 **variance** 两部分
>
> 2、简单的模型 bias 大、variance小；复杂的模型 bias 小、variance大
>
> bias: 模型预测值的均值与实际值的偏差；
>
> variance：模型预测值的方差

# 依据bias和variance改善模型

## 1、辨别 bias 和 variance

不能很好的拟合训练数据—— bias大

拟合训练数据良好，但不能很好的拟合测试数据——variance 大

## 2、如何处理大的bias

- 选择更加合适的features
- 使用更复杂的模型

 ## 3、如何处理大的variance

- 使用更多的数据
- 简化模型，比如使用regularization

# Cross Validation

![]([machine_learning/cross_validation.jpg at main · adagio-summer-wind/machine_learning (github.com)](https://github.com/adagio-summer-wind/machine_learning/blob/main/李宏毅机器学习——2017/pictures/cross_validation.jpg))

