# Example 1 :-

class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
# Linked List class contains a Node object


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None


def Circular(head):
    if head == None:
        return True
    # Next of head
    node = head.next
    i = 0
    # This loop would stop in both cases (1) If
    # Circular (2) Not circular
    while ((node is not None) and (node is not head)):
        i = i + 1
        node = node.next
    return (node == head)


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(3)
    second = Node(2)
    third = Node(0)
    fourth = Node(-4)

    llist.head.next = second
    second.next = llist.head
    third.next = fourth
    fourth.next = llist.head
    if (Circular(llist.head)):
        print("Output: True")
        print("Explanation : there is a cycle in the linked list.")
    else:
        print("Output: False")
        print("Explanation : there is no cycle in the linked list.")


# Example 2 :-

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


def Circular(head):
    if head == None:
        return True
    node = head.next
    i = 0
    while ((node is not None) and (node is not head)):
        i = i + 1
        node = node.next
    return (node == head)


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)

    llist.head.next = second
    second.next = llist.head
    if (Circular(llist.head)):
        print("Output: True")
        print("Explanation : there is a cycle in the linked list.")

    else:
        print("Output: False")
        print("Explanation : there is no cycle in the linked list.")


# Example 3:-

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


def Circular(head):
    if head == None:
        return True

    node = head.next
    i = 0

    while ((node is not None) and (node is not head)):
        i = i + 1
        node = node.next
    return (node == head)


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    if (Circular(llist.head)):
        print("Output: True")
        print("Explanation : there is a cycle in the linked list.")
    else:
        print("Output: False")
        print("Explanation : there is no cycle in the linked list.")
