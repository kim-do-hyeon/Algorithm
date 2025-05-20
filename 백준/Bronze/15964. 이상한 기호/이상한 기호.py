# 백준 15964 - 이상한 기호

def calc(A, B) :
    return (A + B) * (A - B)
A, B = map(int, input().split())

print(calc(A, B))