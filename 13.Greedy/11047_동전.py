from sys import stdin

if __name__ == '__main__':

    s_in = list(map(int, stdin.readline().strip().split()))
    num = s_in[0]
    total = s_in[1]

    coins = []
    for i in range(num):
        coins.append(int(input()))
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        count += (total // coin)
        total %= coin
        if total == 0:
            break
    print(count)


