# kevin_toolbox

一个通用的工具代码包集合



包含以下package：

[TOC]

环境要求

```shell
numpy>=1.19
pytorch>=1.10
```





## data_flow

与数据流相关

### core

与底层操作相关



#### cache

缓存的生成与管理

- Cache_Manager_for_Iterator 适用于迭代器/生成器的缓存管理器
- Strategies 现有策略



#### reader

读取内存、外存中的数据

- File_Iterative_Reader 分批次读取文件内容的迭代器
- Unified_Reader_Base 按行读取数据的抽象基类
- UReader



### file

文档读写

【finished 单元测试已完成】



#### json_

基于 json 包构建，同时定义了一系列实用的 object_hook/converter 用于支持不同场景下的解释。

- write(content, file_path)
- read(file_path, converters=[<converter>, ...])
- converter
  - convert_dict_key_to_number 尝试将字典中的所有 key 转换为数字



#### kevin_notation

 遵守 kevin_notation 格式的数据文本读取器/写入器（格式要求参见本模块下的 readme）。支持分批次向文件写入内容。

- Reader

  ```python
          """
              设定关键参数
  
              必要参数：
                  file_path:          <string> 文件路径
              读取相关参数：
                  chunk_size:         <integer> 每次读取多少行数据
                  beg：                <integer> 开始读取的位置
                                                  默认为0
                  converter:          <instance of kevin.Converter> converter is a dictionary-like data structure
                                                  consisting of <string>:<func> pairs，
                                                  用于根据指定数据类型选取适当的函数来处理输入数据。
          """
  ```

  - 基本使用：

    ```python
        with kevin_notation.Reader(file_path=file_path, chunk_size=chunk_size) as reader:
            # metadata
            print(reader.p_metadata)
            # content
            content = next(reader)
            for chunk in reader:
                for key in content.keys():
                    content[key].extend(chunk[key])
            print(content)
    ```



- Writer

  ```python
          """
              设定关键参数
  
              必要参数：
                  file_path:          <string> 文件路径
              写入相关参数：
                  mode:               <string> 写入模式
                                          支持以下模式：
                                              "w":    从头开始写入
                                              "a":    从末尾续写（要求文件已经具有 metadata）
                  paras_for_open:     <paras dict> open() 函数的补充参数（除 mode 以外）
                  converter:          <instance of kevin.Converter> converter is a dictionary-like data structure
                                              consisting of <string>:<func> pairs，
                                              用于根据指定数据类型选取适当的函数来处理输入数据。
                  sep：                <string> 默认的分隔符
                                              默认使用 \t
          """
  ```

  - 基本使用（具体参考测试用例）：

    ```python
        # 新建
        part = np.random.randint(1, 5)
        values = list(zip(*[expected_content[key][:-part] for key in expected_metadata["column_name"]]))
        with kevin_notation.Writer(file_path=file_path, mode="w", sep=expected_metadata["sep"]) as writer:
            writer.metadata_begin()
            for key, value in expected_metadata.items():
                if key == "sep":
                    pass
                elif key == "column_name":
                    writer.column_name = value
                elif key == "column_type":
                    # 尝试使用局部指定的 sep
                    writer.column_type = {"value": value, "sep": " "}
                else:
                    writer._write_metadata(key, value)
            writer.metadata_end()
    
            writer.contents_begin()
            writer.contents = values
            writer.contents_end()
    
        # 续写
        values = list(zip(*[expected_content[key][-part:] for key in expected_metadata["column_name"]]))
        with kevin_notation.Writer(file_path=file_path, mode="a") as writer:
            writer.contents = values
            writer.contents_end()
    ```



## machine_learning

与机器学习相关

### dataset

与数据集相关的处理工具

【finished 单元测试已完成50%】

- face
  - dummy
    - Factory 用于生成人脸识别的伪数据

  - verification
    - Factory 用于生成人脸识别 1:1 验证任务的数据集 
    - get_generator_by_block() 构造一个迭代生成数据集的迭代器，并返回
    - get_generator_by_samples() 构造一个迭代生成数据集的迭代器，并返回

### statistician

与统计相关的计算工具，比如混淆矩阵、tpr和fpr

【finished 单元测试已完成50%】

