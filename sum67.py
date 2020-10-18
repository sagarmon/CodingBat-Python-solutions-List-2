def sum67(nums):
  sum = 0
  in_range = False
  
  for i in range(len(nums)):
    if nums[i] == 6:
      in_range = True
    if not in_range:
      sum += nums[i]
    if in_range and nums[i] == 7:
      in_range = False
  
  return sum
