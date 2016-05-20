from matplotlib.pyplot import *

class GraphicalNode:
    def __init__(self, tree, item, label, location=(0,0), radius=1, ec='k',children=[]):
        self.tree = tree
        self.item = item
        self.label = label
        self.display_obj = Circle(location, radius)
        self.children = children
        self.set_position()

    def add_child(self, node):
        self.children.append(node)
        node.set_position()

    def get_children(self):
        return self.children

    def get_value(self):
        return self.item

    def is_leaf(self):
        return not bool(self.children)

    def set_position(self):
        if self.tree.root:
            self.position = self.tree.get_node_position(self)
        else:
            self.position = (0,0)
            self.tree._set_root(self)

class Tree:
    def __init__(self):
        self.root = None
        self.nodes = [[]]
        depth = len(self.nodes)

    def _set_root(self,node):
        self.root = node
        self.nodes[0] = [self.root]

    def get_node(self, node_position):
        return self.nodes[node_position[0]][node_position[1]]
        
    def get_children(self, node_position):
        return self.get_node(node_position).get_children()

    def add_child(self, child, parent_position):
        parent = self.get_node(parent_position)
        parent.children.append(child)
        node.set_parent(parent)
        child.set_position()

    def get_node_position(self,node):
        return self.nodes.index(node)
