def solution(arr):
    def compress(r, c, size):
        value = arr[r][c]
        for i in range(r, r + size):
            for j in range(c, c + size):
                if arr[i][j] != value:
                    half = size // 2
                    a = compress(r, c, half)
                    b = compress(r, c + half, half)
                    c_ = compress(r + half, c, half)
                    d = compress(r + half, c + half, half)
                    return [a[0] + b[0] + c_[0] + d[0], a[1] + b[1] + c_[1] + d[1]]
        return [1, 0] if value == 0 else [0, 1]

    return compress(0, 0, len(arr))