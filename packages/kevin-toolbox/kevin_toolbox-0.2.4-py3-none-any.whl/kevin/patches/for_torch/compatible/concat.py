import torch
from kevin.env_info import version

low_version = version.compare(torch.__version__, "<", "1.10")


def compatible_concat(*args, **kwargs):
    """
        参考 torch.concat()
            在 1.9 版本及其之前的 pytorch 中没有 torch.concat()，
            而只有 torch.cat()，
            两者用法与效果一致， concat 可以看做 cat 的别名
    """

    global low_version
    if low_version:
        return torch.cat(*args, **kwargs)
    else:
        return torch.concat(*args, **kwargs)


if __name__ == '__main__':
    x_ = torch.tensor([[1], [2], [3]])

    print(f"x {x_}, res {compatible_concat((x_, x_), dim=1)}")

    low_version = True

    print(f"x {x_}, res {compatible_concat((x_, x_), dim=1)}")
