
## Path

类，表示路径。

`Path(output_folder).mkdir(parents=True, exist_ok=True)`，创建目录 `output_folder`。

- `parents=True`: 如果父目录不存在，也要创建父目录。如果设置为`True`，它将递归地创建所有必要的父目录，以确保目标路径存在。这对于创建多层嵌套的目录非常有用。
- `exist_ok=True`: 如果设置为`True`，即使目录已经存在，也不会引发异常。这是为了防止在目录已经存在的情况下引发错误。
``