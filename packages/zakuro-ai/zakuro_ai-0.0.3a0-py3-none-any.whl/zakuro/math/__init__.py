def recur_fibo(n):
    print(n)
    if n <= 1:
       return n
    else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
