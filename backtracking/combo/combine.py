def combine(n,k):
    res = []
    def helper(start, curr):
        #basecase
        if len(curr) == k:
            res.append(curr[:])
            return
        for j in range(star, n+1):
            curr.append(j)
