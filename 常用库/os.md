# 路径的表示

在 MacOS 和 Linux 系统下，路径默认使用的都是正斜杠'/'，在Windows系统下，正反斜杠都可以表示路径分隔符，默认的是反斜杠 '\\'。

当前路径的初始值并不是脚本代码所在路径，而是 `VScode` 等 IDE 当前打开的文件夹。
## os常用基本方法

| 方法                           | 功能                    |
| ---------------------------- | --------------------- |
| os.getcwd()                  | 获取Python当前的工作路径       |
| os.chdir(folderpath)         | 将当前工作文件夹改为path        |
| os.rename(old_path,new_path) | 重命名                   |
| os.remove(filepath)          | 删除文件                  |
| os.mkdir(folderpath)         | 创建文件夹（如果path已存在会抛出错误） |
| os.rmdir(folderpath)         | 删除空文件夹（如果path非空会抛出错误） |
| os.listdir(folderpath)       | 遍历文件夹下所有文件            |
| os.path.join(path1,path2 )   | 拼接两个路径                |

## os.walk()

假如目录结构如下：

```
--a
  --b
	test.py
  --c
```

```python
import os

for root,dirs,files in os.walk("./"):
    print(root,dirs,files)

```

输出：

```
./ ['b', 'c'] []
./b [] ['test.py']
./c [] []
```

也就是说，`os.walk` 会遍历当前目录下的所有目录（包括当前目录），每次取出一个目录赋值给 `root`，将这个目录下的目录作为一个列表赋值给 `dirs`，将这个目录下的文件作为一个列表赋值给 `files`。






## path下的方法

+ os.path.exists(path)：检查文件或文件夹是否存在
+ os.path.isdir(path)：检查path是否是一个文件夹
+ os.path.basename(path)：返回一个路径的的最后一层