- binary_classification
  - cal_cfm
  - merge_cfm_ls
  - cal_cfm_iteratively_by_chunk
  - cal_tpr_and_fpr
  - Accumulator_for_Cfm
  - convert_to_numpy



## patches

对其他包的补丁

TODO 单元测试未完成：

### for_torch

一些用于对pytorch进行补充的自定义模块

- math
  - my_around()
    - 保留到指定的小数位数。（类似于 np.around() 函数）
  - get_y_at_x()
    - 对于 xs :=> ys 定义的离散函数，获取给定 x 下 y 的取值
- compatible：兼容低版本pytorch
  - tile
  - where

### for_test

用于测试场景

- check_consistency(*args, tolerance=1e-7, require_same_shape=True)

```python
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
```





## scientific_computing

科学计算相关。

包括数学、维度操作、离散余弦变换、基于椭圆曲线的随机生成（正在开发中）等。





### dimension

与维度变换相关

【finished 单元测试已完成】



#### transpose

转置。

【同时支持对np.array和torch.tensor进行变换】

- inside_axis( x, axis, index_ls, reverse )
  - 将变量 x 的第 axis 个轴内的各个维度，按照 index_ls 的顺序进行重排/转置
- get_inverse_index_ls()
  - 获取转置的逆



#### coordinates

与坐标遍历/格式转换相关

【坐标使用np.array保存】

- convert(var, input_format, output_format)
  - 在各种格式的 坐标列表 之间进行转换
  - 坐标格式的介绍参见该模块下的 readme.md
- generate(shape, pattern, output_format)
  - 按照不同模式 pattern 对 shape 进行遍历，并生成指定格式的 坐标列表



#### reshape

改变变量形状。

【同时支持对np.array和torch.tensor进行变换】

- flatten( x, dim_num, generate_func )
  - 将 x 的最后 dim_num 个维度按照 generate_func 指定的遍历顺序进行打平展开

  ```python
  参数示例：
  
  - generate_func
    - = lambda shape: coordinates.generate(shape=shape, pattern="z_pattern", output_format="zip_indices")
    - = lambda shape: coordinates.generate(shape=shape, pattern="shuffle_inside_block", output_format="zip_indices", kwargs=dict(seed=114))
  ```

- unflatten( x, shape, generate_func )
  - 将 x 最后的一个维度，按照 shape 对应的 generate_func 指定的遍历顺序进行堆叠。实际上就是打平展开 flatten() 的逆向操作。

  ```python
  参数示例：
  
  - generate_func
    - = lambda shape: coordinates.generate(shape=shape, pattern="z_pattern", output_format="index_ls")
    - = lambda shape: coordinates.generate(shape=shape, pattern="shuffle_inside_block", output_format="index_ls", kwargs=dict(seed=114))
  # 与上面 flatten 的区别在于输出格式 output_format
  # 注意当使用带有随机生成的模式时，比如 shuffle_inside_block，需要在 kwargs 中补充指定随机种子才能保证 flatten 与 unflatten 之间的结果可逆
  ```

- split_blocks(x, block_shape)
  - 将最后部分的维度 axis 按照 block_shape 分割成 blocks 的组成。
  -  例如，对于 x=[5, 6, 6]，在 block_shape=[3, 2] 的情况下将得到 y=[5, 2, 3, 3, 2]
- merge_blocks(x, block_axis_num)
  - 将最后 block_axis_num 个维度看做是 block，合并到此前 axis_num 个维度上。
  - 是 split_blocks() 的逆操作。



#### concat_and_split

- concat_crops_into_whole(**kwargs)

