class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        # Count frequencies
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        # Sort the numbers based on their frequency
        sorted_freq = sorted(
            freq,  ##take nums inside hashmap and sort them 
            key=freq.get,  ## look up freq in hashmap and compare those
            reverse=True) ## want to flip order 
        # Return the first k numbers
        return sorted_freq[:k]