'''Queue using Arrays insertion and deletion happens at two different ends
rear and front
FIFO
'''
queue=[]
def enqueue():
    print("Enter element to enqueue: ")
    elmnt=int(input())
    queue.append(elmnt)
    print(queue)
def dequeue():
    queue.remove(queue[0])
# can also use queue.pop(0)
    print(queue)
while True:
    print("Select Operation: 1.Enqueue 2.Dequeue 3.Quit")
    opt = int(input())
    if opt==1:
        enqueue()
    elif opt==2:
        dequeue()
    elif opt==3:
        break
    else:
        print("choose correct option")