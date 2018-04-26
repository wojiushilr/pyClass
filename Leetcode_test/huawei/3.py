def minSubArray(nums):

    max = min = sum(nums)
    maxList = minList = nums
    n = len(nums)+1
    for i in range(n+1):
        for j in range(i+1,n+1):
            sonList = nums[i:j]
            Sum = sum(sonList)
            if Sum >= max:
                max = Sum
                maxList = sonList
            elif Sum < min:
                min = Sum
                minList = sonList
    print (sum(maxList))

num =input().strip().split(", ")
arr = []
for i in range(len(num)):
    arr.append(int(num[i]))
#print(num)
#print(arr)
minSubArray(arr)