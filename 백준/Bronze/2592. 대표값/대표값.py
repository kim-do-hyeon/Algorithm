# 백준 2592 - 대표값

A = [int(input()) for _ in range(10)]
A_dict = {}
for i in A :
    if i in A_dict :
        A_dict[i] += 1
    else :
        A_dict[i] = 1
print(int(sum(A) / 10))
for key, value in A_dict.items() :
    if value == max(A_dict.values()) :
        print(key)