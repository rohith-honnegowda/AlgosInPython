from LinkedListsPython import LinkedList, Node 

llist = LinkedList()

llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third

printNodes(llist.head)
