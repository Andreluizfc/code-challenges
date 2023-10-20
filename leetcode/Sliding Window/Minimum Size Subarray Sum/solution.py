def min_sub_array_len(target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    # Initialize minimum length with a large value (positive infinity)
    min_len = float('inf')
    
    current_sum = 0  # Initialize the current sum of the subarray
    left = 0  # Left pointer to mark the start of the subarray
    
    # Iterate through the array using the right pointer
    for right in range(len(nums)):
        current_sum += nums[right]  # Add the current element to the subarray sum

        # Check if the current subarray sum is greater than or equal to the target
        while current_sum >= target:
            # Update min_len with the minimum length found so far
            min_len = min(min_len, right - left + 1)
            
            # Move the left pointer to the right to find a shorter subarray
            current_sum -= nums[left]
            left += 1

    # If min_len remains as positive infinity, there's no valid subarray
    return min_len if min_len != float('inf') else 0


target = 7
nums = [2,3,1,2,4,3]

result1 = min_sub_array_len(target, nums)

target = 4
nums = [1,4,4]

result2 = min_sub_array_len(target, nums)

print(result1)
print(result2)

