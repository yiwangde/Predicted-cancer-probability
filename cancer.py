from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, classification_report
from sklearn.externals import joblib
import pandas as pd
import numpy as np


def logistic():
    """
    逻辑回归做二分类预测癌症
    :return:
    """
    # 构造列名
    c_names = ["Sample code number", "Clump Thickness", "Uniformity of Cell Size",
             "Uniformity of Cell Shape", "Marginal Adhesion", "Single Epithelial Cell Size",
             "Bare Nuclei", "Bland Chromatin", "Normal Nucleoli", "Mitoses", "Class"]

    # 读取数据
    data = pd.read_csv("./breast-cancer-wisconsin.data", names=c_names)

    print(data)

    # 缺失值处理
    data = data.replace(to_replace='?', value=np.nan)

    data = data.dropna()

    # 数据分割
    x_train, x_test, y_train, y_test = train_test_split(data[c_names[1:10]], data[c_names[10]], test_size=0.25)

    # 标准化
    std = StandardScaler()

    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)

    # 逻辑回归预测
    lg = LogisticRegression(C=1.0)

    lg.fit(x_train, y_train)

    print(lg.coef_)

    y_pre = lg.predict(x_test)

    print("准确率：", lg.score(x_test, y_test))

    print("召回率：", classification_report(y_test, y_pre, labels=[2, 4], target_names=["良性", "恶性"]))

    return None
if __name__ == "__main__":
    logistic()