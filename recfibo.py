def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms=int(input("upto which term?"))

# check if the number is negative
if nterms < 0:
   print("Sorry, Number of terms does not exist for negative numbers")
else:
   print("The Fibonacci series is")
   for i in range(nterms):
       print(recur_fibo(i))
