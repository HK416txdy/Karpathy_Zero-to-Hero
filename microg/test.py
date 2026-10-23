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

x1 = Value(2.0, label='x1')
x2 = Value(0.0, label='x2')

w1 = Value(-3.0, label='w1')
w2 = Value(1.0, label='w2')
b = Value(6.7, label='b')
x1w1 = Value(x1.data * w1.data, label='x1w1')
x2w2 = Value(x2.data * w2.data, label='x2w2')
x1w1x2w2 = Value(x1w1.data + x2w2.data, label='x1w1x2w2')
n = x1w1x2w2+b; n.label = 'n'
o = n.tanh(); o.label = 'o'

dot_vishualizer.draw_dot(o)

if __name__ == '__main__':
    output_path = dot_vishualizer.render_dot(
        o,
        view=True,
    )
