nums = [1,1,2,2,3,4,2,3]
k = 6
x = 2
def x_sum (nums , k , x):
  n = len(nums)
  result = []
  for i in range ( n-k+1 ):
    num = nums[i:k+i]
    print (num)
    dict = {}
    for val in num:
      dict[val] = dict.get(val , 0) + 1
    sorted_items = sorted(dict.items(), key=lambda item: (-item[1], -item[0]))
    print(sorted_items) 
    sum = 0
    for a in range (min (x , len (sorted_items))):
      key , value = sorted_items[a]
      sum += key * value
    result.append (sum)
  return result 

r = x_sum(nums , k , x)
print (r)
