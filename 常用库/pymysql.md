
## 连接到数据库

```python
db=pymysql.connect(
		# 主机名
        host='localhost',
		# 端口
        port=3306,
		# 用户名
        user='root',
		# 密码
        password='password',
		# 数据库
        database='eng_zn_dictionary',
		# 自动 commit
        autocommit=True,
    )
cursor = db.cursor()
```

## 执行

```python
cursor.execute("SELECT * FROM your_table")
```

如果不置 `autocommit=True`，每执行一句 `SQL` 语句后要执行一句 `db.commit()`

## 获取结果

```python
results = cursor.fetchall()
```

## 回滚

```python
try:
    # 执行 SQL 语句
    cursor.execute(sql)
    # 提交到数据库执行
    conn.commit()
except:
    # 发生错误时回滚
    conn.rollback()

```

## 关闭

```python
cursor.close()
```
