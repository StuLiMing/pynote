+ 假设已经 `import socket` 。
+ addr 的格式是 `(ip,port)` 或 `(hostname,port)` ，它是一个元组。
# 创建socket
```python
sk=socket(family,type)
```
family 取值：AF_INET(IPv4)、DF_INET6(IPv6)
type 取值：SOCK_STREAM（TCP协议）、SOCK_DGRAM（UDP协议）

# connect
```python
sk.connect(addr)
```
连接到一个远程的 socket。

# bind
```python
sk.bind(addr)
```
将 sk 绑定到一个地址。

# listen(backlog)
监听，使得服务器能够接收客户端连接。 backlog 是连接的最大数量。

# accept
```python
con_sk,addr=sk.accept()
```
等待接受一个连接。前提是 socket 必须已经绑定了一个地址。等待是阻塞式的。连接建立成功后返回元组 `(connectionsocket,addr)`，分别是新的 socket 对象和远端主机的地址。
# send
```python
sk.send(bytes)
```
该 socket 发送数据 bytes。发送前 sk 必须已经 connect 到目的地址。
# sendto
```python
sk.sendto(bytes,addr)
```
该 socket 向 addr 处发送数据 bytes。
# recv
```python
msg=sk.recv(bufsize)
```
该 socket 等待接收数据，大小最多为 bufsize 字节。等待是阻塞式的。

# recvfrom
```python
msg,addr=sk.recvfrom(bufsize)
```
与 recv 的区别在于不仅返回数据，还返回发送方地址。即返回一个 (data,addr) 的元组。

# close
```python
sk.close()
```
关闭 sk。
