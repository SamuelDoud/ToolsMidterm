#This function use the Euclidean Algoritim to return the greatest common denominator of a set of two numbers.
#Assume m is less than n and m and n are positive natural numbers.
def EuclideanGCD(m, n):
    if m == 0:
        return n
    return EuclideanGCD(n % m, m)
def ModifiedEuclideanGCD(nums):
    nums.sort(); #cop-out
    nums.reverse();
    if nums[1] == 0:#this means that the only non-zero element in the list is the first element, the GCD
        return nums[0]#return the top element
    for index in range(0, len(nums) - 1):#iterate through all but the last element
        if (nums[index + 1] == 0):
            return ModifiedEuclideanGCD(nums)#this indicates that zeros are present for the rest of the list... recur
        nums[index] = nums[index] - nums[index+1]#subtract next from current and save it to current
    nums.append(0) #we only get here if there wasn't a zero in the array(only possible on the first run. We need one now!
    return ModifiedEuclideanGCD(nums)#recur statement for the first iteration
def EuclideanLCM(m, n):
    return (m*n)/EuclideanGCD(m, n)
def ListEuclideanLCM(nums):
    nums.sort()
    nums.reverse()#greatest to least now
    for index in range(0, len(nums) - 1):
        nums[index+1] = EuclideanLCM(nums[index+1], nums[index])
    return nums[len(nums) - 1]
print(".")
print(ModifiedEuclideanGCD([256, 512,1024, 5481]))
print(ListEuclideanLCM([3,5,8,16]))
