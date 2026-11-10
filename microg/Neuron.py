import random
from Value import Value

class Neuron:
    """nin : number of inputs to the neuron"""
    def __init__(self,nin):
       self.w = [Value(random.uniform(-1,1)) for _ in range(nin)]
       self.b = Value(random.uniform(-1,1))

    def __call__(self, x):   #实现 w *(点积）x + b
        zip(self.w,x)  #将权重和输入打包成元组



