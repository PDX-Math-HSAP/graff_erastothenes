import scipy, sys

n = int(sys.argv[1])

prime_sieve = scipy.zeros(n)
is_not_prime = prime_sieve
prime_sieve[0] = True
prime_sieve[1] = True

primes = [2]

max_factor = scipy.sqrt(n)
while primes[-1] < max_factor:
    stencil = scipy.array[scipy.prod(primes)]
    


sieve_index = 1
while deref(sieve_index) < max_factor:
    if prime_sieve[sieve_index]:
        current_prime = deref(sieve_index)
        
        # Construct smart skip method
        composites = prime_sieve[0:ref(current_prime ** 2)]
        #
        while :
            prime_sieve[ref(multiple)] = False
            # We skip over even multiples
            multiple += 2 * current_prime
    sieve_index += 1

primes = [2] + list(deref(scipy.nonzero(prime_sieve)[0]))
print(primes[-10:])
