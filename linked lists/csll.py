class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def joinlst(self):
        temp=self.head
        while temp:
            temp=temp.next
        temp.next=self.head
    def insertatbeg(self,data):
        bn=Node(data)
        bn.next=self.head
        self.head=bn
        joinlst()
    def insertatend(self,data):
        en=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=en
        en.next=None
        joinlst()
    def insertatmid(self,index,data):
        mn=Node(data)
        temp=self.head
        for i in range(index-1):
            temp=temp.next
        mn.next=temp.next
        temp.next=mn
    def deleteatbeg(self):
        self.head=self.head.next
        joinlst()
    def deleteatend(self):
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None
        joinlst()
    def deleteatmid(self,index):
        temp=self.head
        for i in range(index-1):
            temp=temp.next
        temp.next=temp.next.next
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
                    print(temp.data,"->",self.head)
                    temp=temp.next
    def search(self,x):
        l=[]
        temp=self.head
        while(temp):
            l.append(temp.data)
            temp=temp.next
        if x in l:
            print("found")
        else:
            print("not found")
    def length(self):
        temp=self.head
        count=1
        while temp.next:
            count+=1
            temp=temp.next
        print(count)
    def reverse(self):
       prev = None
       current = self.head
       while(current is not None):
           next = current.next
           current.next = prev
           prev = current
           current = next
       self.head = prev
    def sortlist(self):
        l=[]
        temp=self.head
        while temp:
            l.append(temp.data)
            temp=temp.next
        l.sort()
        for i in range(0,len(l)):
            if(i==len(l)-1):
                print(l[i])
            else:
                print(l[i],end=" -> ")
obj=sll()
n1= Node(10)
obj.head=n1
n2=Node(20)
obj.head.next=n2
n3=Node(30)
n2.next=n3
obj.display()
print("insert at begin")
obj.insertatbeg(110)
obj.display()
print("insert at begin")
obj.insertatbeg(11)
obj.display()
print("insert at end")
obj.insertatend(100)
obj.display()
print("insert at end")
obj.insertatend(101)
obj.display()
print("insert at position")
obj.insertatmid(3,201)
obj.display()
print("delete at begin")
obj.deleteatbeg()
obj.display()
print("delete at end")
obj.deleteatend()
obj.display()
print("delete at position")
obj.deleteatmid(2)
obj.display()
print("search")
obj.search(10)
obj.display()
print('length')
obj.length()
print("reverse")
obj.reverse()
obj.display()
print("sort")
obj.sortlist()
obj.display()