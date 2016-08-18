# Project Euler problem 3.
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?

number = 600851475143
factor = 2
print "Finding prime factors of %d" % number
while number > 1 and factor < number:
    if number % factor == 0:
        number = number / factor
        print "%d is a factor, leaving %d" % (factor, number)
    else:
        factor += 1
print "Largest prime factor: %d" % number
