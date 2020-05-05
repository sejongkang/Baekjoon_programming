import sys
n = int(sys.stdin.readline())
result = 0
for _ in range(n):
    s = input().strip()
    stack = []
    for i in s:
        if not stack or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()
    if not stack:
        result += 1
print(result)