def combine(n,k):
    res = []
    def helper(start, curr):
        #basecase
        if len(curr) == k:
            res.append(curr[:])
            return
        need = k - len(curr)

        for j in range(start, n+1):
            curr.append(j)
            helper(j+1,curr)
            curr.pop()

    helper(1,[])
    return res
print(combine(4,2))
