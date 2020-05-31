from sys import stdin

def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

if __name__ == '__main__':
    num = int(input())
    cards = list(map(int, stdin.readline().strip().split()))
    num = int(input())
    is_cards = list(map(int, stdin.readline().strip().split()))
    cards.sort()

    for card in is_cards:
        print(binary_search(card, cards), end=' ')



