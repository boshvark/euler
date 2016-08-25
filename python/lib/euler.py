from math import sqrt

def prime_factors(number):
    factors = []
    factor = 2
    while number > 1 and factor < number:
        if number % factor == 0:
            number = number / factor
            factors.append(factor)
        else:
            factor += 1
    factors.append(number)
    return factors

def prime_factor_count(number):
    factor_count = {}
    for factor in prime_factors(number):
        count = factor_count[factor] + 1 if factor in factor_count else 1
        factor_count[factor] = count
        if factor not in factor_count or count > factor_count[factor]:
            factor_count[factor] = count
    return factor_count

def pythagorean_triplet_with_sum(target_sum):
    for a in xrange(1, target_sum + 1):
        for b in xrange(a, target_sum + 1):
            sum = a ** 2 + b ** 2
            c = int(sqrt(sum))
            if sum % c == 0 and a + b + c == target_sum:
                return (a, b, c)
