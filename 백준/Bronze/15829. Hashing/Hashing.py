# 백준 15829 - Hashing
# 분류 : 해쉬

L = int(input())
S = input()

mod = 1234567891
po = [0] * L
po[0] = 1
for i in range(1, L) :
    po[i] = po[i - 1] * 31 % mod

H = 0
for i in range(L) :
    H += (ord(S[i]) - ord('a') + 1) * po[i] % mod
    H %= mod

print(H)