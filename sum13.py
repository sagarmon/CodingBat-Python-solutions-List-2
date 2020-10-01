def sum13(nums):
    sum = 0
    if len(nums) == 0:
        return 0

    for i in range(len(nums)):
        if nums[i] != 13:
            sum += nums[i]
        else:
            if i == len(nums) - 1:
                sum += 0
            else:
                sum -= nums[i + 1]
    if sum < 0:
        return 0
    return sum
