import sys
def bfs(arr, visit, a, b, n):
    que = [a]
    dist = [0]
    visit[a] = 1
    while(que):
        x = que.pop(0)
        d = dist.pop(0)
        if x == b:
            return d
        for i in range(1, n + 1):
            if arr[x][i] == 1 and not visit[i]:
                que.append(i)
                dist.append(d + 1)
                visit[i] = 1
    return -1

if __name__ == '__main__':
    s_in = list(map(int, input().split()))
    a, b = s_in[0], s_in[1]

    s_in = list(map(int, input().split()))
    n, m = s_in[0], s_in[1]

    arr = []
    visit = []
    for _ in range(n + 1):
        visit.append(0)
        tmp = []
        for k in range(n + 1):
            tmp.append(0)
        arr.append(tmp)

    for _ in range(m):
        s_in = list(map(int, input().split()))
        arr[s_in[0]][s_in[1]] = 1
        arr[s_in[1]][s_in[0]] = 1

    print(bfs(arr, visit, a, b, n))