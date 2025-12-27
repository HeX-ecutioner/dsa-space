# Remove Adjacent Duplicates Using Two Pointers
# Problem: Remove adjacent duplicates in a string (like "abbaca" -> "ca")
def remove_adjacent_duplicates(s: str) -> str:
    """
    Use list as stack but simulate two-pointer in-place:
    - write pointer keeps next write position
    - iterate read over characters, if write>0 and top==current -> pop (write-=1)
      else write current char
    Time: O(n), Space: O(n) for result
    """
    chars = list(s)
    write = 0
    for read in range(len(chars)):
        if write > 0 and chars[write-1] == chars[read]:
            write -= 1  # remove last
        else:
            chars[write] = chars[read]
            write += 1
    return ''.join(chars[:write])

# Example:
# remove_adjacent_duplicates("abbaca") -> "ca"
