def plusMinus(arr):
    # Write your code here
    denominator = len(arr)
    
    positives, negatives, zeros = 0, 0, 0

    for num in arr:
        if num > 0:
            positives += 1
        elif num < 0:
            negatives += 1
        else:
            zeros += 1
    
    print(f"{positives/denominator:.6f}")
    print(f"{negatives/denominator:.6f}")
    print(f"{zeros/denominator:.6f}")
