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

        # check case if the head itself if the node to
        # be deleted
        if temphead.data == data:
            self.head = temphead.next

        while temphead.next != None:
            #print("Data is ", temphead.next.data)
            if temphead.next.data == data:
                temphead.next = temphead.next.next
                break
            temphead = temphead.next

    def getNthNode(self, n):
        temphead = self.head
        index = 0
        firstPointer = temphead
        while index < n:
            if temphead.next == None:
                print("The value {0} is larger than the length of the list")
                exit()
            index += 1
            temphead = temphead.next

        while temphead.next != None:
            firstPointer = firstPointer.next
            temphead = temphead.next
        print("The value of the nth Node from the end is {0}".format(firstPointer.data))

    def reverseLinkedList(self):

        if self.head == None or self.head.next == None:
            return

        newhead = None
        while self.head != None:
            temp = self.head
            self.head = temp.next
            temp.next = newhead
            newhead = temp
        self.head = newhead



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
        #llist.insertAtFront(first)
        #llist.insertAtPositionN(nth, 4)
        llist.printNodes()
        #llist.deleteData(49)
        llist.reverseLinkedList()
        llist.printNodes()
        #llist.getNthNode(2)

if __name__== "__main__":
    main()
