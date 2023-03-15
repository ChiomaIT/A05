def addArray(numList, ind, val):
  if ind >= 0:
    val += numList[ind]
    return addArray(numList[:ind], ind-1,val)
  return val

numList = [1,2,3]
print(addArray(numList, len(numList) - 1, 0))