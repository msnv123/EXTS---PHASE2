stack=[]
temp=[]
def push():
    elmnt = int(input("Enter element to push into stack: "))
    stack.append(elmnt)
    print(stack)
def pop():
    stack.pop()
    print(stack)
while True:
    print("Select Operation: 1.Push 2.Pop 3.Quit 4.even 5.odd")
    opt = int(input())
    if opt==1:
        push()
    elif opt==2:
        pop()
    elif opt==3:
        break
    elif opt==4:
        for i in stack:
            if i%2==0:
                temp.append(i)
        print(temp)
        temp.clear()
    elif opt==5:
        for i in stack:
            if i%2!=0:
                temp.append(i)
        print(temp)
        temp.clear()
    else:
        print("choose correct option")    