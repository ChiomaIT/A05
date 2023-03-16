def main():
  def addArray(numList, ind, val):
    if ind >= 0:
      val += numList[ind]
      return addArray(numList[:ind], ind-1,val)
    return val
  
  numList = [1,2,3]
  # print(addArray(numList, len(numList) - 1, 0))
  
  def removeNegative(nums, i, res):
    if i >= 0:
      if nums[i] > 0:
        res.append(nums[i])
        removeNegative(nums[:i], i - 1, res)
      else:
        removeNegative(nums[:i], i - 1, res)
    return res
  
  nums = (1,2,-3,-5,6,2,3,44,5,6,-10,-1)
  # print(removeNegative(nums, len(nums)-1, []))

  
if __name__ == '__main__':
    main()
