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

    def __add__(self,other):
        out = Value(self.data+other.data,
                    (self,other),
                    "+")

        def _backward():
            self.grad += out.grad
            other.grad += out.grad

        out._backward = _backward
        return out

    def __mul__(self,other):
        out = Value(self.data*other.data,
                    (self,other),
                    "*")

        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad

        out._backward = _backward
        return out

    def tanh(self):
        x = self.data
        t = (math.exp(2*x) - 1) / (math.exp(2*x) + 1)
        out = Value(t,(self,),"tanh")
        return out

    def backward(self):
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
