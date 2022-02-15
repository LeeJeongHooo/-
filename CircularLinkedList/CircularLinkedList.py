""" 원형연결리스트는 마지막 노드의 레퍼런스가 저장된 last가 단순연결리스트의 head와 같은 역할 """

class CircularLinkedList:
    class _Node:
        def __init__(self, element, next=None):
            self._data = element
            self._next = next

        def element(self):
            return self._data

        def next(self):
            return self._next

        def __str__(self):
            return str(self._data)

    def __init__(self):
        self._last = None  #head가 존재하지않고 last로 만 이루어진 Circular Linked List
        self._size = 0     #연결된 노드의 갯수

    def __len__(self):
        """ 연결리트의 길이 """
        return self._size

    def __str__(self):
        if self.is_empty():     #빈 원형연결리스트일 경우
            return ""
        else:
            cstr = ''
            first = self._last.next() #last의 다음노드를 first노드로 설정
            p = first
            while p.next() != first:   #무한루프이기에 None이 존재하지 않고 first가 아닐때까지 반복
                cstr += str(p.element()) + ' -> '
                p = p.next()
            cstr += str(p.element())
        return cstr

    def is_empty(self):
        return self._last is None

    def first(self):
        if self.is_empty():
            raise Exception("Underflow")
        else:
            return self._last.next()

    def last(self):
        if self.is_empty():
            raise Exception("Underflow")
        else:
            return self._last

    def insert(self, element):
        """삽입은 last가 참조하는 부분에 노드를 삽입"""
        if self.is_empty():  # 원형연결리스트가 비워있을 경우 last를 그 새롭게 생성된 노드로 꼭 설정
            p = self._Node(element)
            self._last = p._next = p
        else:  
            self._last._next = self._Node(element, self._last._next)

        self._size += 1

    def delete(self):
        """삭제는 last가 참조하는 노드를 삭제한다."""
        assert self._size

        if self._size == 1:  # 원형연결리스트의 남은 노드의 갯수가 1개일 경우
            p = self._last
            self._last = None
        else:
            p = self._last._next
            self._last._next = p.next()

        self._size -= 1


if __name__ == "__main__":
    s = CircularLinkedList()
    s.insert('바나나')
    s.insert('사과')
    s.insert('포도')
    s.insert('키위')
    print(s)
    s.delete()
    print(s)
    s.delete()
    print(s)
    print(s.first())
    print(s.last())
