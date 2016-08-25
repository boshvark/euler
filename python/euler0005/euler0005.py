# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

from euler import prime_factor_count

top = 20
total_factor_count = {}

# Build up a set of factors that includes the full set of prime factors for
# every number between 1 and 20.
for number in xrange(1, top + 1):
    factor_count = prime_factor_count(number)
    for factor in factor_count:
        count = factor_count[factor]
        if factor not in total_factor_count or count > total_factor_count[factor]:
            total_factor_count[factor] = count

product = 1
for factor in total_factor_count:
    count = total_factor_count[factor]
    for i in xrange(0, count):
        product *= factor

print "Smallest positive number divisible by 1 to %d: %d" % (top, product)
