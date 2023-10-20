def length_of_longest_substring(s):
    """
    :type s: str
    :rtype: int
    """
    # Initialize a dictionary to store the most recent index of each character
    char_index = {}
    
    # Initialize variables for tracking the maximum length and the start of the current substring
    max_length = 0
    start = 0

    for current_index in range(len(s)):
        if s[current_index] in char_index and char_index[s[current_index]] >= start:
            # If the character is in the current substring and its index is greater than or equal to the start,
            # update the start position to the next character after the repeated character.
            start = char_index[s[current_index]] + 1

        # Update the index of the character in the dictionary
        char_index[s[current_index]] = current_index

        # Calculate the current substring length and update the maximum length if necessary
        current_length = current_index - start + 1
        max_length = max(max_length, current_length)

    # Return the maximum length of a substring without repeating characters
    print(char_index)
    return max_length


s1 = "workattech"
s2 = "mississippi"

result1 = length_of_longest_substring(s1)
result2 = length_of_longest_substring(s2)

print(result1)  # Output: 6 (Longest valid substring is "workat")
print(result2)  # Output: 3 (Longest valid substrings are "mis" and "sip")

