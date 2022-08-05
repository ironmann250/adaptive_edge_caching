import hashlib
import math

'''
This is a implementation of the FBR algorithm in python
'''


# A linked list node
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.id = self.get_hash()
        self.new = False
        self.old = False
        self.count = 0

    def get_hash(self):
        y = str.encode(str(self.data))
        ha = hashlib.sha256(y)
        hash_no = ha.hexdigest()
        return hash_no

    @property
    def details(self):
        d = lambda x: None if x is None else x.data
        return {'data': self.data, 'new': self.new, 'old': self.old, 'next': d(self.next), 'prev': d(self.prev),
                'count': self.count}

    def reduce_count(self):
        self.count = math.ceil(self.count / 2)


# Class to create a Doubly Linked List
class LRUChain:

    # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.table = {}

    # Given a reference to the head of a list and an
    # integer, inserts a new node on the front of list
    def push(self, new_node):

        # 1. Allocates node
        # 2. Put the data in it

        if new_node.id in self.table:
            new_node = self.delete_node(self.table[new_node.id])
            new_node.next = None
            new_node.prev = None
        self.table[new_node.id] = new_node

        # 3. Make next of new node as head and
        # previous as None (already None)
        new_node.next = self.head

        # 4. change prev of head node to new_node
        if self.head is not None:
            self.head.prev = new_node

            # 5. move the head to point to the new node
        self.head = new_node
        if not self.tail:
            self.tail = new_node

        self.length += 1

        return new_node

    def print_list(self, node):
        print("\nTraversal in forward direction")
        while node is not None:
            print(node.data)
            node = node.next

        print("\nTraversal in reverse direction")
        last = self.tail
        while last is not None:
            print(last.data)
            last = last.prev

    def find(self, id_):
        node = self.head
        while node:
            if node.id == id_:
                result = f'id: {id_} \nData: {node.data}'
                print(result)
                return node
            node = node.next
        return None

    def remove_with_id(self, id_):
        node = self.find(id_)
        if node:
            if node.prev:
                if node.next:  # delete a middle node
                    node.prev.next = node.next
                    node.next.prev = node.prev
                else:  # delete last node
                    node.prev.next = None
                    self.tail = node.prev
                print(f'Deleted {id_}')
            else:  # delete head node
                self.head = node.next
                if node.next:
                    node.next.prev = None
                else:
                    self.tail = None
                print(f'Deleted {id_}')
            self.length -= 1
        return node

    def remove_with_data(self, data):
        node = self.head
        while node:
            if node.data == data:
                if node.prev:
                    if node.next:  # delete a middle node
                        node.prev.next = node.next
                        node.next.prev = node.prev
                    else:  # delete last node
                        node.prev.next = None
                        self.tail = node.prev
                    print(f'Deleted {data}')
                else:  # delete head node
                    self.head = node.next
                    if node.next:
                        node.next.prev = None
                    else:
                        self.tail = None
                    print(f'Deleted {data}')
                self.length -= 1
                return node
            node = node.next
        return None

    def delete_node(self, node):
        if node.id in self.table:
            node = self.table.pop(node.id)
            if node.prev:
                if node.next:  # delete a middle node
                    node.prev.next = node.next
                    node.next.prev = node.prev
                else:  # delete last node
                    node.prev.next = None
                    self.tail = node.prev

            else:  # delete head node
                self.head = node.next
                if node.next:
                    node.next.prev = None
                else:
                    self.tail = None
            self.length -= 1
        return node

    def list(self):
        d_list = []
        node = self.head
        while node:
            d_list.append(node.data)
            node = node.next
        return d_list

    def details(self):
        d_list = []
        node = self.head
        while node:
            d_list.append(node.details)
            node = node.next
        return d_list

    def count_display(self):
        d_list = []
        node = self.head
        while node:
            d_list.append(node.count)
            node = node.next
        return d_list

    def hash_table(self):
        d_list = {}
        node = self.head
        while node:
            d_list[node.id] = node.data
            node = node.next
        return d_list


