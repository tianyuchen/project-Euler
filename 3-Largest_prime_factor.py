# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


def largest_prime_factor(num):
    i = 2
    primfac = []
    while i * i < num:
        while num % i == 0:
            primfac.append(i)
            num //= i  # num = num/i
        i += 1
    if num > 1:
        # add the last prime factor
        primfac.append(num)
        # or print num, it is the largest prime factor
    primfac.sort(reverse=True)
    # print the largest prime factor of the number
    print primfac[0]


largest_prime_factor(600851475143)
