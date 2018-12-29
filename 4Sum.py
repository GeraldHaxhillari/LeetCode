class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums) - 3):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3]>target or nums[-1] + nums[-2] + nums[-3] + nums[-4] < target:
                break
            for j in range(i+1,len(nums) - 2):
                if j != i+1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + nums[j] +nums[j+1] +nums[j+2]>target or nums[i] + nums[-1] + nums[-2] + nums[-3] < target:
                    break
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    if nums[i] + nums[j] +nums[k] +nums[k+1]>target or nums[i] + nums[j] + nums[l-1] + nums[l] < target:
                        break
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        result.append([nums[i], nums[j], nums[k], nums[l]])
                        while k < l and nums[k] == nums[k+1]:
                            k+=1
                        while k < l and nums[l] == nums[l-1]:
                            l-=1
                        k += 1
                        l -= 1
                    elif nums[i] + nums[j] + nums[k] + nums[l] > target:
                        l-=1
                    else:
                        k+=1
        return result
