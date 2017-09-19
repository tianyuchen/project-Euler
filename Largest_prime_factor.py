def largest_prime_factor(num):
    i = 2
    primfac = []
    # important step ***
    while i * i < num:
        while num % i == 0:
            primfac.append(i)
            num //= i  # num = num/i
        i += 1
    if num > 1:
        # add the last prime factor
        primfac.append(num)
    primfac.sort(reverse=True)
    # print the largest prime factor of the number
    print primfac[0]


largest_prime_factor(600851475143)
