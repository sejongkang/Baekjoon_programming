from sys import stdin
deque = []
for _ in range(int(stdin.readline())):
    arr = stdin.readline().split()
    if arr[0] == 'push_front':
        deque.insert(0, arr[1])
    if arr[0] == 'push_back':
        deque.append(arr[1])
    elif arr[0] == 'pop_front':
        if deque: print(deque.pop(0))
        else: print(-1)
    elif arr[0] == 'pop_back':
        if deque: print(deque.pop(-1))
        else: print(-1)
    elif arr[0] == 'size': print(len(deque))
    elif arr[0] == 'empty': print(1-int(bool(deque)))
    elif arr[0] == 'front':
        if deque: print(deque[0])
        else: print(-1)
    elif arr[0] == 'back':
        if deque: print(deque[-1])
        else: print(-1)

    else: pass
