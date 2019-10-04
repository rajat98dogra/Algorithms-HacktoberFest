def fact(n):
    fac=1
    if n==0:
        return 1
    else:
        return n* fact(n-1)
    
if __name__ == '__main__':
    num = int(input("enter number>>"))
    print(fact(num))