```python
    """
        将 crop 按照对应的 box 指示的位置，以行优先的内存顺序，进行拼接、展平

        工作流程：
            首先根据 box_ls 构建 computational_tree，然后将 crop 按照对应的 box 分配到计算图中对应的叶节点，调用计算图中的 concat()
            进行合并，最后从计算图的根节点中取出最后合并得到的结果。

        参数：
            crop_ls:        <list of np.array/tensor>
            box_ls:         <list of np.arrays>
                                each element is an array with shape [2, dimensions]
                                各个维度的意义为：
                                    2：          box 的两个轴对称点
                                    dimensions： 坐标的维度
                                要求：
                                    - 各个 box 应该是已经 sorted 的，亦即小坐标在前大坐标在后。
                                        例如 box=[[1,2],[0,4]] 是错误的。
                                        而 box=[[0,2],[1,4]] 是合法的。
                                    - 各个 box 在坐标轴上的投影之间没有重叠部分
                                    函数 geometry.for_boxes.boolean_algebra() 返回的 boxes 结果，以及
                                    函数 geometry.for_boxes.detect_collision() 返回的 node_ls 中每个 node 下面
                                    的 node.description["by_boxes"] 都符合该要求。
            beg_axis:       <integer> 上面提供的 box 中指定的坐标是从 crop 的第几个 axis 开始对应的。
                                例如： beg_axis=1 时，box=[[i,j],[m,n]] 表示该 crop 是从原张量的 [:, i:m, j:n, ...] 部分截取出来的。
            computational_tree: <Node> 计算图
                                默认为 None，函数将根据输入的 box_ls 自动构建计算图。
                                你也可以将已有的计算图代入该参数中，以跳过构建计算图的步骤，节省计算量。
            return_details: <boolean> 是否以详细信息的形式返回结果
                                默认为 False，此时返回：
                                    whole:  <np.array/tensor> 对 crop_ls 进行合并后的结果
                                当设置为 True，将返回一个 dict：
                                    details = dict(
                                        whole = <np.array/tensor>,  # 对 crop_ls 进行合并后的结果
                                        box_ls = <list of np.arrays>,  # 按照 内存顺序 对 box_ls 进行排序后的结果
                                        crop_ls = <list of np.array/tensor>,  # 按照 内存顺序 对 crop_ls 进行排序后的结果
                                        beg_axis = beg_axis,  # 对应与输入的 beg_axis
                                        computational_tree = <Node>,  # 计算图
                                    )
        返回：
            whole 或者 details
    """
```



- split_whole_into_crops(**kwargs)

```python
    """
        将变量 whole 按照 box_ls 指示的位置，以行优先的内存顺序，拆解成多个 crop
            系 concat_crops_into_whole() 的逆变换

        参数：
            whole:          <np.array/tensor>
            box_ls:         <list of np.arrays>
            beg_axis:       <integer> 要对 x 进行分割的轴
            computational_tree: <Node> 计算图
            return_details: <boolean> 是否以详细信息的形式返回结果
                                默认为 False，此时返回：
                                    crop_ls:  <list of np.array/tensor> 分割结果
                                当设置为 True，将返回一个 dict：
                                    details = dict(
                                        whole = <np.array/tensor>,  # 对 crop_ls 进行合并后的结果
                                        box_ls = <list of np.arrays>,  # 按照 内存顺序 对 box_ls 进行排序后的结果
                                        crop_ls = <list of np.array/tensor>,  # 按照 内存顺序 对 crop_ls 进行排序后的结果
                                        beg_axis = beg_axis,  # 对应与输入的 beg_axis
                                        computational_tree = <Node>,  # 计算图
                                    )
                （以上参数的详细介绍参见 concat_crops_in_memory_order()）
        返回：
            crop_ls 或者 details
    """
```



- Node

计算图节点

以上函数 concat_crops_into_whole() 和 split_whole_into_crops() 的内核



### transform

信号/图像处理，时域频域变换等

【finished 单元测试已完成】



#### dct

离散余弦变换

（在本模块下的 example 文件夹中提供了一个示例展示如何使用本模块结合 kevin.scientific_computing 下的其他模块实现图像的低通or高通滤波。）

- generate_trans_matrix(**kwargs)

