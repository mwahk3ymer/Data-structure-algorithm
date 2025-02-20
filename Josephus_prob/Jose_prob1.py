def findwin(n, k):
    arr = [i+1 for i in range(n)]

    def helper(arr, start_ind):
        if len(arr)==1:
            return arr[0]
        ind_to_rem = (start_ind + k - 1) % len(arr)
        del arr[ind_to_rem]
        return helper(arr,ind_to_rem)
    
    return helper(arr,0)

if __name__ == "__main__":
    n = 5
    k = 2
    print(f"The winner is: {findwin(n, k)}")
