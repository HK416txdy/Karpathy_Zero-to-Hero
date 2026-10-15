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





if __name__ == '__main__':
    output_path = dot_vishualizer.render_dot(
        L,
        view=True,
    )
    print(f'Graph saved to: {output_path}')
