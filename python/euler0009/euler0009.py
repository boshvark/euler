# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#
# Find the product abc.

from euler import pythagorean_triplet_with_sum

target_sum = 1000

(a, b, c) = pythagorean_triplet_with_sum(target_sum)

print "Pythagorean triplet with sum %d: a = %d, b = %d, c = %d" % \
        (target_sum, a, b, c)
print "Product: %d" % (a * b * c)
