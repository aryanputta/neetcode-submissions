class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_counts = {}
        for num in nums: 
            if num in seen_counts: 
                return True 
            seen_counts[num] = 1
        return False