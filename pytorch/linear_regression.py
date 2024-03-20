import torch
import random


# fake train dataset
def synthetic_data(w, b, num_examples):  
    """生成y=Xw+b+高斯噪声"""
    X = torch.normal(0, 1, (num_examples, len(w)))
    y:torch.Tensor = torch.matmul(X, w) + b
    y += torch.normal(0, 0.01, y.shape)
    # 这里有个细节：w是torch.Size([2])的，乘出来的 y 就是torch.Size([1000])的，所以要 reshape 来为 y 增加一个维度。
    return X, y.reshape(-1,1)



# 将 dateset 以 batch 的方式加载
def data_iter(batch_size, features, labels):
    """
    1. epochs 足够多的话至少会遍历训练集
    2. 构造成生成器函数
    3. 传入的参数是 batch_size, features 和 labels，生成的是一个 batch 的数据
    """
    num_examples = len(features)
    indices = list(range(num_examples))
    # 打乱 index
    random.shuffle(indices)
    for i in range(0, num_examples, batch_size):
        batch_indices = torch.tensor(
            indices[i: min(i + batch_size, num_examples)])
        yield features[batch_indices], labels[batch_indices]

# forward
def linreg(X, w, b): 
    """线性回归模型"""
    return torch.matmul(X, w) + b

# loss
def squared_loss(y_hat, y):  
    """均方损失"""
    return (y_hat - y) ** 2 / 2

# SGD
def sgd(params, lr, batch_size): 
    """小批量随机梯度下降"""
    with torch.no_grad():
        for param in params:
            param -= lr * param.grad / batch_size
            param.grad.zero_()


if __name__=="__main__":
    true_w = torch.tensor([2, -3.4])
    true_b = 4.2
    features, labels = synthetic_data(true_w, true_b, 1000)

    batch_size = 10

    lr = 0.03
    num_epochs = 30
    net = linreg
    loss = squared_loss

    # 初始化模型参数
    w = torch.normal(0, 0.01, size=(2,1), requires_grad=True)
    b = torch.zeros(1, requires_grad=True)

    for epoch in range(num_epochs):
        for X, y in data_iter(batch_size, features, labels):
            l = loss(net(X, w, b), y)  # X和y的小批量损失
            # 因为l形状是(batch_size,1)，而不是一个标量。l中的所有元素被加到一起，
            # 并以此计算关于[w,b]的梯度
            l.sum().backward()
            sgd([w, b], lr, batch_size)  # 使用参数的梯度更新参数
        with torch.no_grad():
            train_l = loss(net(features, w, b), labels)
            print(f'epoch {epoch + 1}, loss {float(train_l.mean()):f}')

    print(f'w的估计误差: {true_w - w.reshape(true_w.shape)}')
    print(f'b的估计误差: {true_b - b}')

