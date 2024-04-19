import random
from double_linked_list import DoubleLinkedList

class LRU:
    def __init__(self, max_len):
        self.max_len = max_len
        self.length = 0
        self.dl_list = DoubleLinkedList()
        self.map = {}

    def get(self, key):
        if key in self.map:
            node = self.map[key]
            self.dl_list.pop_node(node)
            self.map[key] = self.dl_list.append(node.data)
            return node.data[1]
        else:
            return -1

    def put(self, k, v):
        if k in self.map:
            node = self.map[k]
            self.dl_list.pop_node(node)
            self.map[k] = self.dl_list.append((k, v))
        else:
            if self.length < self.max_len:
                self.map[k] = self.dl_list.append((k, v))
                self.length += 1
            else:
                node = self.dl_list.popleft()
                old_key = node.data[0]
                del self.map[old_key]
                self.map[k] = self.dl_list.append((k, v))

    def s(self):
        d = {}
        for k, v in self.map.items():
            d[k] = v.data[1]

        return str(d)


if __name__ == '__main__':
    lru = LRU(4)

    # numbers = [i for i in range(50)]
    #
    # for i in range(8):
    #     num = random.choice(numbers)
    #     print('put:', num%10, num)
    #     lru.put(num%10, num)
    #     print(lru.s(), lru.dl_list.s(), lru.length)
    #
    # for i in range(5):
    #     print('get:', i, lru.get(i))
    #     print(lru.s(), lru.dl_list.s(), lru.length)

    lru.put(2, 22)
    lru.put(3, 33)
    print(lru.s(), lru.dl_list.s(), lru.length)

    lru.get(2)
    print(lru.s(), lru.dl_list.s(), lru.length)

    lru.put(2, 52)
    print(lru.s(), lru.dl_list.s(), lru.length)
