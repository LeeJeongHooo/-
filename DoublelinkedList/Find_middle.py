""" 이중연결 리스트의 중간의 노드를 찾아주는 함수 구현 """
from DoublelinkedList import DoublelinkedList

def find_dlist_middle_node(x):
    search_middle = x._header.next()
    cnt = 0
    while (x._header.next() != x._trailer):     #trailer가 아닐때까지 갯수 탐색
        cnt = cnt + 1
        x._header = x._header.next()
    middle_index = int(cnt/2)                   #중간의 인덱스값 설정
        
    
    
    for i in range(middle_index):               #중간의 노드까지 탐색
        search_middle = search_middle.next()
        
    return search_middle

""" search middle index Test case """
d = DoublelinkedList()
for i in range(1,8):
    d.insert_last(i)

print(d)    

print(find_dlist_middle_node(d))                #중간의 노드 출력