class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

# single-linked list:
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("For single-linked list:")
current = node1
while current != None:
    print(current.data, end = "->")
    current = current.next

# doubly-linked list:
node1.next = node2

node2.next = node3
node2.prev = node1

node3.next = node4
node3.prev = node2

node4.next = node5
node4.prev = node3

node5.prev = node4

print("\nFor double-linked list:")
current = node5
while current != None:
    print(current.data, end = "->")
    current = current.prev