class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map = {}

        # adding the elements in the hashmap:
        for index, num in enumerate(nums1):
            if num not in hash_map:
                hash_map[num] =1
            else:
                continue
        
        # check if the element is in hashmap already:
        result = []
        for num in nums2:
            if num in hash_map.keys() and num not in result:
                result.append(num)
        return result
        