import os
import time
import importlib.util
from kevin.developing.decorator import restore_original_work_path

if importlib.util.find_spec("cPickle") is not None:
    # 如果安装有 cPickle，可以更快处理串行化
    import cPickle as pickle
else:
    import pickle


class Cache_Manager_for_Iterator:
    """
        适用于迭代器/生成器的缓存管理器
            通过构建基于磁盘的缓存（首先迭代读取迭代器/生成器的内容，并将这些块 chunk 分别保存为二进制文件）
            以及基于内存的缓存（然后在内存中开辟出一个缓存列表空间，用于保存最常调用的 chunk）
            来加速 迭代器/生成器 内容的读取

        工作流程：
            首先构建基于磁盘的缓存，将分块读取到数据保存为二进制文件；
                相关变量：
                    iterator:       迭代器/生成器
                    folder_path:    保存二进制文件的路径
                                        默认保存在 ./temp/cache_name/ 下
                                        当给定的 folder_path 内容不为空时，将尝试直接构建 file_dict
                    file_dict:      二进制文件的文件名与序号的对应关系表
                                        例如：{ 0: "0.pkl", 1: "1.pkl", 2: "2.pkl", ...}
                                        其中 index 0 对应于文件 ./temp/cache_name/0.pkl
            然后在进行读取时，将先到 cache 中寻找是否已经有需要的 chunk 分块，如果没有则到前面 file_dict 中读取，同时更新 cache
                相关变量：
                    cache_dict：     缓存
                                        例如：{ 1: chunk_var_1, 3: chunk_var_3 }
                                        其中 key 是 chunk 分块的 index，value 是对应的保存在内存中的变量
                    cache_metadata:  缓存的属性数据
                                        包含以下字段，各字段将自动更新
                                        例如：{ 1: {  "last_time": xxx,      # 最近读取时间
                                                     "initial_time": xxx,   # 最初读取时间
                                                     "counts": xxx,         # 读取次数
                                                     },
                                               ... }
                    cache_update_strategy：缓存更新策略
                                        是一个函数，该函数的输入是 cache_metadata ，输出是需要删除的缓存的序号
                                        触发：
                                            在每次出现 cache_dict 无法命中，导致有新的 cache 添加到 cache_dict 时，将会采用该策略进行更新
                                        现有策略：
                                            drop_min_counts:    去除读取次数最小的
                                            drop_min_last_time:    去除最近没有读取的
                                            drop_min_survival_time:    去除生存时间最短的，生成时间 survival_time:=last_time-initial_time
                                        默认使用 drop_min_last_time
                    （cache_dict 的大小受 cache_update_strategy 中的 cache_size 限制，当大小超过限制时，
                    将根据 cache_update_strategy 去除优先级较低的部分来更新缓存）

        支持以下几种方式来：
            以迭代器的形式进行顺序读取
            以指定序号的形式进行随机读取
    """

    def __init__(self, **kwargs):
        """
            设定关键参数
            参数：
                iterator:       迭代器/生成器
                folder_path:    保存二进制文件的路径
                cache_update_strategy：缓存更新策略
            其他参数：
                strict_mode:    禁止同时设置 iterator 和给定一个非空的 folder_path
                                    默认为 True 开启，此时同时设置将报错。
                                    当设置为 False 时，同时设置将以 folder_path 中的二进制文件为准
                del_cache_when_exit:    退出时删除生成的缓存二进制文件
                                    只有在设置了 iterator 的前提下，才会触发。
                                    （对于非本实例生成的文件，比如只给定了非空的 folder_path，不做删除。）
                                    默认为 True 开启。
        """

        # 默认参数
        paras = {
            "iterator": None,
            "folder_path": None,
            "cache_update_strategy": None,
            #
            "strict_mode": True,
            "del_cache_when_exit": True,
        }

        # 获取参数
        paras.update(kwargs)

        # 校验参数
        # cache_update_strategy
        if paras["cache_update_strategy"] is None:
            paras["cache_update_strategy"] = lambda x: Strategies.drop_min_last_time(cache_metadata=x,
                                                                                     cache_size_upper_bound=10)
        # 同时非空
        b_folder_not_empty = isinstance(paras["folder_path"], (str,)) and paras[
            "folder_path"] is not None and os.path.exists(paras["folder_path"]) and len(
            os.listdir(paras["folder_path"])) > 0
        if paras["iterator"] is not None and b_folder_not_empty:
            # iterator 非空，folder_path 非空
            if paras["strict_mode"]:
                # 不能同时设置
                raise Exception(f"Error: folder_path and iterator cannot be set at the same time\n"
                                f"iterator {paras['iterator']} is given when "
                                f"there is already content in folder_path {paras['folder_path']}!")
            else:
                # 以 folder_path 为准
                paras["iterator"] = None
        # 同时为空
        if paras["iterator"] is None and paras["folder_path"] is None:
            raise Exception(f"Error: folder_path and iterator cannot be empty at the same time\n"
                            f"both iterator and folder_path are not given!")

        # 构建基于磁盘的缓存
        file_dict = dict()
        if paras["iterator"] is not None:
            # 根据 iterator 生成
            if paras["folder_path"] is None:
                paras["folder_path"] = os.path.join(os.getcwd(), "temp", str(time.time()))
            if not os.path.exists(paras["folder_path"]):
                os.makedirs(paras["folder_path"])
            file_dict = self.generate_chuck_files(paras["iterator"], paras["folder_path"])
        elif b_folder_not_empty:
            # 尝试直接根据已有文件构建 file_dict
            file_dict = self.find_chuck_files(paras["folder_path"])

        self.file_dict = file_dict
        self.paras = paras

        # 初始化基于内存的缓存
        self.cache_dict = dict()
        self.cache_metadata = dict()

        # 记录最后读取的index
        self.index = -1

    # ------------------------------------ 基于磁盘的缓存 ------------------------------------ #

    @staticmethod
    @restore_original_work_path
    def generate_chuck_files(iterator, folder_path):
        """
            构建基于磁盘的缓存
                将 iterator 每次迭代产生的结果以二进制文件的形式（文件名为 {index}.pkl）保存到 folder_path 指向的目录中，
                并将这些文件名保存到索引 file_dict
        """
        os.chdir(folder_path)
        file_dict = dict()
        for i, chuck in enumerate(iterator):
            file_name = f"{i}.pkl"
            with open(file_name, 'wb') as f:
                pickle.dump(chuck, f)
            file_dict[i] = file_name
        return file_dict

    @staticmethod
    @restore_original_work_path
    def find_chuck_files(folder_path):
        """
            建立到磁盘缓存的索引
                从 folder_path 中找到已有的二进制文件，并将这些文件名保存到索引 file_dict
        """
        os.chdir(folder_path)
        file_dict = dict()
        count = 0
        while True:
            file_name = f"{count}.pkl"
            if os.path.isfile(file_name):
                file_dict[count] = file_name
            else:
                break
            count += 1
        return file_dict

    def __read_from_files(self, index):
        """
            从磁盘中读取
                根据 index 到索引 file_dict 中找出对应的文件名，然后读取文件
        """
        file_path = os.path.join(self.paras["folder_path"], self.file_dict[index])
        with open(file_path, 'rb') as f:
            chunk = pickle.load(f)
        return chunk

    # ------------------------------------ 基于内存的缓存 ------------------------------------ #

    def __read_from_cache(self, index):
        """
            从内存中读取
        """
        chunk = self.cache_dict[index]
        # 更新缓存属性
        self.cache_metadata[index]["counts"] += 1
        self.cache_metadata[index]["last_time"] = time.time()
        return chunk

    def __add_to_cache(self, index, chunk):
        """
            添加到内存中
        """
        # 更新缓存
        self.cache_dict[index] = chunk
        # 更新缓存属性
        self.cache_metadata[index] = {
            "last_time": time.time(),  # 最近读取时间
            "initial_time": time.time(),  # 最初读取时间
            "counts": 1,  # 读取次数
        }
        # 依据策略去除优先级较低的缓存
        drop_ls = self.paras["cache_update_strategy"](self.cache_metadata)
        for i in drop_ls:
            self.cache_dict.pop(i)
            self.cache_metadata.pop(i)

    # ------------------------------------ 读取 ------------------------------------ #

    def read(self, index):
        assert 0 <= index < len(self), \
            KeyError(f"Error: index {index} not in [0, {len(self)})")
        if index in self.cache_dict:
            # 直接从内存中读取
            chunk = self.__read_from_cache(index)
        else:
            # 到磁盘读取
            chunk = self.__read_from_files(index)
            # 添加到缓存
            self.__add_to_cache(index, chunk)
        self.index = index
        return chunk

    # ------------------------------------ 其他 ------------------------------------ #

    # 迭代器，通过 next(self) 调用
    def __next__(self):
        if self.index < len(self) - 1:
            return self.read(self.index + 1)
        else:
            self.index = -1
            raise StopIteration

    # 支持 for 循环调用
    def __iter__(self):
        return self

    # 通过 len(self) 调用
    def __len__(self):
        return len(self.file_dict)

    def __del__(self):
        if self.paras["iterator"] is not None and self.paras["del_cache_when_exit"] and self.paras["strict_mode"]:
            # 在 strict_mode 开启，且 iterator 非空的情况下 self.file_dict 中的二进制文件一定是根据 iterator 生成的
            # 删除文件
            pwd_bak = os.getcwd()
            os.chdir(self.paras["folder_path"])
            for key, value in self.file_dict.items():
                os.remove(value)
            os.chdir(pwd_bak)
            # 删除空文件夹
            if not os.listdir(self.paras["folder_path"]):
                os.removedirs(self.paras["folder_path"])


