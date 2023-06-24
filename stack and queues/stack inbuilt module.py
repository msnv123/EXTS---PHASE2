from queue import LifoQueue
s=LifoQueue(maxsize=10)
print(s.qsize())
s.put(1)
s.put(2)
s.put(3)
for i in range(0,s.qsize()):
    print(s.get())
s.empty()