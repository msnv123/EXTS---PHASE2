class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stackll:
    def __init__(self):
        self.head=None
    def enqueue(self,data):
        en=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=en
        en.next=None
    def dequeue(self):
        self.head=self.head.next
    def display(self):
        if self.head is None:
            print("LL Empty")
        else:
            temp=self.head
            while temp:
                if(temp.next!=None):
                    print(temp.data,"->", end=" ")
                    temp=temp.next
                else:
                    print(temp.data, end=" ")
                    temp=temp.next
obj=stackll()
n=Node(100)
obj.head=n
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.enqueue(40)
obj.display()
print("")
obj.dequeue()
obj.display()
print("")
obj.enqueue(32)
obj.display()