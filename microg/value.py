import math


class Value:
    def __init__(self,data,
                 _children=(),
                 _op='',
                 label=''):
        self.data = data
        self.grad = 0.0
        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op
        self.label = label

    def __repr__(self):
        return f"Value(data={self.data})"

    def __neg__(self):  # 负号运算
        return self * -1

    def __add__(self,other):
        other = other if isinstance(other,Value) \
            else Value(other)
        out = Value(self.data+other.data,
                    (self,other),
                    "+")

        def _backward():
            self.grad += out.grad        #累加保证在多次使用同一个节点时，梯度不会被覆盖（下同）
            other.grad += out.grad

        out._backward = _backward
        return out

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self,other):
        other = other if isinstance(other,Value) \
            else Value(other)
        out = Value(self.data*other.data,
                    (self,other),
                    "*")

        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad

        out._backward = _backward
        return out

    def __pow__(self, other):
        assert isinstance(other, (int, float)), "only supporting int/float powers for now"
        out = Value(self.data**other, (self,), f'**{other}')

        def _backward():
            self.grad += (other * self.data**(other-1)) * out.grad

            out._backward = _backward
        return out







    def __rmul__(self, other):   #交换操作数以进行乘法
        return self * other

    def __truediv__(self, other):
        return self * (other**-1)

    def exp(self):#指数函数
        x = self.data
        out = Value(math.exp(x),(self,),"exp")

        def _backward():
            self.grad += out.data * out.grad

        out._backward = _backward
        return out







    def tanh(self):#双曲正切函数
        x = self.data
        t = (math.exp(2*x) - 1) / (math.exp(2*x) + 1)
        out = Value(t,(self,),"tanh")

        def _backward():
            self.grad += (1-t**2)*out.grad

        out._backward = _backward
        return out

    def backward(self): #仅负责向前传递，各数学函数使用自动微分
        ordered = []
        visited = set()

        def build(node):
            if node in visited:
                return
            visited.add(node)
            for child in node._prev:
                build(child)
            ordered.append(node)

        build(self)
        for node in ordered:
            node.grad = 0.0
        self.grad = 1.0
        for node in reversed(ordered):
            node._backward()
