class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, x in enumerate (nums): ##enumerate gives x and i at same time   
            complement = target - x
            if complement in seen:
                return [seen[complement], i]
            seen[x] = i

    ## first loop in (i = 0, x = 2)