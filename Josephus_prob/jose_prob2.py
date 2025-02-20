def findwin(n, k):

    def jose(n):
        if n==1:
            return 0
        return (jose(n-1) +k)%n

    return jose(n) + 1

if __name__ == "__main__":
    n = 5
    k = 2
    print(f"The winner is: {findwin(n, k)}")
