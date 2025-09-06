# 백준 1145 - 적어도 대부분의 배수

from itertools import combinations
import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def lcm_multiple(nums):
    result = nums[0]
    for n in nums[1:]:
        result = lcm(result, n)
    return result

A = list(map(int, input().split()))
results = []
for comb in combinations(A, 3):
    results.append(lcm_multiple(comb))

print(min(results))