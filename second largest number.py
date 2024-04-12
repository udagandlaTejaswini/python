def second_largest(nums):
    if len(nums) < 2:
        return None

    largest = float('-inf')
    second_largest = float('-inf')

    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        return None
    else:
        return second_largest

# Example usage:
nums = list(map(int,input().split()))
result = second_largest(nums)
if result is not None:
    print("The second largest number in the list is:", result)
else:
    print("There is no second largest number in the list.")