```python
    """
        生成用于进行1维离散余弦变换（DCT）的变换基

        使用方法：
            假设要变换的1维信号队列为 X [k, n]
                其中：
                - n 为信号序列的长度（在DCT中一般将输入的信号序列视为经过时轴对称延拓后得到的周期为2n的序列）
                - k 为信号的通道数。
                你可以将 X 视为 k 个长度为 n 的1维信号的组合。
            使用该函数生成一个转换基 B [n, m]
                其中：
                - m 表示基向量/基函数的数量（数量越大越能整合高频信号）
                - n 为基向量的长度/基函数的离散采样点数量，与输入周期信号的周期的一半相等
            则变换过程为 Y = X @ B
                得到的 Y [k, m]

        如何推广到多维？
            原理：
                由于频域变换的维度可分离性，因此可以将多维 DCT 变换分解为对信号的每个维度单独做1维 DCT 变换。
            具体方法：
                以 2d DCT 变换为例，假设输入信号为 X [k, n0, n1]
                    1.0 首先使用该函数生成针对于维度 n1 的变换基 B1 [n1, m1]
                    1.1 对维度 n1 进行变换：Z = X @ B1，得到 Z [k, n0, m1]
                    1.2 对 Z 进行转置 Z = Z.permute(0, 2, 1) 得到 Z [k, m1, n0]
                    2.0 类似地生成变换基  B0 [n0, m0]
                    2.1 对维度 n0 进行变换：Y = Z @ B0，得到 Y [k, m1, m0]
                    2.2 对 Y 进行转置恢复维度顺序 Y = Y.permute(0, 2, 1) 得到 Z [k, m0, m1]
        参数：
            sampling_points_num:    <integer> 转换矩阵的行数，对应 基函数的离散采样点数量
                                                与输入周期信号的周期的一半相等
            basis_series_num:       <integer> 转换矩阵的列数，对应 基向量/基函数的数量
                                                数量越大越能整合高频信号，但不应超过采样点的数量 sampling_points_num
                                                如果超过则会导致列向量不再两两正交，也不一定保证单位化
            shape:                  <list of integers> 长度为 2 的列表，记录了 [sampling_points_num, basis_series_num]
                当 sampling_points_num ... 和 shape 被同时设定时，以前者为准。

        返回：
            B       <np.array> shape [r_num, c_num]
                矩阵中各元素为
                    B[r,c] := g(c) * sqrt(2/r_num) * cos( (2*r + 1) * c * pi / (2*r_num) )
                        其中 g(c) := sqrt(1/2) if c==0 else 1

        技巧：
            当两个转换矩阵的 r_num 相同时，小矩阵可以直接从大矩阵中截取，而不需要重新计算。
    """
```



- Calculator

  ```python
      """
          多维dct变换
              对张量的最后几个维度进行dct变换或者逆变换
  
          使用方法：
              calculator = dct.Calculator(...)  # 可预设使用的转换矩阵
              outputs = calculator(inputs, reverse, ...)
          更多请参考 calculator.cal() 函数的介绍
  
          ps：
              - 本模块计算DCT时并没有使用类似FFT的动态规划方式来节省计算量，因为本模块更多地关注使用gpu并行计算的场景，而
                  诸如文章 https://jz.docin.com/p-699413364.html 中的快速DCT都难以实行并行计算。
                  因而对于 basis_series_num 较小（能够被gpu一次性装下并计算）的情况，快速DCT的实际速度较慢。
                  以后有可能会针对cpu的场景，增加快速DCT的计算方式。
              - 本模块支持 torch.tensor/np.array 类型的输入，并且会将输入变量所在的设备来作为计算设备。
                  因此如果需要使用 gpu 进行计算，请首先保证输入变量已经指定到某个 gpu 设备上了。
      """
  ```

  - cal(**kwargs)

    ```python
            """
                多维dct变换
                    对张量的最后几个维度进行dct变换或者逆变换
    
                参数：
                    x:                          <torch.tensor/np.array> 输入张量
                    reverse:                    <boolean> 是否进行逆变换
                    sampling_points_num_ls:     <list of integers> 对应维度上，进行转换时，采样点数量，的列表
                                                    不设置时，默认使用初始化时设置的值，
                                                    如果进一步连初始化时也没有设置时，将尝试根据 x 和 basis_series_num_ls 推断得到
                    basis_series_num_ls:        <list of integers> 对应维度上，进行转换时，使用的基函数数量，的列表
                                                    不设置时，默认使用初始化时设置的值，
                                                    如果进一步连初始化时也没有设置时，将尝试根据 x 和 sampling_points_num_ls 推断得到
    
                例子：
                    在 reverse=False 正向模式下时，当输入为 x [b, n0, n1, n2] 时，
                        在设置 sampling_points_num_ls=[n0, n1, n2] 和 basis_series_num_ls=[m0, m1, m2] 下，
                        将对输入的最后 len(basis_series_num_ls)=3 个维度进行变换，得到 y [b, m0, m1, m2]
    
                注意：
                    - 基函数的数量 basis_series_num 不应超过采样点的数量 sampling_points_num
                    - 当基函数的数量 basis_series_num 小于采样点的数量 sampling_points_num 时，此时转换过程是有损的，将丢失高频信息
                    - 本函数将输入变量 x 所在的设备来作为计算设备。因此如果需要使用 gpu 进行计算，请首先保证输入变量已经指定到某个 gpu 设备上了。
    
                建议：
                    - 对于 np.array 类型的输入和 dtype!=torch.float32 的 torch.tensor 类型的输入，
                        本函数会先转换成 <torch.tensor with dtype=float32> 再进行计算，
                        因此直接使用 <torch.tensor with dtype=float32> 类型输入可以跳过该转换过程，从而实现加速。
    
                返回：
                    y：          <torch.tensor with dtype=float32> （所在设备与输入变量保持一致）
            """
    ```

    

