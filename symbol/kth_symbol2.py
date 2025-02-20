def kth_symbol(n, k):
    if n==1: return 0
    length = 2**(n-1)
    mid = length //2
    if k<=mid:
        return kth_symbol(n-1, k)
    else:
        return 1 - kth_symbol(n-1, k - mid)

if __name__ == "__main__":
            n = 4  # Example row
            k = 3  # Example index
            print(f"The {k}-th symbol in row {n} is: {kth_symbol(n, k)}")
