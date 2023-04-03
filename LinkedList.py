class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value


class LinkedList:
    def __init__(self, ls: list = None):
        """ llist = LinkedList([10, 20, 30, 40]) """
        self.head = None
        if ls is not None:
            node = Node(value=ls.pop(0))
            self.head = node
            for element in ls:
                node.next = Node(value=element)
                node = node.next

    def append(self, value=0):
        """llist.append(123) """
        temp = Node(value)
        if self.head is None:
            self.head = temp
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = temp

    def delete_at_index(self, index):
        """llist.delete_at_index(0)"""

        if self.head is not None:
            if index == 0:
                self.head = self.head.next
            else:
                temp = self.head
                while temp is not None and index > 1:
                    temp = temp.next
                    index = index - 1
                if index == 1 and temp.next is not None:
                    temp.next = temp.next.next

    def prepend(self, value=0):
        """llist.prepend(123)"""
        node = Node(value)
        node.next = self.head
        self.head = node

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        nodes.append("None")
        return " -> ".join(map(str, nodes))


if __name__ == '__main__':
    llist = LinkedList([20, 30])
    print(f'original llist:\n\t {llist}')

    llist.prepend(10)
    llist.append(40)
    print(f'\nllist 10 through 40:\n\t {llist}')

    llist.delete_at_index(0)
    print(f'\nnode 0 removed:\n\t {llist}')

    llist.delete_at_index(2)
    print(f'\nnode 2 removed:\n\t {llist}')

    llist = LinkedList([11, 22, 33, 44, 55])
    print(f'\nrestored the llist:\n\t {llist}')

    llist.delete_at_index(20)
    print(f'\nnode 20 removed:\n\t {llist}')

    llist.delete_at_index(1)
    print(f'\nnode 1 removed:\n\t {llist}')

    llist.delete_at_index(1)
    print(f'\nnode 1 removed:\n\t {llist}')

    llist.delete_at_index(0)
    print(f'\nnode 0 removed:\n\t {llist}')




