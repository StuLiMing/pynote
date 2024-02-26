argparse 模块用于命令项选项与参数解析。

```python
# test.py
# 导入库
import argparse

# 定义命令行解析器对象。
parser = argparse.ArgumentParser(description='Demo of a argparse')


# 实例化一个命令行解析器对象
args=parser.parse_args()
```

以上 `description` 中的内容是描述信息。可以在命令行通过 `-h` 命令查看。

```sh
python test.py -h
```

输出如下：

```
usage: a.py [-h]

Demo of a argparse

optional arguments:
  -h, --help  show this help message and exit
```

接下来在 `test.py` 的基础上实际添加一些命令行参数。

```python
# test2.py
import argparse

parser = argparse.ArgumentParser(description='Demo of a argparse')

# 添加参数
parser.add_argument('--epochs',type=int,default=30,help="This is epochs")
parser.add_argument('--batch',type=int,default=4,help="This is batch")

args=parser.parse_args()

print(args)

epochs=args.epochs

batch=args.batch

print(f"show {epochs} {batch}")
```

使用命令：
```sh
python test2.py
```

输出如下：
```
Namespace(epochs=30, batch=4)
show 30 4
```

使用命令：
```sh
python test2.py --epochs 100 --batch 10
```

输出如下：
```
Namespace(epochs=100, batch=10)
show 100 10
```

使用命令：
```sh
python test2.py -h
```

输出如下：
```
usage: test2.py [-h] [--epochs EPOCHS] [--batch BATCH]

Demo of a argparse

optional arguments:
  -h, --help       show this help message and exit    
  --epochs EPOCHS  This is epochs
  --batch BATCH    This is batch
```

其他：

```python
parser.add_argument('--if_fog', action='store_true', help="whether to create 'fog' corruptions.")

```
`action='store_true'` 表示，如果在命令行中出现了 `--if_fog` 这个参数，那么相应的变量（在这里是 `args.if_fog`）将被设置为 `True`。这是一种常见的用法，用于启用或禁用某些功能，而不需要显式地写出 `=True` 或 `=False`。

```python
parser.add_argument('--config', default='', metavar='FILE', help='Path to config file')
```

`metavar='FILE'`: 这个参数在帮助信息中用于表示这个参数的值应该是什么类型的。