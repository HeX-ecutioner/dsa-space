from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies using a Hash Map
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # 2. Bucket Sort setup
        # Create an array of empty lists. The index represents the frequency.
        # Max possible frequency is len(nums), so we need size len(nums) + 1
        freq = [[] for i in range(len(nums) + 1)]
        
        # 3. Populate buckets
        for num, c in count.items():
            freq[c].append(num)
            
        # 4. Gather results from highest frequency to lowest
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                    
        return res

# --- Example Usage ---
# sol = Solution()
# print(sol.topKFrequent([1,1,1,2,2,3], 2)) # Output: [1, 2]
# print(sol.topKFrequent([1], 1))         # Output: [1]
