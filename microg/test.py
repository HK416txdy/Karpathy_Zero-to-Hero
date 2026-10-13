from value import Value

a = Value(2)
b = Value(3)
c = a + b
print(c)

d = a * b+ c
print(d._prev)
print(d._op)