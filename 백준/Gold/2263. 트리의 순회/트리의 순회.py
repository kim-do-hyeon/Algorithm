# 백준 2263 - 트리의 순회
# 분류 : 트리

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
INORDER = list(map(int, input().split()))
POSTORDER = list(map(int, input().split()))

INDEX = {val : idx for idx, val in enumerate(INORDER)}

def build(in_start, in_end, post_start, post_end) :
    if in_start > in_end or post_start > post_end :
        return

    root = POSTORDER[post_end]
    print(root, end = ' ')
    root_index = INDEX[root]
    left_size = root_index - in_start

    build(in_start, root_index - 1, post_start, post_start + left_size - 1)
    build(root_index + 1, in_end, post_start + left_size, post_end - 1)

build(0, N - 1, 0, N - 1)