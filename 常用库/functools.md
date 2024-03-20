## partial

`partial`函数用于从一个函数创建一个新的函数，同时预先设定好一些参数。

```python
from functools import partial

def add(a,b):
    return a+b

add1=partial(add,a=1)
add1(b=2)
```

注意这里调用 `add1()` 时必须写 `add1(b=2)` 二不能写 `add1(2)` 了。