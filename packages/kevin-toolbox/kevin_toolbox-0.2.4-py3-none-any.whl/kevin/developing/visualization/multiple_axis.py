import matplotlib.pyplot as plt
import matplotlib.axes._axes as axes
import matplotlib.figure as figure
from mpl_toolkits.axisartist.parasite_axes import HostAxes, ParasiteAxes
import numpy as np

# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

"""
roc曲线
"""

# ------------ 准备数据 ------------ #
x_ls, y_ls = np.linspace(0, 10, 10), np.random.uniform(0, 1, size=10)

# ------------ 准备画布与图层 ------------ #
fig = plt.figure(figsize=(4, 4))  # type:figure.Figure

# 通过下面语句指定axes在fig中的位置和大小
# axes = fig.add_axes([left, bottom, width, height])
ax1 = fig.add_subplot()  # type: axes.Axes
# ax.twinx() 生成并返回关于y轴对称的一个axes
ax2 = ax1.twinx()  # type: axes.Axes

# ------------ 绘制图形元素 ------------ #
ax1.plot(x_ls, -y_ls, color='r')
ax2.plot(x_ls, y_ls, color='g')

plt.show()


def func(cfm, axis_paras, to_sort_x=False):
    """
    cfm dict 混淆矩阵
        axis_paras: dict {"x": {"key": key_0_in_cfm}  "y_0": {"key": key_1_in_cfm} }
    """
    x_paras = axis_paras.get("x", None)
    assert isinstance(x, (dict,))
    y_names = sorted([i for i in list(axis_paras.keys()) if i.startswith("y")],
                     key=lambda x: int(x.split("_", -1)[-1]) if "_" in x else -1)
    assert len(y_names) + 1 == len(axis_paras)
    y_paras_ls = [axis_paras[i] for i in y_names]

    # ------------ 准备画布与图层 ------------ #
    fig = plt.figure(figsize=(4, 4))  # type:figure.Figure

    # 添加 axes，并指定其在fig中的位置和大小
    axes_ls = []
    # axes = fig.add_axes([left, bottom, width, height])
    axes_ls.append(fig.add_axes([0.15, 0.1, 0.65, 0.8], axes_class=HostAxes))
    # for# https://www.runoob.com/python/python-func-sorted.html
