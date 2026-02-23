def twoSum( nums, target):
    sum=[]
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            x=nums[i]+nums[j]
            if x==target:
                sum.append(i)
                sum.append(j)
                return sum
        