#### scaling_and_shift

放缩，以及各种归一化操作。

【同时支持对np.array和torch.tensor进行变换】

- scaling(**kwargs)

```python
    """
        以给定的 zero_point 为原点，将 x 以 factor 为比例进行放大/缩小
            由于数值计算过程存在截断误差，本函数在同样的 factor,zero_point 配置下进行正向和逆向运算时，仅能保证 1e-2 之前的数值相同。

        必要参数：
            x:              <torch.tensor/np.array>
            factor:         <int/float>
            zero_point:     <int/float>
            reverse:        <boolean> 逆操作

        建议：
            - 对于需要保留更多小数点后精度的情况，建议在输入前先进行一定比例的放大。
    """
```





### utils

- get_function_table_for_array_and_tensor(x)

```python
    """
        根据输入 x 的类型获取对应的 function_table
            目前 function_table 已覆盖的函数有：
                swapaxes(x, dim0, dim1)  交换两个维度
                permute(x, dim_ls)  对维度进行重排

        返回：
            [type], [function_table]
    """
```



对数据的类型、范围进行转换、重整

- convert_dtype(x, target_type)

```python
    """
        转换 dtype 数据类型
            本函数相较于 numpy 或者 pytorch 内置的转换函数，添加了根据类型自动裁剪的步骤，从而能够避免潜在的溢出情况。
            建议使用本函数替代内置的转换函数。

        参数：
            x:          <np.array/torch.tensor>
            dtype:      <string> 转换的目标类型
                            已支持的类型：
                                "float32", "int8", "uint8"
    """
```



- get_crop_by_box(x, box_ls, beg_axis=0)

```python
"""
    根据 boxes/box_ls 选定的区域，将 crop_ls 从源张量 x 中截取出来。

    参数：
        x:              <np.array/tensor>
        box_ls:         <list of box>
                            each box is a np.array with shape [batch_size, 2, dimensions]，各个维度的意义为：
                                2：          box的两个轴对称点
                                dimensions： 坐标的维度
                            要求：
                                - 各个 box 应该是已经 sorted 的，亦即小坐标在前大坐标在后。
                                    例如 box=[[1,2],[0,4]] 是错误的。
                                    而 box=[[0,2],[1,4]] 是合法的。
        beg_axis:       <integer> 上面提供的 boxes 中指定的坐标是从 x/crop 的第几个 axis 开始对应的。
                            例如： beg_axis=1 时，box=[[i,j],[m,n]] 表示该 crop 是从原张量的 x[:, i:m, j:n, ...] 部分截取出来的。

    返回：
        crop_ls:        <list of np.array/tensor>
"""
```



- set_crop_by_box(x, box_ls, crop_ls, beg_axis=0)

```python
"""
    将 crop_ls 填充到 x 中 boxes 指定的区域
        将直接在输入的 x 上进行 inplace 赋值操作

    参数：
        x:              <np.array/tensor>
        box_ls:         <list of box>
                            each box is a np.array with shape [batch_size, 2, dimensions]，各个维度的意义为：
                                2：          box的两个轴对称点
                                dimensions： 坐标的维度
                            要求：
                                - 各个 box 应该是已经 sorted 的，亦即小坐标在前大坐标在后。
                                    例如 box=[[1,2],[0,4]] 是错误的。
                                    而 box=[[0,2],[1,4]] 是合法的。
        crop_ls:        <list of np.array/tensor> 需要与 boxes 一一对应
        beg_axis:       <integer> 上面提供的 boxes 中指定的坐标是从 x/crop 的第几个 axis 开始对应的。
                            例如： beg_axis=1 时，box=[[i,j],[m,n]] 表示该 crop 是从原张量的 x[:, i:m, j:n, ...] 部分截取出来的。

    返回：
        x:              <np.array/tensor>
"""
```



