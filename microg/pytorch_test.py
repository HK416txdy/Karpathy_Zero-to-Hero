import torch


x1 = torch.tensor([2.0]).double()               ;x1.requires_grad_(True)
x2 = torch.tensor([0.0]).double()               ;x2.requires_grad_(True)
w1 = torch.tensor([-3.0]).double()              ;w1.requires_grad_(True)
w2 = torch.tensor([1.0]).double()               ;w2.requires_grad_(True)
b = torch.tensor([6.8813735870195432]).double() ;b.requires_grad_(True)

n = x1*w1 + x2*w2 + b
o = torch.tanh(n)

print(o.data.item())
o.backward()

