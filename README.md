<h1 align="center">机器学习 · Machine Learning</h1>

<p align="center"><strong>SEU-CS-OpenSource 系列</strong></p>
<p align="center">课程讲义 · 编程实验 · 学习记录</p>

<p align="center">
  <code>Stanford CS229</code> &nbsp; <code>浙江大学 · 2017</code> &nbsp; <code>Jupyter Notebook</code>
</p>

<p align="center">
  <a href="#课程概览">课程概览</a> ·
  <a href="#课程资料">课程资料</a> ·
  <a href="#目录结构">目录结构</a> ·
  <a href="#使用建议">使用建议</a> ·
  <a href="#关于这个仓库">关于这个仓库</a>
</p>

---

本仓库整理了两门机器学习课程的**部分配套作业与学习资料**，记录从理论学习到编程实践的过程，也希望为同样对机器学习感兴趣的同学提供参考。

> **仓库定位**：本项目归入 SEU-CS-OpenSource 系列，但与东南大学机器学习课程体系无直接关联。

## 课程概览

| 课程 | 收录内容 | 资料目录 |
| :--- | :--- | :--- |
| **Stanford · CS229**（2025 Summer） | 课程讲义、`ps1.pdf`、Ex1–Ex5 编程练习及配套数据 | [Stanford_ML_2025](./Stanford_ML_2025/) |
| **浙江大学 · 机器学习**（2017） | SVM、MLP 两个实验的 Notebook 与实验说明 | [浙江大学_机器学习_2017](./浙江大学_机器学习_2017/) |

## 课程资料

### Stanford · CS229

CS229 是一门值得系统学习的机器学习课程。这里收录的是 **2025 年 Summer 学期的部分配套作业**，建议结合课程视频与讲义学习，在推导与实验之间建立联系。

- **课程讲义**：[Machine Learning — CS229 Lecture Notes](./Stanford_ML_2025/Machine%20Learning%28Stanford%20CS229%20Lecture%20Notes%29.pdf)，更新于 **2026-08-23**。
- **作业题目**：[Problem Set 1（ps1.pdf）](./Stanford_ML_2025/ps1.pdf)。

| 编号 | 实验入口 |
| :---: | :--- |
| Ex1 | [梯度下降](./Stanford_ML_2025/Ex1-梯度下降/) |
| Ex2 | [局部加权线性回归](./Stanford_ML_2025/Ex2-局部加权线性回归/) |
| Ex3 | [线性回归与过拟合问题](./Stanford_ML_2025/Ex3-线性回归与过拟合问题/) |
| Ex4 | [隐式正则化](./Stanford_ML_2025/Ex4-隐式正则化/) |
| Ex5 | [双重下降](./Stanford_ML_2025/Ex5-双重下降/) |

各实验目录包含对应的 Notebook；配套数据、辅助脚本和结果图片随实验一同存放。

### 浙江大学 · 机器学习

这一部分保留了 2017 年课程中的两个实验，作为学习记录与纪念。其中，SVM 实验使用 scikit-learn，MLP 实验使用 TensorFlow。

| 实验 | Notebook | 实验说明 |
| :--- | :--- | :--- |
| **SVM · 兵王问题** | [查看代码](./浙江大学_机器学习_2017/SVM/兵王问题.ipynb) | [查看 PDF](./浙江大学_机器学习_2017/SVM/兵王问题.pdf) |
| **MLP · 多层感知机** | [查看代码](./浙江大学_机器学习_2017/MLP/MLP实验.ipynb) | [查看 PDF](./浙江大学_机器学习_2017/MLP/MLP实验.pdf) |

> **归档说明**：本部分仅收录上述两个实验，并非漏传；考虑到课程年代较早，后续不再补充更新。

## 目录结构

```text
SEU-CS-OpenSource-Machine_Learning/
├── Stanford_ML_2025/
│   ├── Machine Learning(Stanford CS229 Lecture Notes).pdf
│   ├── ps1.pdf
│   ├── Ex1-梯度下降/
│   ├── Ex2-局部加权线性回归/
│   ├── Ex3-线性回归与过拟合问题/
│   ├── Ex4-隐式正则化/
│   └── Ex5-双重下降/
├── 浙江大学_机器学习_2017/
│   ├── SVM/
│   └── MLP/
├── LICENSE
└── README.md
```

## 使用建议

1. **先读讲义与题目**：结合课程录播理解概念，再进入对应实验。
2. **按主题练习**：Stanford 部分可按 Ex1 → Ex5 的顺序阅读和实践。
3. **打开 Notebook**：使用 Jupyter Notebook、JupyterLab 或支持 Notebook 的编辑器阅读与运行 `.ipynb` 文件。
4. **留意相对路径**：运行时将工作目录设为当前实验所在文件夹，以便读取同目录下的数据和辅助模块。

Stanford 实验主要使用 NumPy、Matplotlib 和 SciPy；浙大实验还涉及 pandas、scikit-learn 和 TensorFlow。运行前请按所选 Notebook 的导入语句准备依赖。

## 关于这个仓库

我最初是出于**科研训练**的需要，开始系统学习机器学习，并将过程中整理的资料与实验保存在这里。

学习投入的时间与精力，也希望能成为后续探索的积累。愿这些记录既能帮助有需要的同学，也祝愿自己在科研训练中有所收获、有所产出。

---

仓库许可证：[MIT License](./LICENSE)。
