创建两个线程，分别执行函数 `eyekeyboard` 和 `terminal`

```python
# 监视键盘
keyboard_thread = threading.Thread(target=eyekeyboard,daemon=True)
keyboard_thread.start()


# 终端
terminal_thread = threading.Thread(target=terminal)
terminal_thread.start()
```

这里参数 `daemon=True` 意思是将这个线程设置为**守护线程**。守护线程会在主线程结束时自动结束。