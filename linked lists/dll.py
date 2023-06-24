class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head==None:
            print("dll not created")
        else:
            temp=self.head
            while temp.next:
                print(temp.data,end=" <--> ")
                temp=temp.next
            print(temp.data)
    def insertatbeg(self,data):
        n=Node(data)
        n.prev=None
        n.next=self.head
        self.head.prev=n
        self.head=n
    def insertatend(self,data):
        n=Node(data)
        n.next=None
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=n
        n.prev=temp
    def insertatpos(self,index,data):
        n=Node(data)
        temp=self.head
        for i in range(index-1):
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n
    def deleteatbeg(self):
        temp=self.head
        self.head=temp.next
    def deleteatend(self):
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next.prev=None
        temp.next=None
    def deleteatpos(self,index):
        temp=self.head
        for i in range(index-1):
            temp=temp.next
        if(temp.next.next!=None):
            temp.next.next.prev=temp
            temp.next=temp.next.next
        else:
            print("no")
obj=dll()
n1=Node(10)
obj.head=n1
n2=Node(20)
n2.prev=n1
n1.next=n2
obj.display()
print(" ")
obj.insertatbeg(35)
obj.display()
print(" ")
obj.insertatend(40)
obj.display()
print("")
obj.insertatpos(2,32)
obj.display()
print("")
obj.deleteatbeg()
obj.display()
print("")
obj.deleteatend()
obj.display()
print("sss")
obj.deleteatpos(1)
obj.display()