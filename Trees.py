# Tree datastructure and its various operations
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def populateTree(root):
    temproot = root
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six= Node(6)
    seven = Node(7)
    eight = Node(8)
    nine = Node(9)
    temproot.left = two
    temproot.right = three
    temproot.left.right = four
    temproot.right.left = five
    temproot.right.right = six
    temproot.right.left.left = seven
    temproot.right.right.left = eight
    temproot.right.right.right = nine


def printTree(root):
    buf = []
    output = []
    if not root:
        print('*')
    else:
        buf.append(root)
        count = 1
        nextCount = 0
        while count > 0:
            node = buf.pop(0)
            if node:
                output.append(node.data)
                count -= 1
            else:
                output.append('*')
            if node and node.left:
                buf.append(node.left)
                nextCount += 1
            else:
                buf.append(None)
            if node and node.right:
                buf.append(node.right)
                nextCount += 1
            else:
                buf.append(None)
            if count == 0:
                print(output)
                output = []
                count = nextCount
                nextCount = 0
        # print the remaining all empty leaf node part
        for i in range(len(buf)):
            output.append('*')
        print(output)





def main():
    root = Node(11)
    populateTree(root)
    printTree(root)



if __name__ == '__main__':
    main()
