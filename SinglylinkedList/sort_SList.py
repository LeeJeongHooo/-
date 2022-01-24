#SignlyList 모듈 

from SinglyList import SinglyList 

def sort_slist(target):
    sorted = SinglyList()
    sorted.insert_first(target.delete_first().data()) #SinglyList 하나 늘려서 삽입정렬 수행

    while not target.is_empty():
        new_item = target.delete_first()
        node = sorted.head()
        
        if sorted.tail().data() < new_item.data(): #새로운 값이 마지막 노드보다 큼
            sorted.insert_last(new_item.data())
            
        else: # 새로운 값이 마지막 노드보다 작음
            node = sorted.head() #헤드부터 다시 탐색

            if sorted.head().data() > new_item.data(): #만약 헤드보다 작은 값이면 맨앞에 삽입
                sorted.insert_first(new_item.data())
            else:
                while node.next().data() < new_item.data(): #기존 노드들 보다 커지는 지점 탐색
                    node = node.next()
                
                sorted.insert_next(new_item.data(),node) #커지는 지점 바로 앞노드에서 next삽입
    return sorted
#미리 정렬시키기위해 만든 함수정의

"""test case"""
s = SinglyList()
s.insert_first("1")
s.insert_first("3")
s.insert_last("2")
s.insert_first("5")
print(s)

"""정렬된 상태로 변환"""
s = sort_slist(s)
print(s)