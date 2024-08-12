# Python Note

## Python 函数相关

##### range

- Syntax: range(start, stop, step)

  Parameter :

  start: [ optional ] start value of the sequence
  stop: next value after the end value of the sequence
  step: [ optional ] integer value, denoting the difference between any two numbers in the sequence
  Return : Returns an object that represents a sequence of numbers

```python
for i in range(0, 10, 2):
    print(i, end=" ")
print()

'''
0 2 4 6 8
'''

# incremented by -2
for i in range(25, 2, -2):
    print(i, end=" ")
print()

'''
25 23 21 19 17 15 13 11 9 7 5 3 
'''
```











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

    





## Python 开发辅助

### VSCode + Python

- Black Formatter 自动排版

  - setting 中的操作
    - Editor: Default Formatter
      - **必须设置为null, 不能选择 black**
    - Editor: Format On Save
      - on
    
  - 下方控制条中的 Python 版本，选择与命令行对应的env版本
  
    - env中也需要安装black
  
        ```
        pip install black
        ```
  
    - 外部的环境中需要卸载 black
  
      ```
      pip uninstall black
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

  

## Python 基础功能包

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

  

### tqdm

1. **简介**
   `tqdm` 是一个 Python 库,用于向控制台或 Jupyter Notebook 中添加进度条。它可以让你轻松地为任何可迭代对象(如列表、范围或自定义迭代器)添加进度显示。
2. **主要特性**

- **进度条显示**: `tqdm` 主要功能是在任何迭代过程中显示进度条,进度条会显示完成百分比、总项目数和已用时间。
- **嵌套进度条**: `tqdm` 支持嵌套进度条,这在有复杂工作流程和多个子任务时非常有用。
- **自定义**: 你可以根据需要自定义进度条的外观,如宽度、颜色和格式。
- **Jupyter Notebook 支持**: `tqdm` 有针对 Jupyter Notebook 的优化,可以在笔记本中流畅地显示进度条。
- **兼容性**: `tqdm` 支持 Python 2 和 Python 3,并且可以在各种 Python 版本中使用。



**循环迭代**

```python
from tqdm import tqdm

for i in tqdm(range(1000), desc="Processing items"):
    # 执行某些操作
    pass
```

在这个例子中,`tqdm` 函数用于包装 `range(1000)` 迭代器,`desc` 参数用于设置进度条的描述。

**处理文件**

```python
from tqdm import tqdm

with open("large_file.txt", "r") as f:
    for line in tqdm(f, desc="Reading file", unit="lines"):
        # 处理每一行
        pass
```

这个例子展示了如何在处理大文件时使用 `tqdm` 来显示读取进度,`unit` 参数用于设置进度单位为"行"。

**嵌套进度条**

```python
from tqdm import tqdm

outer_iterable = range(10)
inner_iterable = range(1000)

with tqdm(outer_iterable, desc="Outer Loop") as outer:
    for _ in outer:
        with tqdm(inner_iterable, desc="Inner Loop", leave=False, position=0) as inner:
            for _ in inner:
                # 执行某些操作
                pass
```

在这个例子中,我们使用嵌套的进度条来显示外层循环和内层循环的进度。`leave=False` 确保内层进度条在循环结束时被清除,`position=0` 确保进度条显示在同一行。



## Python 数据功能包

### Numpy

#### np.max() & np.argmax()

1. **`np.max()`**:
   - 功能: 返回数组中的最大值。
   - 语法: `np.max(a, axis=None, out=None, keepdims=False)`
   - 参数:
     - `a`: 输入数组。
     - `axis`: 沿着该轴找最大值。如果不指定,则返回数组中的最大值。
     - `out`: 存储结果的输出数组。
     - `keepdims`: 如果为 True,则结果数组的维度保持不变。
   - 返回值: 数组中的最大值。
2. **`np.argmax()`**:
   - 功能: 返回数组中最大值的索引。
   - 语法: `np.argmax(a, axis=None, out=None)`
   - 参数:
     - `a`: 输入数组。
     - `axis`: 沿着该轴找最大值的索引。如果不指定,则返回数组中最大值的一维索引。
     - `out`: 存储结果的输出数组。
   - 返回值: 数组中最大值的索引。

```python
import numpy as np

# 创建一个 2D 数组
arr = np.array([[1, 5, 2], [4, 3, 6]])

# 获取数组中的最大值
max_value = np.max(arr)
print("最大值:", max_value)  # 输出: 最大值: 6

# 获取最大值的位置索引
max_index = np.argmax(arr)
print("最大值的索引:", max_index)  # 输出: 最大值的索引: 5

# 如果需要获取 2D 数组中最大值的行列索引
row_index, col_index = np.unravel_index(max_index, arr.shape)
print("最大值的行列索引:", row_index, col_index)  # 输出: 最大值的行列索引: 1 2
```



### collections

#### Counter:

- 这是`dict`类的子类,提供了计数hashable对象的便捷方法。

- 可以用来统计列表中元素的出现频率。

- 示例:

  ```python
  from collections import Counter
  print(Counter(['a', 'b', 'c', 'a', 'b', 'b']))
  # 输出: Counter({'b': 3, 'a': 2, 'c': 1})
  ```

#### defaultdict:

- 这也是`dict`类的子类,提供了缺失键的默认值。

- 当你想初始化一个字典,并给新键一个特定的默认值时很有用。

- 示例:

  ```python
  from collections import defaultdict
  d = defaultdict(int)
  d['a'] += 1
  d['b'] += 2
  print(d)
  # 输出: defaultdict(<class 'int'>, {'a': 1, 'b': 2})
  ```

#### OrderedDict:

- 这也是`dict`类的子类,记住了键首次插入的顺序。

- 当你需要保持字典中元素的顺序时很有用。

- 示例:

  ```python
  from collections import OrderedDict
  od = OrderedDict()
  od['a'] = 1
  od['b'] = 2
  od['c'] = 3
  print(od)
  # 输出: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
  ```

#### namedtuple:

- 这是一个工厂函数,创建一个带有命名字段的新的元组子类。

- 当你需要创建轻量级的对象类似结构,而不需要定义一个完整的类时很有用。

- 示例:

  ```python
  from collections import namedtuple
  Point = namedtuple('Point', ['x', 'y'])
  p = Point(x=1, y=2)
  print(p.x, p.y)
  # 输出: 1 2
  ```



#### deque

1. **创建deque**

   ```python
   from collections import deque
   d = deque()
   ```

2. **在两端添加元素**

   ```python
   d.append(1)
   d.appendleft(2)
   print(d)  # Output: deque([2, 1])
   ```

3. **在两端删除元素**

   ```python
   d.pop()   # Removes and returns 1
   d.popleft()  # Removes and returns 2
   print(d)  # Output: deque([])
   ```

4. **设置最大长度**

   ```python
   d = deque(maxlen=3)
   d.append(1)
   d.append(2)
   d.append(3)
   d.append(4)
   print(d)  # Output: deque([2, 3, 4], maxlen=3)
   ```

   当deque达到最大长度时,新添加的元素会自动挤掉最早添加的元素。

5. **迭代deque**

   ```python
   for item in d:
       print(item)
   ```

6. **将deque转换为其他数据结构**

   ```python
   list(d)
   tuple(d)
   ```

`deque`的一些常见用途包括:

- 实现先进先出(FIFO)队列
- 在两端进行高效的插入和删除操作
- 在固定大小的窗口内保存数据,如最近的N个元素

总的来说,`collections.deque`是一个非常灵活和高效的数据结构,在需要频繁在两端添加或删除元素的场景中非常有用。