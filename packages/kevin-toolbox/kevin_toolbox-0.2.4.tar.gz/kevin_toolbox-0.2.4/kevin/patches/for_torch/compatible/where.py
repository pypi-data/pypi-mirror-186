import torch
import numpy as np
from kevin.env_info import version

low_version = version.compare(torch.__version__, "<", "1.2")


def compatible_where(*args):
    """
        参考 torch.where()
            在 1.1 版本及其之前的 pytorch 中的 torch.where()，
            只有 torch.where(condition, x, y) 的用法，
            而没有 torch.where(condition) 的用法，
            考虑到兼容性，在pytorch版本过低时，自动使用 numpy.where() 来替代
    """
    global low_version

    if len(args) == 1 and low_version:
        return np.where(args[0].cpu())
    else:
        return torch.where(*args)


if __name__ == '__main__':
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    x_ = torch.tensor([[1], [2], [3]], device=device)

    print(f"x {x_}, res {compatible_where(x_ > 0)}")

    low_version = True

    print(f"x {x_}, res {compatible_where(x_ > 0)}")
