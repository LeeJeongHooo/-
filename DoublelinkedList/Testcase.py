""" Testcase """
from DoublelinkedList import DoublelinkedList

d = DoublelinkedList()
print(d)

d.insert_first("3")
d.insert_last("4")
d.insert_first("2")
d.insert_first("1")
d.insert_last("5")
print(d)

#단순연결리스트의 단점을 보안할 수 있게 만들어진 구조이기에 바로 지정한 노드를 삭제할 수 있다.
d.delete_node(d._header.next().next())
print(d)

d.delete_node(d._header.next())
print(d)