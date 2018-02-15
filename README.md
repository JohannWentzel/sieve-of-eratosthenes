# Sieve of Eratosthenes
Python implementation of the Sieve of Eratosthenes, allowing you to efficiently generate primes. With this, you can easily check if a number is prime without additional iteration!

From *Cracking the Coding Interview* (originally in Java, translated into Python).

The algorithm essentially follows these steps:

1. Start with a list of all numbers (up to a maximum you specify). Here we're using a array of Booleans, all set to true.
2. Cross off (set to False) all numbers divisible by 2.
3. Find the next prime (conveniently, the next non-crossed-off number).
4. Cross off all numbers divisible by that next prime.
5. Repeat until you reach the maximum.
