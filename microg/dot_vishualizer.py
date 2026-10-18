from pathlib import Path

from graphviz import Digraph


def trace(root):
    """收集从 root 可达的所有节点，以及输入节点到结果节点的边。"""
    nodes, edges = set(), set()

    def build(v):
        if v in nodes:
            return
        nodes.add(v)
        for child in v._prev:
            edges.add((child, v))
            build(child)

    build(root)
    return nodes, edges


def draw_dot(root):
    """创建从左到右排列的计算图；返回对象，供预览或渲染。"""
    dot = Digraph(format='svg', graph_attr={'rankdir': 'LR'})

    nodes, edges = trace(root)
    for n in nodes:
        uid = str(id(n))
        # record 将标签和数值显示在矩形的不同分栏中。
        dot.node(
            name=uid,
            label="{ %s | data %.4f | grad %.4f }" % (n.label, n.data, n.grad),
            shape='record',
        )
        if n._op:
            # 运算节点单独显示，并连接到运算结果。
            dot.node(name=uid + n._op, label=n._op, shape='ellipse')
            dot.edge(uid + n._op, uid)

    for n1, n2 in edges:
        # 输入值先连接到运算节点，再由运算节点连接到结果。
        dot.edge(str(id(n1)), str(id(n2)) + n2._op)

    return dot


def render_dot(root, filename='computation_graph', directory='Svg_out', view=False):
    dot = draw_dot(root)
    return dot.render(
        filename=filename,
        directory=directory,
        view=view,
        cleanup=True,
    )
