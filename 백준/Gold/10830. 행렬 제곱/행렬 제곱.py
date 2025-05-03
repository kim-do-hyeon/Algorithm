def matrix_mul(A, B, mod=1000):
    N = len(A)
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= mod
    return result

def matrix_pow(A, power):
    if power == 1:
        return [[x % 1000 for x in row] for row in A]

    half = matrix_pow(A, power // 2)
    half_squared = matrix_mul(half, half)

    if power % 2 == 0:
        return half_squared
    else:
        return matrix_mul(half_squared, A)

# 입력
N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
result = matrix_pow(A, B)
for row in result:
    print(*row)