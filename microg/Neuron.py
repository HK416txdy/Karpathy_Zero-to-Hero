import random
from microg.Value import Value

class Neuron:
    """单个神经元：计算 tanh(w · x + b)。"""

    def __init__(self,nin):
        """nin 为输入数量，每个输入对应一个权重。
        权重 w 和偏置 b 均从 [-1, 1] 均匀随机初始化，
        并封装为 Value，以便参与自动求导。
        """
        self.w = [Value(random.uniform(-1,1)) for _ in range(nin)]
        self.b = Value(random.uniform(-1,1))


    def __call__(self, x):
        """前向传播；x 的长度应与输入数量 nin 一致。"""
        # zip 将权重与输入逐一配对；sum 以偏置 b 为初始值累加乘积。
        act = sum((wi * xi for wi, xi in zip(self.w, x)), self.b)
        # 使用 tanh 激活函数，将加权和映射到 (-1, 1)。
        out = act.tanh()
        return out


class Layer:
    """全连接层：所有神经元接收同一组输入。"""

    def __init__(self,nin,nout):
        """nin 为每个神经元的输入数量，nout 为本层的神经元数量。"""
        self.neurons = [Neuron(nin) for _ in range(nout)]

    def __call__(self, x):
        """返回本层输出；只有一个神经元时返回单个 Value，否则返回列表。"""
        outs = [neuron(x) for neuron in self.neurons]
        return outs[0] if len(outs) == 1 else outs


class MLP:
    """多层感知机：将多个全连接层依次连接。"""

    def __init__(self,nin,nouts):
       """nin 为网络输入数量，nouts 为各层的神经元数量列表。

       例如 nin=3、nouts=[4, 4, 1] 表示 3 → 4 → 4 → 1 的网络。
       """
       # 将输入维度与各层输出维度拼接，相邻两项确定一层的形状。
       sz = [nin] + nouts
       self.layers = [Layer(sz[i], sz[i+1]) for i in range(len(nouts))]

    def __call__(self, x):
        """依次执行各层的前向传播，将上一层的输出作为下一层的输入。

        当前 Layer 会将单元素输出转为 Value，因此中间层的神经元数量
        应大于 1，以便下一层能够遍历输入。
        """
        for layer in self.layers:
            x = layer(x)
        return x
