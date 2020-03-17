import math

# if a number P is not prime, then we can write it as $P = a *b$.
# if both a nd b are greater than sqrt(P), then a*b would be greater
# than $P$. So at least one of those factors must be less than or equal to sqrt(P).
# If we cannot find any factors less than or equal to sqrt(P), P must be prime.

def isPrime(n):
    sq = math.sqrt(n)

    for i in range(2,math.ceil(sq)):
        if (n % i == 0):
            return False

    return True

