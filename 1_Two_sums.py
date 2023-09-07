# Problem : Two sums

def twoSum(nums, target):
    # using the hashing concept:
    result = []
    hash_map = {}
    
    for index, n in enumerate(nums):
        if target - n in hash_map.keys():
                result.extend([hash_map[target-n], index]) 
                
        if n not in hash_map:
            hash_map[n] = index
            
    return result

if __name__ == "__main__":
    result = twoSum([3, 3], 6)
    print(result)