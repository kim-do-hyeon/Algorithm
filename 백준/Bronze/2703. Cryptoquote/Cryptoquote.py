import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    encrypted = sys.stdin.readline().rstrip("\n")
    rule = sys.stdin.readline().strip()

    result_chars = []

    for ch in encrypted:
        if ch == " ":
            result_chars.append(" ")
        else:
            idx = ord(ch) - ord('A')
            result_chars.append(rule[idx])

    print("".join(result_chars))
