# 백준 11944 - NN

N, M = map(int, input().split())

result = ""
for i in range(N) :
    result += str(N)
print(result[:M])