import torch
from kevin.env_info import version

low_version = version.compare(torch.__version__, "<", "1.8")


def compatible_tile(x, multiples):
    """
        将 input 的各个维度按照 multiples 中的倍速进行复制（占用内存）
            由于在1.7版本及其之前的 pytorch 没有 torch.tile，
            考虑到兼容性，本函数在pytorch版本过低时自动使用 x.repeat() 来实现 tile 函数

        参数：
            x:                  input tensor
            multiples:          要复制的维度
    """
    assert isinstance(multiples, (list, tuple,))

    global low_version
    if low_version:
        return x.repeat(*multiples)
    else:
        return torch.tile(x, multiples)


if __name__ == '__main__':
    x_ = torch.tensor([[1], [2], [3]])
    multiples_ = (1, 3)

    x_tile = compatible_tile(x_, multiples_)
    print(f"x {x_.shape}, x_tile {x_tile.shape}")
    print(f"x {x_},\n x_tile {x_tile}")

    low_version = True

    x_tile = compatible_tile(x_, multiples_)
    print(f"x {x_.shape}, x_tile {x_tile.shape}")
    print(f"x {x_},\n x_tile {x_tile}")
