# 백준 9093 - 단어 뒤집기
# 분류 : 자료구조

T = int(input())
for i in range(T) :
    S = input().split()
    for j in S :
        reverse_s = j[::-1]
        print(reverse_s, end = " ")
