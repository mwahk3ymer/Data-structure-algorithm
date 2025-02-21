def toh(N, fromm, to, aux):

    count = 0
    def helper(N,fromm,to,aux):
        nonlocal count

        if N==1:
            print("move disk" + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
            count+=1
            return

        helper(N-1,fromm,aux,to)
        print("move disk" + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
        count +=1
        helper(N-1,aux,to,fromm)
    
    helper(N,fromm,to,aux)
    return count

if __name__ == "__main__":
    N = 3  # Example: Moving 3 disks
    moves = toh(N, 1, 3, 2)
    print(f"Total moves: {moves}")
