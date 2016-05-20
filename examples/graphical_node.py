from matplotlib.pyplot import *
from fovea import *
from queue import *

class VisualNode:
    def __init__(self, item, label, parent=None, radius=.1, edge_color='k'):
        self.item = item
        self.label = label
        self.children = [] 
        self.set_parent(parent)
        self.radius = radius
        self.edge_color = edge_color

    def __str__(self):
        return "Node " + self.label + " at location " + str(self.location) + "."

    def display(self):
        self.display_obj = Circle(self.location, self.radius, ec=self.edge_color, fill=False)

    def set_location(self, location, x_cushion, y_cushion, total_space, max_radius):
        if not self.parent:
            self.location = location 
        else:
            self.location = (self.parent.location[0], self.parent.location[1] - .25)

    def set_parent(self, parent):
        if parent:
            self.parent = parent
            self.parent.add_child(self)
        else:
            self.parent = None

    def add_child(self, node):
        self.children.append(node)

    def get_children(self):
        return self.children

    def num_children(self):
        return len(self.children)

    def num_grandchildren(self):
        return sum([self.children[i].num_children() for i in range(self.num_children())])

    def get_value(self):
        return self.item

    def is_leaf(self):
        return not bool(self.children)

    def delete(self):
        self.display_obj.remove()
        self.parent = None
        self.children = []


class VisualTree:
    def __init__(self, root):
        self.root = root
        self.tree_fig = figure() 
        self.nodes = self.get_nodes(self.root)
        self.height = self.get_height()
        self.mlr = self.max_level_radii()
        self.mll = self.max_level_length()
        self.mnr = self.max_node_radius()

    def get_nodes(self, root):
        node_list = [] 
        node_queue = Queue()
        node_queue.put(root)
        root.level = self.get_level(root)
        node_list.append([])
        while not node_queue.empty():
            current_node = node_queue.get()
            if not current_node.is_leaf():
                node_list.append([])
            node_list[current_node.level].append(current_node)
            for child in current_node.get_children():
               child.level = child.parent.level + 1
               node_queue.put(child)
        return node_list
                
    def get_level(self, node):
        if node is self.root:
            return 0
        return 1 + get_level(self.parent)

    def get_height(self):
        return len(self.nodes)

    def max_node_radius(self):
        max_rad = 0
        for level in self.nodes:
            for node in level:
                if node.radius > max_rad:
                    max_rad = node.radius
        return max_rad

    def max_level_radii(self):
        level_radii = []
        for level in self.nodes:
            max_level_radius = 0
            for node in level:
                if node.radius > max_level_radius:
                    max_level_radius = node.radius
            level_radii.append(max_level_radius)
        return level_radii

    def max_level_length(self):
        max_length = 1
        for level in self.nodes:
            level_length = len(level)
            if level_length > max_length:
                max_length = level_length
        return max_length

    def set_tree_bounds(self, x_cushion, y_cushion):
        if not x_cushion:
            x_cushion = 4 * sum(self.mlr)
        if not y_cushion:
            y_cushion = 3 * sum(self.mlr)
        xlim = x_cushion * self.mll
        ylim = y_cushion * self.mll
        self.tree_axes.set_xlim([0, xlim])
        self.tree_axes.set_ylim([0, ylim])
        return (xlim, ylim)

    def set_patch_locs(self, x_cushion, y_cushion, bounds):
        self.root
    
    def draw_tree(self, x_cushion=None, y_cushion=None):
        self.tree_plot = self.tree_fig.add_subplot(111, aspect='equal')
        self.tree_axes = gca()
        self.bounds = self.set_tree_bounds(x_cushion, y_cushion)
        for level in self.nodes:
            for node in level:
                node.display()
                self.tree_plot.add_patch(node.display_obj)
        show()

firstNode = VisualNode(1, '1')
secondNode = VisualNode(2, '2', parent=firstNode)
thirdNode = VisualNode(3, '3', parent=secondNode)
fourthNode = VisualNode(4, '4', parent=secondNode)
fifthNode = VisualNode(5, '5', parent=firstNode)
fir = VisualTree(firstNode)
