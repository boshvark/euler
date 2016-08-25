# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
#
# What is the 10 001st prime number?

from euler import first_n_primes

prime_count = 10001
primes = first_n_primes(prime_count)
print "Prime #%d: %d" % (prime_count, primes[-1])




