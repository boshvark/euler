# The sum of the squares of the first ten natural numbers is,
#
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 552 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

sum = 0
sum_of_squares = 0
top = 100

for i in xrange(1, top + 1):
    sum_of_squares += i * i
    sum += i

square_of_sum = sum * sum
difference = square_of_sum - sum_of_squares

print "Square of sum minus sum of squares: %d" % difference




