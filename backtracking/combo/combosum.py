def combinationSum(candidates, target):
    res = []
    n = len(candidates)
    def helper(start, curr, sum_included):
        if sum_included > target:
            return
        if sum_included == target:
            res.append(curr[:])
            return
        for i in range(start, n):
            curr.append(candidates[i])
            helper(i, curr, sum_included+candidates[i])
            curr.pop()
        helper(0,[],0)
        return res
