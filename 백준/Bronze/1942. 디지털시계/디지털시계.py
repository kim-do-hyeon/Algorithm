def multiple_of_3(h, m, s):
    return 1 if int(''.join(map(lambda x: str(x).zfill(2), [h, m, s]))) % 3 == 0 else 0

for _ in range(3):
    start, end = map(lambda x: x.split(':'), input().split())
    sh, sm, ss = map(int, start)
    eh, em, es = map(int, end)

    count = 0

    while 1:
        count += multiple_of_3(sh, sm, ss)

        ss += 1

        if 60 <= ss:
            ss = 0
            sm += 1
        
        if 60 <= sm:
            sm = 0
            sh += 1

        if 24 <= sh:
            sh = 0
            sm = 0
            ss = 0

        if (sh == eh) and (sm == em) and (ss == es):
            count += multiple_of_3(sh, sm, ss)
            break

    print(count)