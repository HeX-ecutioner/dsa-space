# Bulb Switcher

**Difficulty:** Medium

There are `n` bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.
On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the `i`th round, you toggle every `i`th bulb. For the `n`th round, you only toggle the last bulb.
Return the number of bulbs that are on after `n` rounds.

## Example 1:
**Input:** `n = 3`
**Output:** `1`
**Explanation:** 
At first, the three bulbs are `[off, off, off]`.
After first round, the three bulbs are `[on, on, on]`.
After second round, the three bulbs are `[on, off, on]`.
After third round, the three bulbs are `[on, off, off]`. 
So you should return 1, because there is only one bulb is on.

## Approach: Math / Logical Deduction
This isn't a two-player game, but it's a classic Game Theory / Mathematical simulation problem. 
If we trace the toggles, a bulb `i` is toggled in round `k` if `k` is a factor of `i`.
For example, bulb 12 is toggled in rounds 1, 2, 3, 4, 6, and 12.

- If a bulb has an **even** number of factors, it is toggled an even number of times (Off -> On -> Off). It ends up **Off**.
- If a bulb has an **odd** number of factors, it is toggled an odd number of times (Off -> On -> Off -> On). It ends up **On**.

Which numbers have an odd number of factors? Only **Perfect Squares**.
For non-perfect squares, factors always come in pairs (e.g., for 12: 1x12, 2x6, 3x4).
For perfect squares, the square root factor pairs with itself, yielding an odd total (e.g., for 16: 1x16, 2x8, 4x4 -> factors are 1, 2, 4, 8, 16. That's 5 factors).

Therefore, the problem is just asking: "How many perfect squares are there less than or equal to `n`?"
The answer is exactly `floor(sqrt(n))`.

## Complexity
- **Time Complexity:** $O(1)$ (Assuming math.sqrt is constant time).
- **Space Complexity:** $O(1)$
