# 백준 18129 - 이상한 암호코드

data = input().split()
S = data[0].lower()
K = int(data[1])

seen = [False] * 26
res = []
current = S[0]
cnt = 0
S += " "
for ch in S :
    if ch == current :
        cnt += 1
    else :
        index = ord(current) - ord('a')
        if not seen[index] :
            res.append('1' if cnt >= K else '0')
            seen[index] = True
        current = ch
        cnt = 1

print("".join(res))