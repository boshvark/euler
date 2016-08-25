# Project Euler problem 4.
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two
# 2-digit numbers is 9009 = 91 * 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(number):
    string = str(number)
    return string == string[::-1]

highest_palindrome = 0

for i in xrange(999, 100, -1):
    for j in xrange(999, 100, -1):
        product = i * j
        if is_palindrome(product):
            if product > highest_palindrome:
                highest_palindrome = product
                #print "new high: (i = %d) * (j = %d) = %d" % (i, j, product)

print "Highest palindrome: %d" % highest_palindrome
