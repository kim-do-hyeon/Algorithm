# [브론즈 2] 백준 1718 - 암호

S = input().rstrip()
KEY = input().rstrip()

LONG_KEY = ""
while len(LONG_KEY) < len(S):
    LONG_KEY += KEY

result = []
for i in range(len(S)):
    if S[i] == " ":
        result.append(" ")
    else:
        c = ord(S[i]) - ord('a')
        k = ord(LONG_KEY[i]) - ord('a')
        dec = (c - (k+1)) % 26
        result.append(chr(dec + ord('a')))

print("".join(result))