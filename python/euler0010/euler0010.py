# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

top = 2000000
composites = {}
sum_of_primes = 0

for number in xrange(2, top):
    if number not in composites:
        sum_of_primes += number
    multiple = number
    while multiple < top:
        composites[multiple] = 1
        multiple += number

print "Sum of primes: %d" % sum_of_primes

