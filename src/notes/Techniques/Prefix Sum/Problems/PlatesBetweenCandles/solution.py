# Problem: There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s consisting of characters '*' and '|'. Return an array answer where answer[i] is the number of plates between candles in the substring s[lefti...righti].
def platesBetweenCandles(s, queries):
    """
    Approach: Prefix Sum with Nearest Indices.
    Time: O(N + Q)
    Space: O(N)
    """
    n = len(s)
    prefix_stars = [0] * n
    left_candle = [-1] * n
    right_candle = [-1] * n
    stars = 0
    last_candle = -1
    for i in range(n):
        if s[i] == '*': stars += 1
        elif s[i] == '|': last_candle = i
        prefix_stars[i] = stars
        left_candle[i] = last_candle
    last_candle = -1
    for i in range(n - 1, -1, -1):
        if s[i] == '|': last_candle = i
        right_candle[i] = last_candle
    res = []
    for l, r in queries:
        left_bound = right_candle[l]
        right_bound = left_candle[r]
        if left_bound != -1 and right_bound != -1 and left_bound < right_bound:
            res.append(prefix_stars[right_bound] - prefix_stars[left_bound])
        else:
            res.append(0)
    return res
