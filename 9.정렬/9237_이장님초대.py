from sys import stdin

if __name__ == '__main__':
    num = int(input())
    s_in = list(map(int, stdin.readline().strip().split()))

    max = 0
    s_in.sort(reverse=True)
    for i in range(num):
        tmp = (i + 2) + s_in[i]
        if tmp > max:
            max = tmp

    print(max)