import scipy, sys

n = int(sys.argv[1])

prime = 2
is_prime = scipy.ones(n+1,dtype="Bool")
is_prime[0] = False
is_prime[1] = False
largest_factor_to_check = int(scipy.ceil(scipy.sqrt(n)))
for prime in range(2, largest_factor_to_check + 1):
    if is_prime[prime] == 1:
        multiple = 2 * prime
        while multiple <= n:
            is_prime[multiple] = False
            multiple += prime
        prime = scipy.nonzero(is_prime[prime+1:n+1])[0][0]

print(scipy.nonzero(is_prime))
