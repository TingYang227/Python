class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


class BinaryTree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insert_left(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insert_right(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def get_left_child(self):
        return self.leftChild

    def get_right_child(self):
        return self.rightChild

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key


def preorder(tree):
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())

def postorder(tree):
    if tree != None:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val())

def postordereval(tree):
    opers = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.get_root_val()](res1, res2)
        else:
            return tree.get_root_val()

def inorder(tree):
    if tree != None:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())



def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree("")
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == "(":
            currentTree.insert_left("")
            pStack.push(currentTree)
            currentTree = currentTree.get_left_child()

        elif i in ["+", "-", "*", "/"]:
            currentTree.set_root_val(i)
            currentTree.insert_right("")
            pStack.push(currentTree)
            currentTree = currentTree.get_right_child()

        elif i == ")":
            currentTree = pStack.pop()

        elif i not in ["+", "-", "*", "/", ")"]:
            try:
                currentTree.set_root_val(int(i))
                parent = pStack.pop()
                currentTree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return eTree


pt = buildParseTree("( ( 10 + 5 ) * 3 )")
postorder(pt)

