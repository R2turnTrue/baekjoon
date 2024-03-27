N = int(input())

nums = [int(input()) for i in range(N)]

nums.sort()

print(round(sum(nums) / float(N)))
print(nums[(len(nums) - 1) // 2])

dic = dict()

for i in nums:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
        
mx = max(dic.values())
mx_dic = []

for i in dic:
    if mx == dic[i]:
        mx_dic.append(i)

if len(mx_dic) > 1:
    print(mx_dic[1]) # 2번째로 작은 값
else:
    print(mx_dic[0])

print(nums[-1] - nums[0])