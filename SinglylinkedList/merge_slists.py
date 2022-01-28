from SinglyList import SinglyList
from sort_SList import sort_slist

def merge_slists(x, y):
    """ 두개의 단순연결리스트를 병합시켜주는 함수 """
    result = SinglyList()

    x = sort_slist(x)
    y = sort_slist(y)
    
    while not x.is_empty() and not y.is_empty():
        if min(x.head().data(), y.head().data()) == x.head().data():
            result.insert_last(x.delete_first())
        else:
            result.insert_last(y.delete_first())
        
        if x.is_empty():
            while not y.is_empty():
                result.insert_last(y.delete_first())
        if y.is_empty():
            while not x.is_empty():
                result.insert_last(x.delete_first())
    return result

    raise NotImplementedError

if __name__ == "__main__":
    x = SinglyList()
    y = SinglyList()
    for i in range(10):
        x.insert_last(i*2+1) #홀수인 data삽입 노드 연결
        y.insert_last(i*2)   #짝수인 data삽입 노드 연결
    print(x)
    print(y)
    
    z = merge_slists(x, y)
    print(z)