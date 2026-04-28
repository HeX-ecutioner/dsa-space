# Problem: You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person. Return the earliest year with the maximum population.
def maximumPopulation(logs):
    """
    Approach: Sweep Line / Difference Array.
    Time: O(N log N)
    Space: O(N)
    """
    events = []
    for birth, death in logs:
        events.append((birth, 1))
        events.append((death, -1))
    events.sort()
    max_pop = 0
    curr_pop = 0
    res_year = 0
    for year, change in events:
        curr_pop += change
        if curr_pop > max_pop:
            max_pop = curr_pop
            res_year = year
    return res_year
