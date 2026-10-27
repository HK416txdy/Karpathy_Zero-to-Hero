import dot_vishualizer
from value import Value

a = Value(2, label='a')
b = Value(3, label='b')
c = Value(10, label='c')
print(c)
e = a * b
e.label = 'e'
d = e + c
d.label = 'd'

f = Value(-2.0, label='f')
L = d * f
L.label = 'L'
print(d._prev)
print(d._op)

x1 = Value(0.1, label='x1')
x2 = Value(0.9, label='x2')

w1 = Value(0.0, label='w1')
w2 = Value(0.7, label='w2')

b = Value(0.2, label='b')

x1w1 = x1*w1; x1w1.label = 'x1w1'
x2w2 = x2*w2; x2w2.label = 'x1w2'
x1w1x2w2 = x1w1 + x2w2 ; x1w1x2w2.label = 'x1w1+x2w2'
n = x1w1x2w2 + b; n.label = 'n'
o=n.tanh();o.label = 'o'
o.backward()

output_path = dot_vishualizer.draw_dot(o)
