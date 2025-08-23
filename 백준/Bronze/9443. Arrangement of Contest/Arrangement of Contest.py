# 백준 9443 - Arrangement of Contest

N = int(input())
first_letters = set()

for _ in range(N):
    title = input().strip()
    first_letters.add(title[0])

result = 0
for ch in range(ord('A'), ord('Z') + 1):
    if chr(ch) in first_letters:
        result += 1
    else:
        break

print(result)