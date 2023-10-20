def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    indices = {} # Create a dictionary to store numbers and their indices
    
    for index, number in enumerate(nums):
        # Calculate the complement (the number needed to reach the target)
        complement = target - number 

        # Check if the complement is in the dictionary
        if complement in indices:
            # If the complement is found, return the indices of the two numbers
            return [indices[complement], index]
        
        # If the complement is not found, add the current number to the dictionary with its index
        indices[number] = index
    
    # If no solution is found, return an empty list
    return []
            