class CountChain:      # replace and maintain count and maintain boundary
    def __init__(self, cache_size):
        self.length = 0
        self.cache_size = cache_size
        self.sections = [.4, .3]
        self.section_count = [round(i * self.cache_size) for i in self.sections]  # middle, old
        self.new_boundary = None
        self.old_boundary = None
        self.total_count = 0
        self.a_max = 3  # maximum average of counts
        self.c_max = 8  # maximum chain count
        self.table = {}  # to check if a block exists | stores the reference of a block if it exists {id: node}
        self.chain = {i: LRUChain() for i in range(1, self.c_max+1)}
        self.hit = 0
        self.miss = 0

    @property
    def average_count(self):
        return round(self.total_count / self.length, 2)

    def maintain_count(self):
        if self.average_count > self.a_max:
            # print('start: ', self.details_display())
            new_chain = {i: LRUChain() for i in range(1, self.c_max+1)}

            def reduce_count(node):
                while node:
                    node.reduce_count()
                    new_chain[node.count].push(node)
                    node = node.prev

            for chain in self.chain.values():
                reduce_count(chain.tail)
            self.chain = new_chain
            # print('end: ', self.details_display())
            # print('b', self.total_count, self.average_count)
            self.total_count = math.ceil(self.total_count / 2)
            # print('a', self.total_count, self.average_count)

    def find_match(self, count, old, new, boundary, new_node):
        tails = [boundary.prev] + [self.chain[i].tail for i in range(count + 1, self.c_max + 1)] + [self.chain[i].tail for i in range(1, count)] + [self.chain[count].tail]
        # print(tails)

        # print({i:self.chain[i].list() for i in self.chain})

        def find(n_node):
            while n_node is not None:
                if n_node.id == new_node.id:
                    n_node = n_node.prev
                    continue
                if (n_node.old is old) and (n_node.new is new):
                    return n_node
                n_node = n_node.prev
            return None

        for tail in tails:
            match = find(tail)
            if match is not None:
                return match

    def maintain_boundary(self, new_node, status, replace):    # status => hit or miss
        if self.length > sum(self.section_count):
            # print(self.new_boundary.data, self.old_boundary.data)

            if (status == 'miss' and self.length == self.cache_size and replace is True) or (status == 'hit' and new_node.old is True):
                # middle and new boundary changes
                self.old_boundary = self.find_match(count=self.old_boundary.count, old=False, new=False,
                                                    boundary=self.old_boundary, new_node=new_node)
                self.old_boundary.old = True
                # print('new old', self.old_boundary.data)
                self.new_boundary = self.find_match(count=self.new_boundary.count, old=False, new=True,
                                                    boundary=self.new_boundary, new_node=new_node)
                self.new_boundary.new = False

            elif status == 'hit' and new_node.new is True:
                pass    # no boundary changes
            elif (status == 'hit') and (new_node.old is False) and (new_node.new is False):
                # only middle boundary changes | status is hit and new_node is in the middle
                self.new_boundary = self.find_match(count=self.new_boundary.count, old=False, new=True,
                                                    boundary=self.new_boundary, new_node=new_node)
                self.new_boundary.new = False

            new_node.new, new_node.old = True, False

        elif self.length == sum(self.section_count):
            self.new_boundary = new_node
        elif self.length == self.section_count[1]:
            self.old_boundary = new_node
            new_node.old = True
        elif self.length <= self.section_count[1]:
            new_node.old = True

    def maintain_cache_size(self):
        if self.length > self.cache_size:
            victim = self.find_victim()
            self.total_count -= victim.count
            self.length -= 1
            self.table.pop(victim.id)
            self.chain[victim.count].delete_node(victim)
            return True

    def find_victim(self):
        def find_match(n_node):
            while n_node is not None:
                # print('victim finder', n_node.data, n_node.old)
                if n_node.old is True:
                    return n_node
                n_node = n_node.prev
        for no in range(1, self.c_max+1):
            chain = self.chain[no]
            node = find_match(chain.tail)
            if node:
                return node

    def push(self, data):
        # creating boundaries and labelling new and old sections
        new_node = Node(data)
        status = 'miss'
        if new_node.id in self.table:
            new_node = self.table[new_node.id]
            new_node = self.chain[new_node.count].delete_node(new_node)         # self.table[new_node.id]
            new_node.prev, new_node.next = None, None
            self.hit += 1
            status = 'hit'
        else:
            self.table[new_node.id] = new_node
            self.length += 1
            self.miss += 1

        replace = self.maintain_cache_size()

        if not new_node.new:
            new_node.count += 1
            self.total_count += 1

        self.chain[new_node.count].push(new_node)

        self.maintain_count()  # maintains the average count

        self.maintain_boundary(new_node=new_node, status=status, replace=replace)

    def freq_count_display(self):
        return {i.data: i.count for i in self.table.values()}

    def data_display(self):
        return {i: self.chain[i].list() for i in self.chain}

    def details_display(self):
        return {i: self.chain[i].details() for i in self.chain}

    def hit_ratio(self):
        return round((self.hit/(self.hit+self.miss))*100, 2)

