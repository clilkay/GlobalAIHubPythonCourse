
def PrimeNumber(num):
   for num in range(num + 1):
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

num=int(input(("To find a prime number in the interval  please write your upper bond value : ")))
PrimeNumber(num)