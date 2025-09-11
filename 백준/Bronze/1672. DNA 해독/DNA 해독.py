# [브론즈 1] 백준 1672 - DNA 해독

DNA = {"AA" : "A",
        "AG" : "C",
        "AC" : "A",
        "AT" : "G",
        "GA" : "C",
        "GG" : "G",
        "GC" : "T",
        "GT" : "A",
        "CA" : "A",
        "CG" : "T",
        "CC" : "C",
        "CT" : "G",
        "TA" : "G",
        "TG" : "A",
        "TC" : "G",
        "TT" : "T"
}

N = int(input())
S = list(input())

while True :
    if len(S) == 1 :
        break
    SS = S[-2] + S[-1]
    if SS in DNA :
        del S[-2:]
        S.append(DNA[SS])
print(*S)