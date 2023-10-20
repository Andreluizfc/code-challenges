def miniMaxSum(arr):
    # Write your code here
    arr.sort()

    min_sum = sum(arr[0:4])
    max_sum = sum(arr[1:5])

    print(min_sum, max_sum)


arr = [1, 3, 5, 7, 9]

miniMaxSum(arr)