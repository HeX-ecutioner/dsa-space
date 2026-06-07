import math

class Solution:
    def bulbSwitch(self, n: int) -> int:
        # A bulb remains 'ON' only if it is toggled an odd number of times.
        # A bulb 'i' is toggled for every factor it has.
        # Only perfect squares have an odd number of factors.
        # Thus, the number of bulbs that remain 'ON' is exactly the number of
        # perfect squares less than or equal to 'n'.
        return int(math.sqrt(n))

# --- Example Usage ---
# sol = Solution()
# print(sol.bulbSwitch(3)) # Output: 1
# print(sol.bulbSwitch(0)) # Output: 0
# print(sol.bulbSwitch(9)) # Output: 3 (Bulbs 1, 4, and 9 are ON)
