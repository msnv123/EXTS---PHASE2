class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stackll:
    def __init__(self):
        self.head=None
    def push(self,data):
        n=Node(data)
        n.next=self.head
        self.head=n
    def pop(self):
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None
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
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.display()
obj.pop()
obj.display()

        