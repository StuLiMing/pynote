1. `time()` 

   获取当前时间戳（浮点数），单位是秒。

   计算机的时间戳通常是从一个特定的起始点开始计时，这个起始点被称为"Unix纪元"或"UNIX Epoch"。

   Unix纪元的起始点是：

   **时间：** 1970年1月1日，协调世界时（Coordinated Universal Time，UTC）的午夜（00:00:00 UTC）。

2. `time_ns()`

   获取当前时间戳（浮点数），单位是纳秒。

3. `ctime()`

   获取当前时间并以易读的方式表示（字符串）。

   ```python
   print(ctime())			# Sat Aug 19 17:21:13 2023
   ```

   `ctime(secs)` 会把时间戳secs转为易读的字符串。

4. `gmtime()`

   获取当前时间并以计算机易处理的格外返回（struct_time）。

   ```python
   print(gmtime())			
   # time.struct_time(tm_year=2023, tm_mon=8, tm_mday=19, tm_hour=9, tm_min=25, tm_sec=13, tm_wday=5, tm_yday=231, tm_isdst=0)
   ```

   + 这里调用这个语句的时候是17：25 ，tm_hour不是17而是9因为返回的是UTC，我所在的地方是东八区，要加8。

   + `tm_wday=5` 是说此时是一周的第6天，也就是星期六（从0开始计）

     `tm_yday=231` 是说此时是一年的第231天，这个是从1开始计。

     `tm_isdst=0` 说明这个时间不是夏令时。如果 `tm_isdst` 的值为 `-1`，则表示不可用或未知的夏令时信息。这种情况可能发生在操作系统或编程库无法确定夏令时状态的情况下。

   + `gtime(secs)` 会把时间戳secs转为 time_struct 格式。

5. `localtime()`

   基本同上，除了返回的是本地时间。

6. `strptime(string,format)`

   将string按format的规则解析，返回一个 struct_time

   ```python
   timeStr= '2023-8-19 17:37:44'
   print(strptime(timeStr, "%Y-%m-%d %H:%M:%S"))
   # time.struct_time(tm_year=2023, tm_mon=8, tm_mday=19, tm_hour=17, tm_min=37, tm_sec=44, tm_wday=5, tm_yday=231, tm_isdst=-1)
   ```

7. `strftime(format,t)`

   将 struct_time 类型的 t 按format解析，返回一个字符串。

   ```python
   print(strftime("%Y-%m-%d %H:%M:%S",gmtime()))
   # 2023-08-19 09:39:42
   ```

   格式化表示时间的字符串用到的占位符：

   | 占位符 | 意义          | 范围             |
   | ------ | ------------- | ---------------- |
   | %Y     | 年份          | 0000~9999        |
   | %m     | 月份          | 01~12            |
   | %B     | 月份          | January~December |
   | %b     | 月份          | Jan~Dec          |
   | %A     | 星期          | Monday~Sunday    |
   | %a     | 星期          | Mon~Sun          |
   | %H     | 小时（24h制） | 00~23            |
   | %I     | 小时（12h制） | 01~12            |
   | %p     | 上/下午       | {AM,PM}          |
   | %M     | 分钟          | 00~59            |
   | %S     | 秒钟          | 00~59            |

8. `sleep(secs)`

   程序休眠 secs 秒（浮点数）

9. `perf_counter()`

   返回一个CPU级别的精确时间计数值，单位为秒。这个计数值起点不确定，两次调用求差值才有意义。

10. `perf_counter_ns()`

    同上，但单位是纳秒。