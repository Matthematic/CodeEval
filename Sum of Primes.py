#http://en.wikipedia.org/wiki/Primality_test





#function to test if a number is prime
def isPrime(num):
    if num <= 1:    #if num is 1, return false (not prime)
        return False
    elif num == 2:  #if num is 2, return true (first prime number)
        return True
    elif num % 2 == 0: #if num is even, return false (all primes other than 2 are odd)
        return False

    count = 3           #since we have 1 and 2 covered, we start at the number 3

    while count*count <= num:   #until count is the sqrt of num (becomes redundant after this)
        if num % count == 0:    #if count divides num, our number
            return False        #   has a divisor other than 1 and itself, so return false
        else:
            count += 2          #else, try the next odd number

    return True                 #if we get to sqrt of num and there were no divisors,
                                #   then num is clearly prime

count = 0
Sum = 2
num = 3

while count < 999:
    if isPrime(num):
        Sum += num
        count += 1

    num += 2







print (Sum)
