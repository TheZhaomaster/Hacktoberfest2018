import math 
num = int(input("Give a positive number: "))
if num > 1:
   
   for i in range(2, num):
       if (num % i) == 0:
           print num,"is not a prime number"
           break
   else:
       print num,"is a prime number"
    
else:
   print "entered number should be gretater than 1"
