#Largest prime factor
#The prime factors of 13195 are 5, 7, 13 and 29. (13195=5x7x13x29)
#What is the largest prime factor of the number 600851475143 ?

#Results:
#The largest prime factor of the number 600851475143 is 6857
#Total time elapsed: 0.0935151576996 seconds

#

#Python code:

#!/usr/local/bin/python2.7
#
# Program to find the largest prime factor of a number
#

from math import sqrt
import time


def prime_factors( n):
# find primes factors, return longest

  #reduce the even numbers
  while (n % 2 == 0):
    ret = 2
    n = n/2
 
  #Every composite number has at least one prime factor
  #less than or equal to square root of itself.
  max=sqrt(n)
 
  i = 3
  while (i <=max):
    while (n % i == 0):
      ret = i
      n = n/i;
    i = i + 2 # skipping the even numbers

  # primes numbers
  if (n > 2):
      ret = n      

  return ret
if __name__ == '__main__':
 
  #initialization
  number=600851475143
  start_time = time.time()

  #find the solution
  longest_divisor = prime_factors(number)
 
 
  print "\n\nThe largest prime factor of the number " + str(number) + " is " + str(longest_divisor)
  print "\n\nTotal time elapsed: " + str(time.time() - start_time) + " seconds"
 
 
