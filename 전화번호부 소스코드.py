def solution(phone_book): (1)
 flag = True
 phone_nums = {}

for i in phone_book: (2)
    phone_nums[i] = True

for l in phone_nums: (3)
    for j in range(len(l)):
        b = l[:j]
        if phone_nums.get(b):
            flag = False
            break

return flag
