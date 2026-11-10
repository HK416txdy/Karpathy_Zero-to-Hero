from microg import Value
from microg import Neuron
from microg.Neuron import Layer
from microg.Neuron import MLP

x = [2.0,3.0,-1.0]

n = MLP(3,[4,4,1])
y = n(x)
print(y)


