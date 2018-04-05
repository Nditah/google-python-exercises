# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
  result = []
  z = len(nums)
  i=0
  while i < z :
    
    if i+1 < len(nums):
      if  nums[i] != nums[i+1]:
        result.append(nums[i])
      else:
        counting = 1
        while nums[i] == nums[i+1]:
          counting += 1
          i +=1
        if nums[i] == nums[i+1]:
          continue
        result.append(counting * nums[i])
        
    i= i + 1 

  return result

print(remove_adjacent( [1, 2, 2, 3, 4, 5,5,5,7,8,8,8,9]))