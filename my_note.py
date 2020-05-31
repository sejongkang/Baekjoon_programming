
# 트리
class Node:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def set_data(self, data):
        self.data = data

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

class Tree:
    def __init__(self, root):
        self.root = root

    def set_root(self, root):
        self.root = root

    def get_root(self):
        return self.root

    def preorder(self, node):
        if (not node == None):
            print(node.data, end='')
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if (not node == None):
            self.inorder(node.left)
            print(node.data, end='')
            self.inorder(node.right)

    def postorder(self, node):
        if (not node == None):
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end='')


# 이분 탐색
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


# 병합 정렬
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


# 퀵 정렬
def quick_sort(li,start,end):
    if end <= start:
        return li

    pivot = li[(start + end) // 2]#가운데 값을 피벗으로

    left=start
    right=end
    while left <= right:
        while li[left] < pivot:
            left += 1
        while li[right] > pivot:
            right -= 1
        print(li)
        if left <= right: #left와 right가 교차하지 않았으면
            li[left], li[right] = li[right], li[left]
            left, right = left + 1, right - 1

    quick_sort(li,start, left - 1)
    quick_sort(li,left, end)


# 삽입 정렬
def insert_sort(nums):
    for i in range(1, len(nums)):
        while (i > 0) & (nums[i] < nums[i - 1]):
            nums[i], nums[i - 1] = nums[i - 1], nums[i]

            i -= 1


# 버블 정렬
def bubble_sort(numbers):
    for i in range(len(numbers)) :
        for j in range(len(numbers)) :
            if numbers[i] < numbers[j] :
                numbers[i], numbers[j] = numbers[j], numbers[i]