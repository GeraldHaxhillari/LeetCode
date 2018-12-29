class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        N, result = len(nums), []
        if N < 3: return result

        for i in range(N-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = N - 1
            target = -nums[i]
            while left < right:
                twoSum = nums[left] + nums[right]
                if twoSum > target:
                    right -= 1
                elif twoSum < target:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1  
                    while left < N and nums[left-1] == nums[left]:
                        left += 1 
                    while right > 0 and nums[right+1] == nums[right]:
                        right -= 1  
        return result
