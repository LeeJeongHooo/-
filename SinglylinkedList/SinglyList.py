""" '_'변수들은 사용하지 Class밖에서 사용하지 않는 것을 권장 """
""" 다음노드의 정보만를 가지고 있기 때문에 단순연결리스트는 바로 그 노드를 삭제 하지 못한다. """
""" 결국 노드의 다음노드를 삭제 할 수 있어도 이전 노드의 정보가 없기에 바로 가르키고있는 노드는 삭제 할 수 없다. """

class SinglyList:
    class _Node:
        def __init__(self, data = None, next = None):
            """data정보와 다음 연결된 node정보"""
            self._data = data
            self._next = next
        def data(self):
            return self._data

        def next(self):
            return self._next
        
        def set_data(self, data):
            self._data = data

        def set_next(self, next):
            self._next = next

        def __str__(self):
            return str(self._data)

    def __init__(self):  
        """모든 정보들을 자동적으로 초기화"""
        self._head = None
        self._tail = None #tail정보로 맨뒤에 삽입 O(1), 하지만 tail정보를 넣어도 맨뒤에 삭제는 O(n) 
                          #그 현재 위치의 노드를 바로 삭제할 수 없다는 것이 단순연결리스트의 특징
        
        self._size = 0    #노드의 갯수   
    
    def __len__(self):
        """len(SList)메소드 실행시 자동적으로 값 반환"""
        return self._size

    def __str__(self):
        """print(SList)시 자동으로 출력"""
        p = self._head
        set_str = ""
        while p:
            set_str += str(p.data()) + " -> "
            p = p.next()
        set_str += 'None'  
        return set_str  
    
    def is_empty(self):
        return self._head is None

    def head(self):
        return self._head

    def tail(self):
        return self._tail

    def insert_first(self, data):
        """맨 앞에 위치에 Node삽입하기"""
        if self.is_empty(): #노드가 한개도 없어서 비워있는 경우, head와 tail정보 모두 업데이트
            p = self._Node(data)      
            self._head = self._tail = p
        else: #head정보만 변경
            self._head = self._Node(data, self._head) #head가 새로운 노드를 가르키게 하고 기존의 노드를 이어준다.             
        self._size += 1

        return self._head

    def delete_first(self):
        """맨 앞에 위치에 노드 삭제 하기"""
        if self.is_empty():
            return False
        elif self._size == 1: #head가 가르키는 노드만 남아있을 경우/ 노드가 한개있는 경우
            p = self._head
            self._head = self._tail = None
        else: #여러개의 노드가 남아 있는 경우
            p = self._head
            self._head = self._head.next()

        self._size -= 1
        return p 

    def insert_next(self, data, p):
        """p가 가르키는 노드의 다음에 노드삽입"""
        p._next = self._Node(data, p._next) #p의 다음위치에 기존의 p의 next를 이어줄 노드 생성 후 삽입
        
        if p == self._tail:   #p가 tail일 경우 tail정보 업데이트
            self._tail = p._next

        self._size += 1
        return p._next    

    def delete_next(self, p):
        """p의 다음노드 삭제하기"""
        assert p

        if p == self._tail:  # tail뒤에 아무것도 존재 하지 않을 경우 index 오류
            raise IndexError("Underflow") 

        q = p._next #p의 다음노드를 q라고 설정
        p._next = q.next() #삭제하기위해 p의 다음노드를 q의 다음노드로 바꿈 자동으로 q가 연결이 끊어진다.
        if q == self._tail: #만약 삭제할려는 노드가 tail일 경우 p를 tail로 업데이트
            self._tail = p

        self._size -= 1
        return q        

    def insert_last(self, element):
        """맨뒤에 노드 삽입하기, insert_next함수를 이용해서 구현"""
        if self.is_empty():  # 비워있는 경우 head와 tail정보 모두 업데이트 
            p = self._Node(element)
            self._head = self._tail = p
            self._size += 1
            return p
        return self.insert_next(element, self._tail)

    def delete_last(self):
        """tail노드 삭제하기, delete_last함수를 이용해서 구현"""
        p = self._head
        if self._size == 1:  # 하나의 노드 밖에 없을 경우
            self._head = self._tail = None
            self._size -= 1
            return p
        """단순 연결리스트 마지막 노드를 지우기 위해서는 tail의 이전 노드의 정보를 알아야 된다."""
        while p._next._next: #p의 다음 다음 노드가 None일 때 까지 노드 search
            p = p._next 
        return self.delete_next(p) #while구문 반목으로 p가 tail 앞의 노드