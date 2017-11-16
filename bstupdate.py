import sys

def insert(tree, z):
    #
    # MODIFY THIS FUNCTION AS NEEDED....
    #
    parent = None
    new = Node(z)
    node = tree.root
    while node is not None:
        parent = node
        if new.data < node.data:
            node = node.left
        else:
            node = node.right

    new.parent = parent
    if parent is None:
        tree.root = new
    elif new.data < parent.data:
        parent.left = new
        parent.minval = new.data
        parent.mingap = min(parent.data - new.data, new.mingap)

        MinGapOp(parent)
    else:
        parent.right = new
        parent.maxval = new.data
        parent.mingap = min(new.data - parent.data, new.mingap)

        MinGapOp(parent)

    return new

def MinGapOp(z):
    flag = True
    a = z.parent

    while flag:
        if a != None:

            leftmg = sys.maxsize
            rightmg = sys.maxsize

            rightdiff = sys.maxsize
            leftdiff = sys.maxsize

            if a.left != None:
                leftmg = a.left.mingap
                leftdiff = a.data - a.left.maxval
                a.minval = min(a.data, a.left.minval)
            if a.right != None:
                rightmg = a.right.mingap
                rightdiff = a.right.minval - a.data
                a.maxval = max(a.data, a.right.maxval)
            a.mingap = min(leftmg, rightmg, leftdiff, rightdiff)

            a = a.parent
        else:
            flag = False

def delete(tree, z):
    #
    # MODIFY THIS FUNCTION AS NEEDED....
    #
    target = search(tree.root, z)
    if target is None:
        return None
    if target.left is None:
        transplant(tree, target, target.right)
        MinGapOp(target.right)
    elif target.right is None:
        transplant(tree, target, target.left)
        MinGapOp(target.left)
    else:
        node = minimum(target.right)
        updateNode = node.right
        if node.parent is not target:
            transplant(tree, node, node.right)
            node.right = target.right
            node.right.parent = node
        transplant(tree, target, node)
        node.left = target.left
        node.left.parent = node
        MinGapOp(updateNode)

    return target

def transplant(tree, u, v):
    #
    # MODIFY THIS FUNCTION AS NEEDED....
    #
    if u.parent is None:
        tree.root = v
    elif u is u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v

    if v is not None:
        v.parent = u.parent


def minimum(node):
    #
    # MODIFY IN THE CODE IF NEEDED....
    #
    if node is not None:
        while node.left is not None:
            node = node.left
    return node


#
# YOU DO NOT NEED TO CHANGE THE CODE BELOW THIS LINE, BUT YOU CAN IF YOU WANT
#
def search(node, z):
    #
    # YOU DO NOT NEED TO MODIFY THIS FUNCTION....
    #
    while node is not None:
        if z == node.data:
            return node
        elif z < node.data:
            node = node.left
        else:
            node = node.right
    return None

# tree class
# YOU DO NOT NEED TO CHANGE THIS CLASS
class BST(object):
    def __init__(self):
        self.root = None

# node class
class Node(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.parent = None
        self.data = val
        self.mingap = sys.maxsize  # YOU WANT TO MAKE SURE THAT THIS ATTRIBUTE IS ALWAYS MAINTAINED CORRECTLY
        self.minval = val  # YOU WANT TO MAKE SURE THAT THIS ATTRIBUTE IS ALWAYS MAINTAINED CORRECTLY
        self.maxval = val  # YOU WANT TO MAKE SURE THAT THIS ATTRIBUTE IS ALWAYS MAINTAINED CORRECTLY


# This function takes care of building the tree according to specifications and outputing the min-gap after each operation as required.
def ads_test(data):
    n = len(data)
    tree = BST()  # create an empty BST

    for i in range(0, n):
        # perform required operation on the BST
        if data[i][0] == 'I':
            insert(tree, int(data[i][1:]))
        elif data[i][0] == 'D':
            delete(tree, int(data[i][1:]))

        # if this is not the first element, then output the value of the min gap after this operation
        if i > 0:
            print tree.root.mingap,

# Read input
f = open("input.txt", "r")
data = f.readline().split()

# Fill in the augmented data structure with the input and generate the appropriate output
ads_test(data)
