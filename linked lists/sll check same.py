'''2 ll and display same or not'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        bn=Node(data)
        bn.next=self.head
        self.head=bn
    def insertatend(self,data):
        en=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=en
        en.next=None
    def insertatmid(self,index,data):
        mn=Node(data)
        temp=self.head
        for i in range(index-1):
            temp=temp.next
        mn.next=temp.next
        temp.next=mn
    def deleteatbeg(self):
        self.head=self.head.next
    def deleteatend(self):
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None
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
                    print(temp.data, end=" ")
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
    def lister(self):
        temp=self.head
        l=[]
        while temp:
            l.append(temp.data)
            temp=temp.next
        return l
obj=sll()
obj1=sll()
n1= Node(10)
obj.head=n1
n=Node(20)
obj1.head=n
obj.insertatbeg(20)
obj1.insertatbeg(10)
obj.insertatbeg(30)
obj1.insertatbeg(40)
a=obj.lister()
b=obj1.lister()
if a==b:
    print("same")
else:
    print("not same")