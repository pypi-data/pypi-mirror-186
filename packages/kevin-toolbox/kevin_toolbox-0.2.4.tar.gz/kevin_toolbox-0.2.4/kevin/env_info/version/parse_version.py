def parse_version_string_to_array(string, **kwargs):
    """
        将版本的字符串转换为数组的形式
        参数：
            string:                 string of version
            sep：                    分隔符
        工作流程：
            string "1.2.3"  == sep '.' ==> array [1, 2, 3]
            注意：对于分割后包含非整数的 string，默认返回 [0]，例如：
            string "1.2_3"  == sep '_' ==> array [0]
        返回：
            array:                 array of version
    """
    sep = kwargs.get("sep", '.')
    assert isinstance(string, (str,))

    array = string.split(sep, -1)
    for i, v in enumerate(array):
        if v.isdigit():
            array[i] = int(v)
        else:
            # 对于不符合规则的，直接返回 0
            array = [0]
            break
    return array


if __name__ == '__main__':
    print(interpret_version_string("1.2.3"))
