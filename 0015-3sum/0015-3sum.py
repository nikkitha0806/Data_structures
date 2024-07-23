class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array and then use two pointer 2 concept:
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            if a == nums[i-1] and i >0:
                continue

            l, r = i+1, len(nums)-1
            while l<r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0: 
                    r-=1
                elif threesum <0:
                    l+=1
                else:
                    result.append([a, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return result