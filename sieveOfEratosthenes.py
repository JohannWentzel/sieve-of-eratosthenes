max = 100

sieve = [True] * (max + 1)
sieve[0] = False
sieve[1] = False

nextPrime = 2

while nextPrime <= max:
	for i in range(nextPrime + 1,len(sieve)):
		if i % nextPrime == 0:
			sieve[i] = False

	nextPrime += 1

	while nextPrime < len(sieve) and not sieve[nextPrime]:
		nextPrime += 1

primes = []

for i in range(len(sieve)):
	if sieve[i]:
		primes.append(i)

print(primes)