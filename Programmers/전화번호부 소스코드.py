def solution(phone_book):
 flag = True
 phone_nums = {}

for i in phone_book:
    phone_nums[i] = True

for l in phone_nums:
    for j in range(len(l)):
        b = l[:j]
        if phone_nums.get(b):
            flag = False
            break

return flag
