import scipy, sys

def deref(index):
    return 2 * index + 1

def ref(number):
    assert(number % 2 == 1)
    return (number - 1) // 2

n = int(sys.argv[1])

# prime_sieve = scipy.ones((n+1)//2,dtype="Bool")

Holds composites


max_factor = scipy.sqrt(n)
sieve_index = 1
while deref(sieve_index) < max_factor:
    if prime_sieve[sieve_index]:
        current_prime = deref(sieve_index)
        multiple = current_prime ** 2
        while multiple <= n:
            prime_sieve[ref(multiple)] = False
            # We skip over even multiples
            multiple += 2 * current_prime
    sieve_index += 1

primes = [2] + list(deref(scipy.nonzero(prime_sieve)[0]))
print(primes[-10:])
