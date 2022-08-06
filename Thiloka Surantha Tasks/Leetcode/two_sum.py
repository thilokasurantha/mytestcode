def twosum(nums, target) :
    for i in range(0, len(nums)) :
        for j in range(1, len(nums)) :
            if nums[i] + nums[j] == 9 :
                return "["+str(i)+","+str(j)+"]"

result = twosum([2,7,11,15], 9)
print(result)