## geometry

空间几何运算

### for_boxes

针对 box 数据结构的算法

【finished 单元测试已完成】

- cal_iou(box_0, box_1)

```python
    """
        计算 box_0 和 box_1 之间的交并比 iou

        参数：
            box_0:          <np.array>
                                shape [2, dimensions]，各个维度的意义为：
                                    2：          box的两个轴对称点
                                    dimensions： 坐标的维度
            box_1:          <np.array>
                                与 box_0 类似。
            return_details: <boolean> 是否以详细信息的形式返回结果
                                默认为 False，此时返回：
                                    iou <float>
                                当设置为 True，将返回一个 dict：
                                    details = dict(
                                        iou=<float>,
                                        intersection=dict(area=<float>, box=<np.array>,),  # area 表示面积
                                        union=dict(area=<float>),
                                        box_0=dict(area=<float>, box=<np.array>,),
                                        box_1=dict(area=<float>, box=<np.array>,),
                                    )
    """
```



- cal_area(boxes, is_sorted=True)

计算体积



- convert_from_coord_to_grid_index(boxes, settings_for_grid, reverse)

```python
    """
        对输入的 boxes，进行 实数坐标 与 网格点序号坐标 之间的坐标转换
            注意：
            - 这种转换可能是可逆的， 实数坐标 ==> 网格点序号坐标 的转换一般会使得 box 的实际范围扩大。
            - 特别地，当使用 grid_coverage_mode=closed 模式，并配合从 boxes 中获取的坐标（可以通过for_boxes.get_ticks()获取）时，
                转换是完全可逆的。
            - 网格点的 index 包头不包尾， beg, end = 0, 1 表示 0 号网格。

        参数：
            boxes:          <3 axis np.array> 需要转换的 box
                                shape [batch_size, 2, dimensions]，各个维度的意义为：
                                    batch_size： 有多少个 box
                                    2：          box的两个轴对称点
                                    dimensions： 坐标的维度
            settings_for_grid:      <dict of paras> 用于设定网格位置、范围的参数列表。
                                目前支持两种格点覆盖模式 mode：
                                    mode:     <string> 格点覆盖模式
                                        支持以下两种模式：
                                            "open"：     开放式，将构建一个覆盖整个空间的格点阵列。
                                            "closed"：   封闭式，仅在指定范围内构建格点阵列。对于超出范围外的坐标，将投影到格点阵列的边界上。
                                在不同的格点覆盖模式 mode 下，有不同的设置方式。
                                目前支持以下三种方式：
                                    mode=open，以 grid_size 为基准
                                        grid_size:      <list/integer/float> 各个维度上网格的大小
                                                            设置为单个 integer 时，默认所有维度使用同一大小的网格划分
                                        offset：         <list/integer/float> 网格点的原点相对于原始坐标的偏移量
                                                            默认为 [0,...]，无偏移
                                                            设置为单个 integer 时，默认所有维度使用同一大小的 offset
                                            例子：
                                                当 grid_size=[1,5] , offset=[3,1]，
                                                表示以 coord=(3,1) 为原点，对维度dim=0以size=1划分网格，对dim=1以size=5划分网格。
                                    mode=closed，以 ticks 为基准
                                        ticks：          <list of np.array> 在各个维度下，网格点的划分坐标
                                                            ticks[i][0] 就是网格的原点坐标，与上面的 offset 相同
                                    mode=closed，以 grid_size 为基准
                                        grid_size:      <list of np.array/list> 在各个维度下，网格点的一系列划分大小
                                        offset：         <list/integer>
                                            函数将会首先把 grid_size 和 offset 转换为对应的 ticks，然后再按照 ticks 执行划分。
            reverse:        <boolean> 决定转换的方向
                                默认为 False，此时为 coord ==> grid_index
                                True 时为 grid_index ==> coord
    """
```



- get_ticks(boxes)

获取 boxes 中涉及到的坐标刻度 ticks



