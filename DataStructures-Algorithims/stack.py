from collections import deque

stk = []

stk.append(5)
stk.append(3)
stk.append(4)

x = stk.pop()

print(x)
print(stk)

if stk:
    print("stack is not empty")
    stk.pop()
else:
    print("stack is empty")


# queue (kuyruk)
q = deque()


q.append(5)
q.append(3)
q.append(4)

x = q.popleft()
print(f"{x} is removed from the queue")
print(q)
