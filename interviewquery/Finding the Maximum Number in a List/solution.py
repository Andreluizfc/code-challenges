def find_max(nums):
    if nums:
        max = nums[0]
        for num in nums:
            if num > max:
                max = num
        return max
    else:
        return None