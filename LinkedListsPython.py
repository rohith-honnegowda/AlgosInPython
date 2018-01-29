# Let us first create the required node and
# then created the linkedListStructure from it

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def printNodes(self):
        temphead = self.head
        index = 0
        print("The List of Nodes in the linkedList")
        while temphead != None:
            print("{0}({1})-->".format(index, temphead.data), end = '')
            index = index + 1
            temphead = temphead.next
        print("None")

    # Insert Node at the beginning of the linkedList
    def insertAtFront(self, newNode):
        newNode.next = self.head
        self.head = newNode

    # Insert New node at the end of the list
    def insertAtEnd(self, newNode):
        temphead = self.head
        while temphead.next != None:
            temphead = temphead.next
        temphead.next = newNode

    # Insert at a given position in the list
    def insertAtPositionN(self, newNode, n):
        index = 0
        temphead = self.head
        while index < n-1:
            index = index + 1
            temphead = temphead.next
            if temphead.next == None:
                temphead.next = newNode
                break
        tempNode = temphead
        newNode.next = tempNode.next
        tempNode.next = newNode

    def deleteData(self, data):
        temphead = self.head
        while temphead.next != None:
            #print("Data is ", temphead.next.data)
            if temphead.next.data == data:
                temphead.next = temphead.next.next
                break
            temphead = temphead.next


def main():
        llist = LinkedList()

        llist.head = Node(15)
        second = Node(62)
        third = Node(83)
        fourth = Node(49)
        fifth = Node(25)

        llist.head.next = second
        second.next = third
        third.next = fourth
        fourth.next = fifth
        first = Node(67)
        nth = Node(894)
        llist.insertAtFront(first)
        llist.insertAtPositionN(nth, 4)
        llist.printNodes()
        llist.deleteData(67)
        llist.printNodes()

if __name__== "__main__":
    main()
