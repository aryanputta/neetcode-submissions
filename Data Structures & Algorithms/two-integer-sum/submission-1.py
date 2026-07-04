class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, x in enumerate (nums): ##enumerate gives x and i at same time   
            complement = target - x
            if complement in seen:
                return [seen[complement], i] ## ONLY RAN WHEN COMPLEMNT IS IN SEEN
            seen[x] = i

    ## [2, 7 , 11, 15]

    #1st LOOP
    ## seen {} --> starts empty 
    ## for i, x in enmumerate (nums): --> target 9:   i = 0, x = 2
    ## complement _7_ = 9 - 2 
    ## if complement in seen: (checks if 7 is in HASHMAP)
    ## seen[x] = i, 7 is not in HASHMAP, store value for later, 2->0, gets stored 

    ##2nd LOOP
    ## for i, x in enumerate (nums): --> target 9: i = 1, x - 7
    ## complement _2_ = 9 - 7
    ## seen[2] = 0 old index
    ## return [seen[complement], i] returns [0][1]: