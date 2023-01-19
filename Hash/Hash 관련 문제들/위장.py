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

        # if some_cloth[l] not in cloth.keys():
        #     cloth[some_cloth[l]] = [l]
        #
        # else:
        #     cloth[some_cloth[l]].append(l)

    print(cloth)

    for j in cloth:
        c = cloth[j] + 1
        b = c * b

    answer = b - 1
    return answer
