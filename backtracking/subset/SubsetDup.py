def subsetsWithDup(nums):

    res = []
    nums.sort()
    def helper(index, curr):
        if index == len(nums):
            res.append(curr[:])
            return
        #include choice
        curr.append(nums[index])
        helper(index+1, curr)
        curr.pop() #backtracking
        #exclude
        while index<len(nums)-1 and nums[index]==nums[index+1]:
            index+=1
        helper(index+1, curr)

    helper(0,[])
    return res

print(subsetsWithDup([1, 2, 2]))
print(subsetsWithDup([4, 4, 4, 1, 4]))
