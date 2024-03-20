## setuptools

用于打包和分发Python项目

## setup

用于安装包

```python
from setuptools import setup

setup(
    name="ddpm",
    py_modules=["ddpm"],
    install_requires=["torch", "torchvision", "einops", "wandb", "joblib"],
)
```

用法：在包含该脚本的目录下运行 `pip install .`