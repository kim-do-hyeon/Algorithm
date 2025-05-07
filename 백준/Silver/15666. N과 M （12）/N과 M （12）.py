# 백준 15666 - N과 M (12)
# 분류 : 백트래킹

N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums = sorted(list(set(nums)))

result = []

def back(start, depth) :
    if depth == M :
        print(' '.join(map(str, result)))
        return
    for i in range(start, len(nums)) :
        result.append(nums[i])
        back(i, depth + 1)
        result.pop()

back(0, 0)