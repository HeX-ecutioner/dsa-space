# Problem: Given an array of non-negative integers and a value sum, determine if there is a subset of the given set with sum equal to given sum.
def isSubsetSum(arr, target):
    """
    Approach: Branch and Bound / Backtracking.
    Prune paths that exceed the target.
    Time: O(2^N)
    Space: O(N)
    """
    arr.sort()
    def dfs(index, current_sum):
        if current_sum == target: return True
        if current_sum > target or index == len(arr): return False
        
        if dfs(index + 1, current_sum + arr[index]):
            return True
        if dfs(index + 1, current_sum):
            return True
        return False
    return dfs(0, 0)