- detect_collision(boxes, complexity_correction_factor_for_aixes_check, duplicate_records)

  ```python
      """
          碰撞检测
              Adapt the entry of different detection functions
              当输入参数中有 boxes 时，调用 detect_collision_inside_boxes() 进行碰撞检测，此时将 boxes 中的每个 box 视为一个 item
              当输入参数中有 boxes_ls 时，调用 detect_collision_among_boxes_ls()，此时将 boxes_ls 中的每个 boxes 视为一个 item
      """
  ```

  - detect_collision_inside_boxes(**kwargs)

    ```python
        """
            基于分离轴定理，对 box（属于凸多边形），进行碰撞检测
                特点：
                    - 时复杂度为 O( N*log(N) + M ) 其中 N 表示 box 的数量，M 表示发生碰撞的 pairs 数量。
                    - 不需要像AABB包围盒和四叉树那样依赖树结构。
                    - 可以配合 for_boxes.convert_from_coord_to_grid_index() 将 boxes 映射到格点阵列内，
                        从而实现多阶段碰撞检测的 Broad-Phase 和 Narrow-Phase。
                注意：
                    - 我们将接触但不重合的情况也视为是碰撞。
    
            基本流程：
                1. 计算各个轴的碰撞概率
                2. 选取碰撞概率最小的轴开始进行 aixes_check
                    （aixes_check 是基于分离轴定理，使用 Sort and Sweep 的方式进行的碰撞粗检测）
                3. 比较后续进行 aixes_check 和 fine_check 的时间成本，选择成本最低的方式进行迭代
                    （fine_check 是对前面碰撞粗检测得到的潜在碰撞 box pairs 进行逐一精细准确的碰撞检测）
    
            参数：
                boxes:          <3 axis np.array> 需要检测的 box
                                    shape [batch_size, 2, dimensions]，各个维度的意义为：
                                        batch_size： 有多少个 box
                                        2：          box的两个轴对称点
                                        dimensions： 坐标的维度
                complexity_correction_factor_for_aixes_check:   <float/integer> 进行 aixes_check 的复杂度修正系数
                                    通过设置该系数，可以调整 aixes_check 与 fine_check 的复杂度比例。
                                    - 该系数越大，计算得到 aixes_check 的复杂度越高，程序对于进行 fine_check 的偏好越大。
                                    - 该系数越小，对进行 aixes_check 的偏好越大。
                                    系数默认为 1.0，建议根据不同设备的实际情况（最好进行测试比较）进行调整。
                duplicate_records:  <boolean> 是否在输出的 collision_groups 的每个 box_id 下都记录一次碰撞。
                                        默认为 False，此时对于每个碰撞对，只会在其中一个 box_id 下的 set 中记录一次。
                                            至于碰撞对的具体分配方式则是随机的，不应作为后续流程依仗的特征。
                                        当设置为 True，则会重复记录。
            输出：
                collision_groups:   <dict of integers set> 检出的碰撞对。
                                    其中的第 i 个 set 记录了 box_id==i 的 box 与其他哪些 box 存在碰撞
                                        比如：  collision_groups[0] = {1, 2} 表示0号 box 与1、2号 box 发生了碰撞
        """
    ```

    

  - detect_collision_among_boxes_ls(**kwargs)

    ```python
        """
            将 boxes_ls 中的每个 boxes 视为一个 item，进行碰撞检测
                本函数是在 detect_collision_between_boxes() 的基础上实现的，具体工作原理请参见该函数。
    
            参数：
                boxes_ls:       <list of boxes/None> 需要检测的 item
                                    each boxes inside the list is an np.array with shape [batch_size, 2, dimensions]
                                    各个维度的意义为：
                                        batch_size： 有多少个 box
                                        2：          box的两个轴对称点
                                        dimensions： 坐标的维度
                                    支持使用 None 作为占位符，标记为 None 的 item 将不与任一其他 item 发生碰撞
                complexity_correction_factor_for_aixes_check:   <float/integer>
                                        参见 detect_collision_between_boxes() 的介绍
                duplicate_records:  <boolean>
                                        参见 detect_collision_between_boxes() 的介绍
            输出：
                collision_groups:   <dict of integers set> 检出的碰撞对。
                                    其中的第 i 个 set 记录了 id==i 的 boxes 表示的 item 与其他哪些 items 存在碰撞
                                        比如：  collision_groups[0] = {1, 2} 表示0号 item 与1、2号 items 发生了碰撞
        """
    ```



