from setuptools import setup, find_packages

setup(
    name="kevin_toolbox",
    version="0.2.4",
    author="kevin hsu",
    author_email="xukaiming1996@163.com",
    description="一个常用的工具代码包集合",
    # 项目主页
    url="https://github.com/cantbeblank96/kevin_toolbox",
    #
    classifiers=[
        # 许可证信息
        'License :: OSI Approved :: MIT License',
        # 目标 Python 版本
        'Programming Language :: Python :: 3',
    ],

    #
    packages=find_packages(),

    # # 默认只添加 .py 文件，如果需要添加其他文件则需要令 include_package_data 为 True
    # include_package_data=True,
    # # 需要添加的额外文件列表，比如这里就表示将添加 images/raw 下的所有 .png 文件和 images/2k 下的所有 .jpg 文件
    # package_data={
    #     "images": ['raw/*.png', '2k/*.jpg'],
    # },
    # # 需要排除的文件
    # exclude_package_data={
    #     "images": ['raw/233.png'],
    # },

    # 依赖的python版本
    python_requires='>=3.6',

    # 表明当前模块依赖哪些包，若环境中没有，则会从pypi中下载安装
    install_requires=[
        'torch>=1.10.0',
        'numpy>=1.20.0',
    ],

    # 仅在测试时需要使用的依赖，在正常发布的代码中是没有用的。
    # 在执行python setup.py test时，可以自动安装这三个库，确保测试的正常运行。
    tests_require=[
        'pytest>=6.2.5',
        'line-profiler>=3.5',
    ],
)
