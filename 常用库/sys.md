
## 读入命令行参数

```python
import sys

# 获取命令行参数
script_name = sys.argv[0]
arguments = sys.argv[1:]

# 打印脚本名称和参数
print(f"Script Name: {script_name}")
print(f"Arguments: {arguments}")
```