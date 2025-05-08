# 백준 5639 - 이진 검색 트리
# 분류 : 트리

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

preorder = []
while True :
    try :
        preorder.append(int(input()))
    except :
        break

def postorder(start, end) :
    if start >= end :
        return
    root = preorder[start]

    right = start + 1
    while right < end and preorder[right] < root :
        right += 1
    
    postorder(start + 1, right)
    postorder(right, end)

    print(root)

postorder(0, len(preorder))