class Strategies:
    """
        现有策略：
                drop_min_counts:    去除读取次数最小的
                drop_min_last_time:    去除最近没有读取的
                drop_min_survival_time:    去除生存时间最短的，生成时间 survival_time:=last_time-initial_time
    """

    @staticmethod
    def drop_min_counts(cache_metadata, cache_size_upper_bound, cache_size_after_drop=None):
        """
            去除读取次数最小的
            参数：
                cache_metadata:  缓存的属性数据
                                    包含以下字段，各字段将自动更新
                                    例如：{ 1: {  "last_time": xxx,      # 最近读取时间
                                                 "initial_time": xxx,   # 最初读取时间
                                                 "counts": xxx,         # 读取次数
                                                 },
                                           ... }
                cache_size_upper_bound： 当 cache_metadata 的大小超过该值时触发更新
                cache_size_after_drop：  更新后 cache_metadata 的目标大小
                                    默认为 cache_size_upper_bound
        """
        if cache_size_upper_bound >= len(cache_metadata):
            return []

        cache_size_after_drop = cache_size_upper_bound if cache_size_after_drop is None else cache_size_after_drop
        # （这里其实可以用最大堆来优化，但是我懒啊）
        drop_ls = [i for i, j in sorted(cache_metadata.items(), key=lambda x: x[1]["counts"])[:-cache_size_after_drop]]
        return drop_ls

    @staticmethod
    def drop_min_last_time(cache_metadata, cache_size_upper_bound, cache_size_after_drop=None):
        """
            去除最近没有读取的
        """
        if cache_size_upper_bound >= len(cache_metadata):
            return []

        cache_size_after_drop = cache_size_upper_bound if cache_size_after_drop is None else cache_size_after_drop
        drop_ls = [i for i, j in
                   sorted(cache_metadata.items(), key=lambda x: x[1]["last_time"])[:-cache_size_after_drop]]
        return drop_ls

    @staticmethod
    def drop_min_survival_time(cache_metadata, cache_size_upper_bound, cache_size_after_drop=None):
        """
            去除生存时间最短的，生成时间 survival_time:=last_time-initial_time
        """
        if cache_size_upper_bound >= len(cache_metadata):
            return []

        cache_size_after_drop = cache_size_upper_bound if cache_size_after_drop is None else cache_size_after_drop
        drop_ls = [i for i, j in sorted(cache_metadata.items(), key=lambda x: x[1]["last_time"] - x[1]["initial_time"])[
                                 :-cache_size_after_drop]]
        return drop_ls


if __name__ == '__main__':
    "测试 Strategies"
    _cache_metadata = {
        1: {
            "last_time": 123,
            "initial_time": 56,
            "counts": 2,
        },
        2: {
            "last_time": 110,
            "initial_time": 0,
            "counts": 4,
        },
        3: {
            "last_time": 126,
            "initial_time": 121,
            "counts": 1,
        },
    }

    print(Strategies.drop_min_counts(_cache_metadata, 2))
    print(Strategies.drop_min_last_time(_cache_metadata, 1))
    print(Strategies.drop_min_survival_time(_cache_metadata, 1))

    "测试 Cache_Manager_for_Iterator"
    cache_manager = Cache_Manager_for_Iterator(iterator=range(10),
                                               del_cache_when_exit=True,
                                               cache_update_strategy=lambda x: Strategies.drop_min_last_time(
                                                   cache_metadata=x,
                                                   cache_size_upper_bound=3))
    print(cache_manager.file_dict)
    print(cache_manager.cache_metadata)
    for i in range(3):
        print(cache_manager.read(0))
    for i in range(2):
        print(cache_manager.read(3))
    for i in range(1):
        print(cache_manager.read(6))
    for i in range(4):
        print(cache_manager.read(9))
    print(cache_manager.cache_metadata)
