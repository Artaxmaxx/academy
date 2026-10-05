from sys import call_tracing


def binary_sum(a :int, b :int):
    ad = list(map(int, str(a)))
    bd = list(map(int, str(b)))

    while len(ad) < len(bd):
        ad.insert(0, 0)
    while len(bd) < len(ad):
        bd.insert(0, 0)

    res = []
    carry = 0
    for i in range(1, len(ad) + 1):
        if ad[-i] + bd[-i] + carry == 0:
            res.append(0)
            carry = 0
        elif ad[-i] + bd[-i] + carry == 1:
            res.append(1)
            carry = 0
        elif ad[-i] + bd[-i] + carry == 2:
            res.append(0)
            carry = 1
        elif ad[-i] + bd[-i] + carry == 3:
            res.append(1)
            carry = 1
    if carry == 1:
        res.append(1)
    RES = res[::-1]
    answer = "".join(map(str, RES))
    return answer

print(binary_sum(1101, 101))