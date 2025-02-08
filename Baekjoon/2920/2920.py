# 백준 2920 - 음계
# 분류 : 구현

numbers = list(map(int, input().split()))
if numbers == [1, 2, 3, 4, 5, 6, 7, 8] :
    print("ascending")
elif numbers == [8, 7, 6, 5, 4, 3, 2, 1] :
    print("descending")
else :
    print("mixed")