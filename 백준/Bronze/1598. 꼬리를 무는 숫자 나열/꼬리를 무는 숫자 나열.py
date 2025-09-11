# [브론즈 3] 백준 1598 - 꼬리를 무는 숫자 나열

A, B = map(int, input().split())
A -= 1
B -= 1
print(abs(A // 4 - B // 4) + abs(A % 4 - B % 4))