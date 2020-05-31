# import sys
# n = int(input())
# l = []
# for i in range(n):
#     l.append(int(sys.stdin.readline()))
# for i in sorted(l):
#     sys.stdout.write(str(i)+'\n')

v = [int(input()) for i in range(int(input()))]  # 입력

# merge sort
def merge(left, right):
    v = list()
    i = 0;
    j = 0
    while (i < len(left) and j < len(right)):
        if left[i] <= right[j]:
            v.append(left[i])
            i += 1
        else:
            v.append(right[j])
            j += 1
    if i == len(left): v = v + right[j:len(right)]
    if j == len(right): v = v + left[i:len(left)]
    return v

def merge_sort(v):
    if len(v) <= 1: return v
    m = len(v) // 2
    left = merge_sort(v[0:m])
    right = merge_sort(v[m:len(v)])
    return merge(left, right)

if __name__ == '__main__':
    m = merge_sort(v)
    print(*m, sep="\n")

# 퀵 정렬 시
# import sys
# 
# n = int(sys.stdin.readline())
# num_list = []
# while (n > 0):  # 인자를 받아서 리스트에 담는다
#     n -= 1
#     num_list.append(int(sys.stdin.readline()))
# 
# 
# def quick_sort(li, start, end):
# 
#     if end <= start:
#         return li
# 
#     pivot = li[(start + end) // 2]  # 가운데 값을 피벗으로
# 
#     left = start
#     right = end
#     while left <= right:
#         while li[left] < pivot:
#             left += 1
#         while li[right] > pivot:
#             right -= 1
#         print(li)
#         if left <= right:  # left와 right가 교차하지 않았으면
#             li[left], li[right] = li[right], li[left]
#             left, right = left + 1, right - 1
# 
#     quick_sort(li, start, left - 1)
#     quick_sort(li, left, end)
# 
# 
# quick_sort(num_list, 0, len(num_list) - 1)
# 
# for i in num_list:
#     print(i)