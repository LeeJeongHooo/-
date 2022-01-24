"""Singlylinked List Testcase"""

from SinglyList import SinglyList 

if __name__ == "__main__":
    s = SinglyList()
    s.insert_first("1")
    s.insert_last("2")
    s.insert_last("3")
    s.insert_last("4") 
    print(s)


    s.insert_next("5", s.head().next()) 
    print(s)  