import sys

def main():
    tokens = sys.stdin.read().split()
    t = int(tokens[0])
    idx = 1
    outputs = []

    for _ in range(t):
        # 재료 (반죽용)
        cm = int(tokens[idx]); idx += 1
        y = int(tokens[idx]); idx += 1
        ssu = int(tokens[idx]); idx += 1
        ssa = int(tokens[idx]); idx += 1
        f = int(tokens[idx]); idx += 1

        # 토핑 재료
        b = int(tokens[idx]); idx += 1
        gs = int(tokens[idx]); idx += 1
        gc = int(tokens[idx]); idx += 1
        w = int(tokens[idx]); idx += 1

        # 만들 수 있는 반죽 최대 개수
        batter_max = min(
            2 * cm,          # 우유
            2 * y,           # 계란 노른자
            4 * ssu,         # 설탕
            16 * ssa,        # 소금
            (16 * f) // 9    # 밀가루 (정수 나눗셈)
        )

        # 토핑으로 만들 수 있는 팬케이크 개수
        topping_total = (
            b +          # 바나나 팬케이크
            gs // 30 +   # 딸기 팬케이크
            gc // 25 +   # 초콜릿 팬케이크
            w // 10      # 호두 팬케이크
        )

        # 실제로 만들 수 있는 팬케이크 최대 개수
        outputs.append(str(min(batter_max, topping_total)))

    sys.stdout.write("\n".join(outputs))

if __name__ == "__main__":
    main()
