import sys
input = sys.stdin.read

MAX = 1000000
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX + 1, i):
            is_prime[j] = False

primes = [i for i, val in enumerate(is_prime) if val]

data = list(map(int, input().split()))

output = []

for N in data:
    if N == 0:
        break
    found = False
    for p in primes:
        if p > N // 2:
            break
        if is_prime[N - p]:
            output.append(f"{N} = {p} + {N - p}")
            found = True
            break
    if not found:
        output.append("Goldbach's conjecture is wrong.")

print('\n'.join(output))