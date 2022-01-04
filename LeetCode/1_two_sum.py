def twoSum() :
        param_1 = [12,2,3,4,5,6,7,1]
        param_2 = 13
        first = param_2 // 2
        last = param_2-first
        if param_1.index(first) != param_1.index(last) :
            print(f"{param_1.index(first)} : {param_1.index(last)}")      
        else :
            first_c = (param_2 // 2)+1
            last_c = param_2-first
            print(f"{param_1.index(first_c)} : {param_1.index(last_c-1)}")

ret = twoSum()

[8,12,2,3,4,5,6,1]


# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(len(nums)): #            0,1,2,3,4,5,6,7,8
#             for j in range(i + 1, len(nums)): # 1,2,3,4,5,6,7,8,9
#                 if nums[j] == target - nums[i]:
#                     return [i, j]

# ret = Solution().twoSum([1,2,3,4,5,6,7,8,9],12)
# print(ret)
        