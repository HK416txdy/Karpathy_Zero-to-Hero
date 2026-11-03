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


def _build_dot(root):
    """创建从左到右排列的计算图。"""
    root.backward()
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


def draw_dot(root, filename='computation_graph', directory=None, view=False):
    """直接生成 SVG，默认保存到本模块旁的 Svg_out，返回文件路径。"""
    if directory is None:
        directory = Path(__file__).resolve().parent / 'Svg_out'
    dot = _build_dot(root)
    return dot.render(
        filename=filename,
        directory=directory,
        view=view,
        cleanup=True,
    )


def render_dot(root, filename='computation_graph', directory=None, view=False):
    """兼容原来的渲染入口。"""
    return draw_dot(root, filename=filename, directory=directory, view=view)
