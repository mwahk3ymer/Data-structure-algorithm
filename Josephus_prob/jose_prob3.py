def findwin(n, k):

    survivor = 0

    for i in range(2,n+1):
        survivor = (survivor + k)% i
    
    return survivor +1

if __name__ == "__main__":
    n = 5
    k = 2
    print(f"The winner is: {findwin(n, k)}")
