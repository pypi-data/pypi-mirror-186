import numpy as np
import torch


def check_consistency(*args, tolerance=1e-7, require_same_shape=True):
    """
        检查 args 中多个 array 之间是否一致

        工作流程：
            本函数会首先将输入的 args 中的所有变量转换为 np.array;
            然后使用 issubclass() 判断转换后得到的变量属于以下哪几种基本类型：
                - 当所有变量都属于 np.number 数值（包含int、float等）或者 np.bool_ 布尔值时，
                    将对变量两两求差，当差值小于给定的容许误差 tolerance 时，视为一致。
                - 当所有变量都属于 np.flexible 可变长度类型（包含string等）或者 np.object 时，
                    将使用==进行比较，当返回值都为 True 时，视为一致。
                - 当变量的基本类型不一致（比如同时有np.number和np.flexible）时，
                    直接判断为不一致。
            numpy 中基本类型之间的继承关系参见： https://numpy.org.cn/reference/arrays/scalars.html

        参数：
            tolerance:          <float> 判断 <np.number/np.bool_> 之间是否一致时，的容许误差。
                                    默认为 1e-7。
            require_same_shape: <boolean> 是否强制要求变量的形状一致。
                                    默认为 True，
                                    当设置为 False 时，不同形状的变量可能因为 numpy 的 broadcast 机制而在比较前自动 reshape 为相同维度，进而可能通过比较。
    """
    assert len(args) >= 2
    assert isinstance(tolerance, (int, float,))

    args = [v.detach().cpu() if torch.is_tensor(v) else v for v in args]
    args = [np.asarray(v) for v in args]

    for v in args[1:]:
        if require_same_shape:
            assert args[0].shape == v.shape
        if issubclass(args[0].dtype.type, (np.number, np.bool_,)):
            # 数字类型
            assert issubclass(v.dtype.type, (np.number, np.bool_,))
            if args[0].size > 0:
                assert np.max(np.abs(args[0] - v)) < tolerance, \
                    f"{args[0]}, {v}, deviation: {np.max(np.abs(args[0] - v))}"
        elif issubclass(args[0].dtype.type, (np.flexible, object,)):
            # 可变长度类型
            assert issubclass(v.dtype.type, (np.flexible, object,))
            assert (args[0] == v).all()
        else:
            raise ValueError