- boolean_algebra(boxes_ls, binary_operation_ls, unary_operation_ls)

```python
    """
        布尔运算
            对 boxes_ls 中的各个 boxes，按照 binary_operation_ls、unary_operation_ls 中指定的操作进行布尔运算

        参数：
            boxes_ls:          <list of boxes/None>
                                where boxes is <np.array> with shape [batch, 2, dimensions]
                                各个维度的意义为：
                                    batch：      box的数量
                                    2：          box的两个轴对称点
                                    dimensions： 坐标的维度
                                where None represents the empty set
            binary_operation_ls:    <list of string> 二元运算操作（对两个相邻的 box进行操作）
                                支持以下运算符：
                                    "and":      与
                                    "or":       或
                                    "diff":     减去， a diff b 等效于 a and (not b)
                                注意：
                                    - 因为二元运算符是对两个 box 进行操作的，因此 binary_operation_ls 的长度需要比 boxes_ls 小 1
            unary_operation_ls:     <list> 一元运算符
                                支持以下运算符：
                                    "not":      取反
                                    None:       不进行运算
                                默认为 None，表示不进行任何一元运算
                                注意：
                                    - 当 unary_operation_ls 设定有具体值时，要求其长度与 boxes_ls 相等
                                    - ！！当使用 "not" 运算时，默认使用 boxes_ls 的最小外切长方体作为全集。
                                        如果要指定全集 U 的范围，建议在第一个元素 a 前添加操作 U and a，
                                        该操作将显式地声明全集范围。
        返回：
            boxes 当结果为空集时，返回 None
    """
```





- detect_overlap(boxes_ls)

```python
    """
        在将 boxes_ls 中的每个 boxes 视为一个 item，检测所有 item 之间的重叠区域

        参数：
            boxes_ls:       <3 axis np.array> 需要检测的 item
                                each boxes inside the list is an np.array with shape [batch_size, 2, dimensions]
                                各个维度的意义为：
                                    batch_size： 有多少个 box
                                    2：          box的两个轴对称点
                                    dimensions： 坐标的维度
        输出：
            node_ls:        <list of Node> 由于重叠分割出的不同区域
                                每个区域由一个 node 表示，其中：
                                    node.description["by_item_ids"]["intersection"]     <set of item_id> 这个区域是由哪些 item 相交而成的
                                    node.description["by_item_ids"]["difference"]       <set of item_id> 在上面交集的基础上，应该减去哪些 item
                                    node.description["by_boxes"]                        <boxes> 该区域由哪些 box 组成
                                可见 node.description["by_item_ids"] 描述了该区域的“来源”，
                                node.description["by_boxes"] 描述了该区域的形状。
                注意：
                    - 将排除所有体积为0的区域
                    - node_ls 中除了 item 之间的重叠区域，也记录了各个 item 的独有区域
    """
    
class Node:
    def __init__(self):
        # 用矢量描述
        self.description = dict(
            by_item_ids=dict(
                difference=set(),
                intersection=set(),
            ),
            by_boxes=None,
        )
```





## env_info

与环境的配置、版本有关

- version
  - parse_to_array 将版本的字符串转换为数组的形式
  - compare 在两个版本号之间比较大小



## developing

一些正在开发中的模块，开发完并通过测试后，将整合到其他package下。

- decorator：装饰器
  - restore_original_work_path 装饰器，在运行函数 func 前备份当前工作目录，并在函数运行结束后还原到原始工作目录。
- general_matrix_multiplication 广义通用矩阵乘法操作






[TODO] 使用 Python-Sphinx 构建项目文档

https://www.jianshu.com/p/d4a1347f467b

问题：Python-Sphinx 没有 py-modindex.html

https://stackoverflow.com/questions/13838368/no-generation-of-the-module-index-modindex-when-using-sphinx

https://www.xknote.com/ask/60d40b986d553.html

问题：WARNING: autodoc: failed to import module 'kevin';

https://juejin.cn/post/6882904677373968397

解决：要设置更上一级的目录，Sphinx才能看到下面的  module 'kevin'

https://github.com/sphinx-doc/sphinx/issues/2390

[TODO] 将使用测试用例转为 pytest 测试单元
