# Python Note

## Python 语法相关

#### 双星操作符

-  ** double star Operator，**kwargs

- 方式1：用于调用函数时展开dict作为输入的变量，注意此时该dict的定义中需要有对应函数的输入变量名

  ```python
  def my_function(a, b, c):
      print(f"a = {a}, b = {b}, c = {c}")
  
  # Create a dictionary
  my_dict = {"a": 1, "b": 2, "c": 3}
  
  # Unpack the dictionary using the double star operator
  my_function(**my_dict)
  ```

  - Output:

    ```python
    a = 1, b = 2, c = 3
    ```

- 方式2：为一个函数定义随意的输入变量

  ```python
  def my_function(**kwargs):
      print(kwargs)
  
  my_function(a=1, b=2, c=3)
  ```

  - Output:

    ```python
    {'a': 1, 'b': 2, 'c': 3}
    ```

    





## Python 开发相关

### VSCode + Python

- Black Formatter 自动排版

  - setting 中的操作
    - Editor: Default Formatter
      - Black Formatter
    - Editor: Format On Save
      - on
  - 下方控制条中的 Python 版本，选择与命令行对应的env版本

    - env中也需要安装black

    - ```
      pip install black
      ```

  - black 目前只支持 3.8 以上
    - Black-formatter: Interpreter 选项中加入 py3.8 以上的环境



- isort

  - `~/.config/Code/User/settings.json` 添加以下内容，保存时自动排序import

    ```json
    "editor.codeActionsOnSave": {
        "source.organizeImports": "explicit"
    }
    ```

- pylint





### Jupyter Notebook

- 安装

  ```
  pip install Jupyter
  
  # 生成配置文件
  jupyter notebook --generate-config
  
  # 配置密码
  jupyter notebook password
  ```



- 运行

  ```bash
  # 启动 Jupyter notebook
  jupyter notebook --no-browser --port=8889 --ip=127.0.0.1
  
  # 复制输出的URL到浏览器，就可以打开Jupyter窗口
  ```

  







### Conda

- conda 环境相关

  ```python
  # 创建环境，指定对应python版本
  conda create -n depth_anything python=3.12
  
  # 激活环境
  conda activate depth_anything
  
  # 停用环境
  conda deactivate depth_anything
  
  # 删除环境，包括所有package
  conda remove --name depth_anything --all
  
  # 查看当前所有环境
  conda env list
  ```

- conda channels 相关

  ```shell
  # 显示 channels
  conda config --show channels
  
  # 添加 channels
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  
  # 删除 channels
  conda config --remove channels  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  
  ```

- conda 更新自己

  ```
  conda update -n base conda
  ```

- 显示所有包名

  ```python
  conda list
  ```

- conda vs pip

  - **先使用 Conda 再使用 pip**

    - 使用 Conda 安装尽可能多的需求，然后使用 pip

    - 使用 pip 安装时 –-upgrade-strategy 参数应当设置为 only-if-needed（默认）

    - 不要将 pip 与 –-user 参数一起使用，避免为所有用户安装

  - **使用 conda 环境进行隔离**

    - 创建一个新的 conda 环境来隔离 pip 所做的任何更改

    - 由于硬链接特性，环境占用的空间很小

    - 应注意避免在默认的 conda 环境下运行 pip

  - 如果需要更改，请重新创建环境

    - 一旦使用 pip，conda 将不知道这些变化

    - 要安装其他 Conda 软件包，最好重新创建环境

  - 将 conda 和 pip 要求存储在文本文件中

    - 包要求可以通过 --file [参数传递](https://www.zhihu.com/search?q=参数传递&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"3188449994"})给 conda

    - pip 接受带有 -r 或 --requirement 的 [Python](https://www.zhihu.com/search?q=Python&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"3188449994"}) 包列表

    - conda env 能够根据 conda 和 pip 的包需求文件导出或创建环境

  

## Python 基础包

### argparse

- 命令行变量解析工具

- demo01:

  ```python
  import argparse
  
  def calculate_area(length, width):
      return length * width
  
  if __name__ == "__main__":
      # Create the parser
      parser = argparse.ArgumentParser(description='Calculate the area of a rectangle.')
  
      # Add arguments
      parser.add_argument('--length', type=int, required=True, help='The length of the rectangle.')
      parser.add_argument('--width', type=int, required=True, help='The width of the rectangle.')
  
      # Parse the arguments
      args = parser.parse_args()
  
      # Calculate the area
      area = calculate_area(args.length, args.width)
      print(f"The area of the rectangle is: {area} square units.")
  ```

  

### glob

- 遍历一个地址下面的文件和文件夹

  ```python
  import glob
  
  # Find all files in the current directory with the .txt extension
  txt_files = glob.glob("*.txt")
  print(txt_files)
  # Output: ['file1.txt', 'file2.txt', 'file3.txt']
  
  # Find all directories in the current directory
  dirs = glob.glob("*/")
  print(dirs)
  # Output: ['dir1/', 'dir2/', 'dir3/']
  
  # Find all files in the "data" directory with the .csv extension
  csv_files = glob.glob("data/*.csv")
  print(csv_files)
  # Output: ['data/file1.csv', 'data/file2.csv', 'data/file3.csv']
  
  # Find all files in the "data" directory and its subdirectories with the .jpg extension
  jpg_files = glob.glob("data/**/*.jpg", recursive=True)
  print(jpg_files)
  # Output: ['data/subdir1/image1.jpg', 'data/subdir2/image2.jpg', 'data/subdir3/image3.jpg']
  ```

  