# 백준 1159 - 농구 경기

import sys
input = sys.stdin.readline
N = int(input())
datas = {}
for i in range(N) :
    name = input()
    if name[0] in datas :
        datas[name[0]] += 1
    else :
        datas[name[0]] = 1

results = []
for key, value in datas.items() :
    if value >= 5 :
        results.append(key)
results.sort()
if len(results) :
    print("".join(results))
else :
    print("PREDAJA")