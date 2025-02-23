def power_set (nums):
    res = []
    def helper(nums, i, subset):
        if i == len(nums):
            res.append(subset.copy())
            return
        helper(nums, i+1, subset)
        subset.append(nums[i])
        helper(nums, i+1, subset)
        subset.pop()
    helper(nums, 0, [])
    return res
test1 = [1, 8, 7]
test2 = [4, 5]
test3 = []

print("Power set of [1, 8, 7]:", power_set(test1))
print("Power set of [4, 5]:", power_set(test2))
print("Power set of []:", power_set(test3))
