'''Stack
LIFO - Last In First Out
Stack implementation-
one - Using arrays
two - using linked list
three - using inbuilt modules
NOTE - insertion and delete happens at one end in stack which is on top
'''
#using arrays
stack=[]
def push():
    elmnt = int(input("Enter element to push into stack: "))
    stack.append(elmnt)
    print(stack)
def pop():
    stack.pop()
    print(stack)
while True:
    print("Select Operation: 1.Push 2.Pop 3.Quit")
    opt = int(input())
    if opt==1:
        push()
    elif opt==2:
        pop()
    elif opt==3:
        break
    else:
        print("choose correct option")    