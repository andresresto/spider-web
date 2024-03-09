# Honestly don't know yet
# Andrés Resto
import numpy as np
# Define object TreeNode
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    # Add Child Node
    def add_child(self, child_node):
        self.children.append(child_node)

    # Remove child Node
    def remove_child(self, child_node):
        if child_node in self.children:
            self.children.remove(child_node)
        else:
            print("Child node not found")
    
# Find tree's depth
def tree_depth(node):
    # Base case
    if node is None:
        return 0
    
    relative_depth = []
    for children in node.children:
        relative_depth.append(tree_depth(children))

    if relative_depth == []:
        print("hi")
        return 1
    return np.max(relative_depth) + 1
    # return 1


# Recurrsive funciton to print tree structure
def print_tree(node, level = 0):
    if node is None:
        return
    print("   " * level + str(node.value))
    for child in node.children:
        print_tree(child, level + 1)



root = TreeNode(0)
child1 = TreeNode(1)
child2 = TreeNode(2)
child3 = TreeNode(3)
child4 = TreeNode(4)
child5 = TreeNode(5)
child6 = TreeNode(6)
child7 = TreeNode(7)
child8 = TreeNode(8)
child9 = TreeNode(9)
child10 = TreeNode(10)

root.add_child(child1)
root.add_child(child2)

child1.add_child(child3)
child1.add_child(child4)

child2.add_child(child5)
child2.add_child(child6)

child3.add_child(child7)
child3.add_child(child8)

child7.add_child(child9)
child9.add_child(child10)



# simple_root = TreeNode(0)
# simple_root.add_child(child1)
# simple_root.add_child(child2)

print("Tree depth: " + str(tree_depth(root)))

print("Tree")
print_tree(root)

# print("test")
# empty = []
# sample = [1,2,3,4]
# print(np.max(sample))