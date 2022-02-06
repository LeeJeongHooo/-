""" 단순연결리스트 중간노드찾는 함수 구현 """

from SinglyList import SinglyList

def find_slist_middle_node(x): 
    search_middle = x.head()
    fast_search_middle = x.head()
    while fast_search_middle and fast_search_middle.next():
        fast_search_middle = fast_search_middle.next().next()
        search_middle = search_middle.next()
    
    return search_middle   

s = SinglyList()

"""Test case"""
for i in range(1,8):
    s.insert_last(i)

print(s)

midnode_data = find_slist_middle_node(s) 

print(midnode_data)