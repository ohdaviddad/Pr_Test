from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.data)

class DoubleLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def append(self, data):
        node = Node(data)
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        return node

    def appendleft(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        return node

    def pop(self):
        if self.tail is None:
            return

        node = self.tail
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            # 删除最后一个元素 设置 head 为 None
            self.head = None

        return node

    def popleft(self):
        if self.head is None:
            return

        node = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            # 删除最后一个元素 设置 tail 为 None
            self.tail = None

        return node

    def pop_node(self, node):
        node_prev = node.prev
        node_next = node.next

        if node_prev:
            node_prev.next = node.next
        else:
            # 删除头节点 需要修改 head
            self.head = node.next

        if node_next:
            node_next.prev = node.prev
        else:
            # 删除尾节点 需要修改 tail
            self.tail = node.prev

        return node

    def s(self, reverse=False):
        d = []
        if reverse:
            tail = self.tail
            while tail:
                d.append(tail.data)
                tail = tail.prev
        else:
            head = self.head
            while head:
                d.append(head.data)
                head = head.next

        return d

    def ss(self, reverse=False, both=False):
        d = []
        if reverse:
            tail = self.tail
            while tail:
                d.append(tail)
                tail = tail.prev
        else:
            head = self.head
            while head:
                d.append(head)
                head = head.next

        if both:
            s1 = ', '.join([f'({i.prev}, {i}, {i.next})' for i in d])
        else:
            s1 = ', '.join([f'{i}' for i in d])

        s2 = f'[{s1}]'
        return s2


if __name__ == '__main__':
    a = DoubleLinkedList()

    b = a.append(1)
    c = a.append(2)
    d = a.append(3)

    a.pop_node(c)
    print(a.ss(), a.ss(reverse=True))

