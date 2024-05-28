# binary_search.py

def binary_search(list, item):
  low = 0
  high = len(list) - 1
  stepCount = 1
  
  while low <= high:
    mid = (low + high) // 2 ## // operator rounds the result of this expression
    guess = list[mid]
    if guess == item:
      return mid
    elif guess > item:
      high = mid - 1 # Estimation number is too big
    else:
      low = mid + 1 # Too small
    stepCount += 1
    print("step count is {0}".format(stepCount))
  return -1
      

lis = [1,2,3,4,5,6,7,8,9,10,11]
res = binary_search(lis, 1)
print(res)