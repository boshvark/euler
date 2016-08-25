# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
#
# What is the 10 001st prime number?

prime_count = 0
top_prime_index = 10001
number = 1
primes = []

while prime_count < top_prime_index:
    number += 1
    is_prime = True
    for prime in primes:
        if number % prime == 0:
            is_prime = False
            break
    if is_prime:
        prime_count += 1
        primes.append(number)

print "Prime #%d: %d" % (top_prime_index, primes[-1])




