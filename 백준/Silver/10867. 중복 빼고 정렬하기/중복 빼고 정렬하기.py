# 백준 10867 - 중복 빼고 정렬하기

import sys
input = sys.stdin.readline
N = int(input())
A = list(set(list(map(int, input().split()))))
A.sort()
print(" ".join(map(str, A)))