import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

def load_dataset(path):
    path=Path(__file__).resolve().parent/path   # 数据文件路径相对于当前模块所在目录
    with open(path) as file:
        headers=file.readline().strip().split(',')

    # 根据表头选择以 x 开头的特征列，以及名为 y 的标签列。
    x_cols=[i for i in range(len(headers)) if headers[i].startswith('x')]
    y_cols=[i for i in range(len(headers)) if headers[i]=='y']

    inputs=np.loadtxt(path,delimiter=',',skiprows=1,usecols=x_cols)
    labels=np.loadtxt(path,delimiter=',',skiprows=1,usecols=y_cols)

    return inputs,labels

def train(X,y):
    # X 行满秩时，此公式给出满足 X @ beta = y 的最小 L2 范数解。
    beta=X.T @ np.linalg.inv(X @ X.T) @ y
    return beta

def plot_points(norms,val_err,save_path):
    fig=plt.figure()
    plt.scatter(norms,val_err,c='b',marker='o')
    plt.xlabel('norm')
    plt.ylabel('val_mean_err')
    # plt.legend()
    fig.savefig(save_path,dpi=300)
    plt.show()