#This function use the Euclidean Algoritim to return the greatest common denominator of a set of two numbers.
#Assume m is less than n and m and n are positive natural numbers.
def EuclideanGCD(m, n):
    if m == 0:
        return n
    return EuclideanGCD(n % m, m)
def ModifiedEuclideanGCD(nums):
    nums.sort; #cop-out
    nums.append(0);
    if nums[1] == 0:
        return nums[0]
    for index in range(0, nums.length):
        nums[index] = nums[index] - nums[index+1]
    nums[index + 1] = 0
    return ModifiedEuclideanGCD(nums)
print(ModifiedEuclideanGCD([256, 512,1024]))