# 백준 11047 - 동전 0
# 분류 : 그리디

N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
A.reverse()

count = 0
while K > 0 :
    for i in A :
        if K // i >= 1 :
            count += K // i
            K = K % i
            
print(count)