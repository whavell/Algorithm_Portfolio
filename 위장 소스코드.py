def solution(clothes):
    some_cloth = {}
    cloth = {}
    b = 1

    for i in clothes:
        some_cloth[i[0]] = i[1]

    for l in some_cloth:

        if some_cloth[l] not in cloth:
            cloth[some_cloth[l]] = 1

        else:
            cloth[some_cloth[l]] += 1

    for j in cloth:
        c = cloth[j] + 1
        b = c * b

    answer = b - 1
    return answer
