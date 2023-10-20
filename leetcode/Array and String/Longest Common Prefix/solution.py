def longest_common_prefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    
    if not strs:
        return ""  # If the input list is empty, return an empty string

    min_length = min(len(s) for s in strs)  # Find the minimum length among the strings

    common_prefix = ""
    for i in range(min_length):
        current_char = strs[0][i]  # Get the character at the current position in the first string
        for s in strs[1:]:
            if s[i] != current_char:
                return common_prefix  # If the characters don't match, return the common prefix found so far
        common_prefix += current_char

    return common_prefix

            