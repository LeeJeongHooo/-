""" 이중연결리스트 """
""" 단순연결리스트의 단점을 보안하기 위해 만들어진 자료구조 """

class DoublelinkedList:
    class _Node:
        def __init__(self, data, prev, next):
            self._data = data
            self._prev = prev
            self._next = next

        def data(self):
            return self._data

        def next(self):
            return self._next

        def prev(self):
            return self._prev

        def set_data(self, data):
            self._data = data

        def set_next(self, next):
            self._next = next

        def set_prev(self, prev):
            self._prev = prev

        def __str__(self):
            return str(self._data)

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def __str__(self):
        
        p = self._header._next
        ret_str = '{}: '.format(self._size)
        ret_str += 'Header'
        while p is not self.trailer():
            ret_str += ' <-> {}'.format(p)
            p = p._next
        ret_str += ' <-> Trailer'
        return ret_str  

    def is_empty(self):
        return self._size == 0

    def header(self):
        return self._header

    def trailer(self):
        return self._trailer

    def insert_between(self, data, prede, succ):
        
        new_node = self._Node(data, prede, succ)
        prede._next = new_node
        succ._prev = new_node
        self._size += 1
        return new_node

    def insert_after(self, data, p):
        if p is self._trailer:
            return None
        else:
            return self.insert_between(data, p, p._next)

    def insert_before(self, data, p):
        if p is self._header:
            return None
        else:
            return self.insert_between(data, p._prev, p)

    def insert_first(self, data):
        return self.insert_after(data, self._header)

    def insert_last(self, data):
        return self.insert_before(data, self._trailer)

    def delete_node(self, node):
        
        if (node is self._header) or (node is self._trailer):
            return None

        prede = node._prev
        succ = node._next
        prede._next = succ
        succ._prev = prede
        self._size -= 1
        data = node._data
        node._prev = node._next = node._data = None 
        return data