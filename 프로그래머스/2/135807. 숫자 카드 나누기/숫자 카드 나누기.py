from math import gcd
from functools import reduce

def check(a, arr) :
    for num in arr :
        if num % a == 0 :
            return False
    return True

def solution(arrayA, arrayB):
    answer = 0
    gcdA = reduce(gcd, arrayA)
    gcdB = reduce(gcd, arrayB)
    
    a = 0
    b = 0
    
    if check(gcdA, arrayB) :
        a = gcdA
    if check(gcdB, arrayA) :
        b = gcdB
    
    answer = max(a, b)
    return answer