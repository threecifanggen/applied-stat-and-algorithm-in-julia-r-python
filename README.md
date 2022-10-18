# applied-stat-in-jupyter

使用`R`、`Python`、`Julia`应用统计学解决实际问题的例子。


## 实现的内容

### 1. 医学特有

#### 1.1 诊断试验统计分析

1. [ROC分析 | `Python`实现](./notebooks/诊断实验统计分析/准确性检验_roc.ipynb)
2. [Bland-Altman一致性分析 | `R`实现](./r/bland-altam-testing.Rmd)

#### 1.2 生存分析

1. [单因素生存分析 | `R`实现](./r/medicine-survival-analysis.Rmd)

### 2. 基本统计学

### 2.1 试验设计

1. 计算试验数量： `python/pytools/exp_design.py`


## 3. 生物信息学

### 3.1 `biopython`使用

1. [`biopython`基本操作](./notebooks/%E5%BA%8F%E5%88%97%E6%95%B0%E6%8D%AE/%E5%BA%8F%E5%88%97%E6%95%B0%E6%8D%AE%E5%9F%BA%E6%9C%AC%E5%A4%84%E7%90%86.ipynb)

## 4. 路线规划

## 依赖

### `Python`

`Python`使用的模块包括：

1. `sympy`
2. `scipy`
3. `statsmodels`
4. `pandas`
5. `numpy`
6. `pyro`


### `R`

`R`使用的额模块包括:

1. `tidyverse`：用于数据处理
2. `predtydoc`: 用于输出美化的`RMarkdown`文件
3. `pROC`：ROC/AUC计算
4. `survival`/`surminer`: 用于生存分析。

## 参考文献

* 潘发明, 编. *医用统计方法及其SPSS软件实现*. 第3版. 合肥: 中国科学技术大学出版社, 2018.
* 李霞和雷健波, 编. *生物信息学*. 第2版. 全国高等学校教材. 北京: 人民卫生出版社, 2015.
* 周登远, 编. *临床医学研究中的统计分析和图形表达实例详解*. 第2版. 北京: 北京科学技术出版社, 2017.
* [意]Allegra Via, [意]Kristian Rother和[意]Anna Tramontano. *Python生物信息学数据管理*. 翻译 卢宏超, 陈一情和李绍娟. 生命科学与信息技术丛书. 北京: 电子工业出版社, 2017.
* Janet L. Peacock和Phiilip J. Peacock. *Oxford Handbook of Medical Statistics*. Oxford ; New York: Oxford University Press, 2011.
* Johnson, D.B. (1973) ‘A Note on Dijkstra’s Shortest Path Algorithm’, *Journal of the ACM*, 20(3), pp. 385–388. Available at: https://doi.org/10.1145/321765.321768.
* Kopec, David. Classic Computer Science Problems in Python. Shelter Island, New York: Manning Publications Company, 2019.
