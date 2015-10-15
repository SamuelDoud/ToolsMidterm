def EuclideanGCD(m, n):
    if m == 0:
        return n
    return EuclideanGCD(n % m, m)
def MinusifiedEuclideanGCD(nums, numberOfRuns):
    nums.sort(reverse = True) #sort the list
    print(nums)#show the remaining and sorted list of nums
    if nums[1] == 0:#this means that the only non-zero element in the list is the first element, the GCD
        print ("Number of recursions: %d" % (numberOfRuns + 1))#print how many recursions this algorithim took
        return nums[0]#return the top element
    for index in range(0, len(nums) - 1):#iterate through all but the last element
        if (nums[index + 1] == 0):#Is the next element zero? If it is it will have no effect on subtraction
            return MinusifiedEuclideanGCD(nums, numberOfRuns + 1)#this indicates that zeros are present for the rest of the list... recur
        nums[index] = nums[index] - nums[index+1]#subtract next from current and save it to current
    nums.append(0) #we only get here if there wasn't a zero in the array(only possible on the first run. We need one now!)
    return MinusifiedEuclideanGCD(nums, numberOfRuns + 1)#recur statement for the first iteration
def removeAll(list, num):
    return [value for value in list if value != num]
def MODifiedEuclidean(nums, numberOfRuns):
    nums = removeAll(nums, 0) #remove any zeros
    nums.sort(reverse = True)#sort the list in descending order
    print(nums)#show the sorted and remaining list off nums
    #these two lines remove any zeros put the numbers in descending order
    if len(nums) == 1:#there is only one element in the list, the rest have been made into zeros and removed
        print ("Number of recursions: %d" % (numberOfRuns + 1))#print how many recursions this algorithim took
        return nums[0] #this is the only non zero element in the list, return it
    for index in range(0, len(nums) - 1):
        nums[index] = nums[index] % nums[index + 1] #take the mod of the index element and index + 1 element and store it in the index-th element
    return MODifiedEuclidean(nums, numberOfRuns + 1)#recur with the mod-ed list
def EuclideanLCM(m, n):
    return (m*n)/EuclideanGCD(m, n)
def ListEuclideanLCM(nums):
    nums.sort()
    nums.reverse()#greatest to least now
    for index in range(0, len(nums) - 1):
        nums[index+1] = EuclideanLCM(nums[index+1], nums[index])
    return nums[len(nums) - 1]
print("Finally going!")
#testCase = [2840,3330,4206,42390, 4392]
testCase = [155,150,145]
print("Using modulo")
print(MODifiedEuclidean(testCase, 0))
print("using minus")
print(MinusifiedEuclideanGCD(testCase, 0))
#This function use the Euclidean Algoritim to return the greatest common denominator of a set of two numbers.
#Assume m is less than n and m and n are positive natural numbers.