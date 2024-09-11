class Node:
    def init(self, item, nextnode):
        self.item = item
        self.next = nextnode

class LinkedListPro:
    def init(self):
        self.first = None
    
    def is_empty(self):
        return self.first == None
    
    def enqueue(self, item):
        oldfirst = self.first
        self.first = Node(item, oldfirst)

    def dequeue(self):
        item = self.first.item
        self.first = self.first.next

    def find(self, key):
        curent = self.first
        while curent is not None:
            if curent.item == key:
                return True
            curent = curent.next
        return False

def main():
    llp = LinkedListPro()
    en = int(input())

    for _ in range(en):
        item = input()
        llp.enqueue(item)

    deq = int(input())

    for _ in range(deq):
        llp.dequeue()

    en = int(input())

    for _ in range(en):
        item = input()
        llp.enqueue(item)

    item = input()
    print(llp.find(item))

if __name__ == '__main__':
    main()