ref = [8, 5, 11, 5, 6, 2, 25, 31, 3, 29, 21, 3, 5, 2, 4, 3, 17, 16, 10, 15, 2, 24, 27, 21, 6, 3, 2, 4, 6, 2, 5, 37, 2, 2, 2, 2, 12, 2, 5, 10, 4, 30, 4, 2, 6, 16, 7, 2, 2, 16, 2, 2, 10, 3, 20, 14, 35, 7, 2, 13, 6, 2, 8, 3, 40, 2, 37, 2, 14, 40, 3, 3, 17, 28, 3, 7, 33, 22, 2, 4, 6, 7, 12, 27, 3, 2, 7, 36, 5, 28, 2, 37, 4, 14, 2, 2, 16, 9, 28, 8, 2, 2, 3, 3, 12, 15, 36, 4, 5, 4, 12, 4, 33, 7, 2, 24, 12, 16, 2, 8, 6, 9, 2, 8, 5, 24, 19, 2, 2, 33, 5, 11, 2, 2, 7, 14, 3, 3, 2, 2, 3, 2, 5, 22, 2, 19, 2, 36, 10, 3, 38, 13, 37, 8, 9, 13, 2, 6, 6, 3, 2, 10, 26, 5, 4, 4, 2, 7, 10, 3, 2, 2, 3, 40, 3, 25, 3, 3, 26, 9, 20, 11, 18, 2, 5, 10, 33, 2, 2, 12, 6, 2, 3, 16, 10, 2, 30, 19, 2, 17, 4, 2, 7, 8, 3, 2, 2, 7, 8, 9, 36, 2, 2, 6, 3, 2, 32, 39, 3, 32, 2, 2, 8, 31, 2, 2, 6, 8, 3, 3, 3, 2, 37, 2, 1, 2, 9, 4, 2, 29, 2, 29, 2, 2, 2, 28, 12, 4, 3, 7, 2, 40, 9, 8, 3, 14, 9, 12, 2, 8, 38, 5, 2, 9, 2, 2, 2, 2, 25, 24, 3, 3, 14, 3, 4, 20, 2, 2, 4, 5, 10, 40, 6, 4, 17, 12, 6, 13, 7, 3, 2, 3, 2, 33, 3, 5, 7, 3, 2, 2, 2, 12, 4, 36, 14, 31, 2, 6, 12, 39, 14, 39, 5, 9, 2, 5, 2, 8, 2, 4, 2, 9, 2, 7, 9, 2, 8, 4, 9, 33, 2, 2, 18, 8, 34, 26, 16, 6, 5, 33, 12, 8, 2, 8, 14, 24, 2, 6, 2, 20, 3, 2, 2, 2, 2, 4, 3, 17, 4, 13, 4, 3, 32, 7, 6, 2, 2, 29, 2, 10, 21, 4, 4, 40, 1, 6, 2, 6, 6, 4, 9, 14, 20, 12, 2, 13, 4, 26, 2, 3, 5, 2, 15, 8, 6, 2, 21, 2, 36, 2, 4, 2, 9, 8, 5, 2, 2, 5, 30, 7, 22, 2, 2, 10, 3, 6, 12, 3, 2, 3, 4, 21, 7, 2, 23, 21, 22, 6, 20, 2, 3, 32, 28, 2, 10, 5, 17, 2, 31, 22, 3, 3, 7, 2, 13, 5, 22, 2, 2, 2, 2, 9, 2, 3, 2, 21, 9, 6, 2, 11, 2, 11, 3, 2, 33, 2, 2, 24, 3, 13, 8, 22, 27, 2, 3, 2, 5, 2, 3, 23, 2, 4, 3, 17, 2, 14, 6, 2, 2, 10, 5, 3, 2, 4, 3, 2, 2, 27, 11, 2, 7, 2, 3, 4, 4, 26, 2, 1, 38, 15, 3, 2, 13, 14, 5, 12, 5, 4, 4, 5, 33, 26, 11, 5, 12, 4, 3, 25, 2, 3, 29, 6, 4, 7, 3, 2, 2, 2, 2, 3, 2, 2, 2, 21, 7, 6, 3, 25, 6, 1, 20, 4, 33, 2, 15, 1, 3, 5, 32, 22, 4, 2, 13, 11, 10, 10, 7, 8, 3, 4, 8, 37, 14, 6, 22, 30, 6, 15, 36, 2, 25, 35, 5, 4, 2, 3, 16, 2, 2, 2, 5, 2, 2, 5, 22, 22, 3, 29, 2, 2, 5, 34, 2, 2, 19, 2, 10, 2, 19, 2, 2, 32, 2, 24, 5, 5, 19, 11, 9, 5, 2, 3, 28, 2, 35, 2, 13, 2, 11, 4, 2, 4, 2, 26, 22, 3, 4, 3, 2, 4, 3, 20, 4, 4, 2, 2, 9, 38, 8, 4, 2, 18, 4, 3, 2, 7, 2, 15, 27, 4, 6, 3, 3, 37, 2, 4, 13, 3, 2, 3, 4, 26, 18, 3, 2, 9, 3, 10, 2, 7, 12, 4, 21, 10, 2, 27, 2, 2, 31, 15, 2, 2, 23, 2, 1, 2, 2, 31, 2, 4, 5, 2, 3, 2, 26, 31, 2, 2, 27, 2, 2, 7, 3, 5, 32, 3, 30, 5, 16, 15, 2, 3, 3, 7, 39, 8, 2, 26, 2, 13, 3, 4, 38, 3, 2, 23, 33, 2, 14, 2, 6, 2, 2, 3, 12, 32, 3, 2, 2, 17, 35, 10, 2, 17, 18, 2, 31, 2, 23, 38, 2, 6, 23, 2, 8, 3, 2, 2, 5, 26, 5, 2, 2, 38, 2, 30, 7, 3, 6, 40, 20, 2, 3, 22, 2, 2, 23, 8, 27, 2, 3, 4, 18, 3, 38, 3, 2, 4, 20, 3, 4, 2, 2, 26, 8, 2, 3, 3, 32, 5, 2, 10, 3, 2, 2, 7, 5, 27, 6, 30, 26, 2, 6, 23, 26, 8, 18, 38, 17, 5, 2, 37, 34, 2, 19, 5, 16, 39, 5, 18, 19, 3, 3, 5, 34, 5, 31, 38, 2, 2, 3, 10, 12, 15, 2, 3, 2, 28, 11, 2, 6, 37, 2, 11, 14, 7, 6, 2, 1, 17, 14, 2, 9, 6, 6, 5, 2, 2, 3, 3, 6, 2, 3, 3, 2, 4, 5, 11, 18, 6, 8, 12, 11, 2, 2, 2, 3, 2, 5, 6, 2, 11, 7, 13, 16, 23, 7, 3, 6, 30, 7, 4, 2, 14, 2, 3, 16, 3, 36, 2, 7, 2, 2, 7, 4, 4, 2, 29, 5, 2, 25, 6, 2, 2, 6, 2, 12, 3, 23, 3, 14, 4, 3, 40, 40, 2, 2, 7, 21, 9, 2, 22, 13, 7, 3, 2, 4, 2, 2, 5, 4, 4, 29, 2, 2, 12, 9, 4, 26, 36, 3, 3, 4, 39, 3, 25, 2, 12, 15, 2, 2, 2, 2, 2, 2, 2, 2, 3, 5, 2, 27, 16, 35, 27, 7, 7, 2, 7, 31, 2, 27, 4, 2, 2, 6, 32, 6, 3, 4, 2, 2, 16, 3, 2, 3, 2, 7, 2, 5, 2, 6, 5, 2, 3, 4, 3, 4, 3, 2, 2, 2, 4, 6, 2, 5, 19, 21, 3, 9, 3, 24, 30, 2, 39, 30, 13, 2, 4, 21, 4, 33, 25, 38, 2, 13, 30, 4, 17, 8, 19, 6, 4, 3, 12, 3, 8, 11, 18, 2, 22, 11, 27, 4, 11, 30, 2, 32, 14, 3, 7, 21, 8, 3, 27, 3, 28, 3, 3, 4, 28, 4, 11, 3, 4, 2, 20, 10, 6, 6, 2, 18, 2, 3, 2, 3, 23, 2, 1, 12, 3, 6, 3, 3, 3, 3, 2, 2, 9, 3, 5, 4, 3, 5, 6, 10, 6, 3, 39, 6, 3, 2, 6, 3, 2, 6, 5, 17, 7, 27, 4, 23, 2, 7, 11, 31, 16, 2, 3, 2, 7, 4, 29, 36, 28, 2, 16, 5, 3, 6, 14, 7, 9, 2, 3, 9, 18, 33, 31, 1, 24, 3, 7, 8, 3, 13, 28, 6, 2, 5, 2, 2, 13, 3, 5, 6, 35, 6, 6, 2, 8, 9, 27, 2, 9, 17, 2, 7, 12, 26, 33, 2, 3, 10, 3, 2, 10, 20, 5, 4, 29, 28, 2, 4, 2, 2, 34, 21, 10, 9, 13, 32, 14, 5, 24, 36, 21, 2, 35, 11, 7, 2, 5, 2, 2, 9, 12, 11, 38, 31, 5, 4, 3, 4, 4, 8, 4, 2, 16, 19, 3, 2, 3, 13, 8, 4, 21, 2, 2, 2, 3, 4, 28, 34, 27, 6, 5, 9, 11, 8, 2, 1, 4, 38, 25, 2, 2, 2, 9, 2, 4, 34, 2, 34, 2, 5, 25, 15, 15, 8, 2, 5, 2, 2, 2, 10, 9, 2, 4, 14, 34, 35, 4, 1, 32, 13, 2, 3, 2, 23, 6, 4, 32, 3, 2, 2, 2, 11, 3, 19, 2, 2, 3, 2, 8, 7, 2, 19, 13, 2, 10, 2, 15, 13, 7, 6, 2, 19, 7, 5, 13, 10, 2, 4, 2, 2, 9, 2, 3, 27, 5, 2, 3, 24, 3, 23, 2, 7, 22, 11, 2, 3, 23, 5, 4, 7, 2, 32, 27, 2, 35, 3, 2, 2, 5, 3, 27, 9, 17, 9, 2, 3, 29, 5, 8, 4, 5, 3, 3, 2, 6, 2, 2, 10, 29, 33, 2, 5, 2, 31, 2, 2, 2, 2, 20, 4, 2, 23, 2, 29, 2, 2, 6, 28, 38, 3, 2, 9, 5, 5, 6, 2, 7, 7, 28, 3, 3, 2, 3, 15, 10, 3, 2, 4, 5, 2, 30, 5, 2, 3, 2, 14, 8, 2, 9, 11, 5, 2, 2, 2, 23, 27, 2, 16, 10, 2, 9, 35, 10, 11, 2, 2, 7, 3, 15, 12, 8, 29, 2, 5, 3, 4, 2, 1, 3, 4, 26, 35, 4, 2, 30, 2, 5, 6, 5, 3, 7, 18, 7, 2, 2, 3, 3, 2, 5, 2, 3, 10, 2, 37, 21]
dl=CountChain(7)
print (len(ref)//30)
for i in ref[0:len(ref)//50]:
    dl.push(i)
print(dl.hit_ratio())
# d_l = CountChain(7)
# # for j in range(8):
# #     d.push(j)
# # print(d.new_boundary.data, d.old_boundary.data)
# # print('f', d.freq_count_display())
#
# p_list = [i for i in range(1, 8)] + [1, 1, 5, 6, 1, 2, 8, 3, 4, 7, 5, 3, 2] + [1,5,7,2,3,5,1,3,7,2]
# n_n = lambda x: None if x is None else x.data
# for i in p_list:
#     d_l.push(i)
#     print(f'\nboundary {i} | old-> {n_n(d_l.old_boundary)}  | new-> {n_n(d_l.new_boundary)}')
#     print(f'details {i}: ', d_l.details_display())
#
# print('f_count:', d_l.freq_count_display())
# print('d_data:', d_l.data_display())
# print(d_l.average_count)
# print(len(d_l.table))
# print(d_l.hit_ratio())