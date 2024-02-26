---
tags:
  - python
---
## json介绍

json是一种轻量级的数据交互格式。主要功能：在各个编程语言中流通的数据格式，负责不同编程语言中的数据传递和交互。本质上是一个有特殊格式的字符串。

python的列表与字典和json数据格式非常像。

json数据示例：

```json
{"name":"Kangkang","age":18}
```

```json
[{"name":"Kangkang","age":18},{"name":"Maria","age":16},{"name":"Jane","age":15}]
```

## json库的方法

+ `dumps()` 把py数据转为json数据

  ```python
  l=[{"name":"Kangkang","age":18},{"name":"Maria","age":16},{"name":"Jane","age":15}]
  json_str=json.dumps(l)
  print(json_str)
  print(type(json_str))				
  ```

  输出：

  ```python
  [{"name": "\u5eb7\u5eb7", "age": 18}, {"name": "Maria", "age": 16}, {"name": "Jane", "age": 15}]
  <class 'str'>
  ```

  为了使中文正常显示需要加参数 `ensure_ascii`

  ```python
  json_str=json.dumps(l,ensure_ascii=False)
  ```

+ `loads()` 把json数据转为py数据

  ```python
  json_str='[{"name":"Kangkang","age":18},{"name":"Maria","age":16},{"name":"Jane","age":15}]'
  l=json.loads(json_str)
  print(l)
  print(type(l))
  ```

  输出：

  ```python
  [{'name': 'Kangkang', 'age': 18}, {'name': 'Maria', 'age': 16}, {'name': 'Jane', 'age': 15}]
  <class 'list'>
  ```

  

