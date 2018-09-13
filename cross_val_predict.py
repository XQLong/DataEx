from sklearn import linear_model, datasets
from sklearn.model_selection import cross_val_predict
import matplotlib.pyplot as plt
# 定义一个线性回归对象
lr = linear_model.LinearRegression()
# 加载数据
boston = datasets.load_boston()


# ‘target’, the regression targets
y = boston.target
# cross_val_predict returns an array of the same size as `y` where each entry
# is a prediction obtained by cross validation:
# 对数据集进行指定次数的交叉验证,返回的是estimator 的分类结果（或回归值）
predicted = cross_val_predict(lr,boston.data,y,cv = 10)

fig, ax = plt.subplots()
ax.scatter(y,predicted,edgecolors = (0,0,0))
ax.plot([y.min(),y.max()],[y.min(),y.max()],'k--',lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()