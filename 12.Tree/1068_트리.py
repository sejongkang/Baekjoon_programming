from sys import stdin

def bfs(num, root, table, check):
    count = 0
    que = [root]
    check[root] = 1
    while que:
        node = que.pop(0)
        end = 1
        for i in range(num):
            if table[node][i] == 1 and not check[i]:
                que.append(i)
                check[i] = 1
                end = 0
        if end:
            count += 1
    print(count)



if __name__ == '__main__':
    # 반례
    # 5
    # 4 4 4 4 -1
    # 1

    num = int(input())
    parents = list(map(int, stdin.readline().strip().split()))
    remove = int(input())

    table = []
    check = []
    for i in range(num):
        tmp = []
        for j in range(num):
            tmp.append(0)
        table.append(tmp)
        check.append(0)

    for i in range(len(parents)):
        if parents[i] == -1:
            root = i
        else:
            table[i][parents[i]] = 1
            table[parents[i]][i] = 1

    for i in range(num):
        table[remove][i] = 0
        table[i][remove] = 0

    if remove == root:
        print(0)
    else:
        bfs(num, root, table, check)