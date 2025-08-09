N = int(input())

for _ in range(N):
    N_list = list(map(int, input().split()))
    N_list.sort()
    if N_list[3] - N_list[1] >= 4:
        print("KIN")
    else:
        print(sum(N_list[1:4]))