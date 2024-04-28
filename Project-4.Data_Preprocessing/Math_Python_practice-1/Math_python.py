""" pythagorean. triple.generation code """

def gen_triples(N):
    for m in range(1, int(N**5)+1):
        for n in range(1,m):
            if (m-n) % 2 and gcd(m, n) == 1:
                c = m**2 + n**2
                if c <= N:
                    a = m**2 -n**2
                    b = 2*m*n
                    yield (a, b,c)
    triples = sorted(
        gen_triples(50), key = lambda * triple: sum(*triple))
    print(triples)


   


""" print the primes between given interval"""



# python program to print all the prime numbers between given numbers
lower = 5
upper = 20

for prime in range(lower , upper+1):
    if prime >1:   # prime numbers are greater than 1
        for n in range(2, prime):
            if (prime % n) == 0:
                break
            else:
                print(prime)
              
""" output : 5, 7, 11, 13, 17, 19"""


# another process
# find the prime number between given number

prime = []
upto = 100
for n in range(2, upto+1):
    for divisor in range (2,n):
        if n % divisor ==0:
            break
        else:
            prime.append(n)
    print(prime)
# this also print prime numbers between given number.


# formula for geometric progression is a, aq, aq^2,..... where a is the first term and q is the common ratio

def geometric_progression(a,q):
    k = 0
    while True:
        result = a * q**k
        if result <= 1000000:
            yield result
        else:
            return
        k += 1
for n in geometric_progression(2, 5):
    print(n)
    
    
"""
out put : 
2
10
50
250
1250
6250
31250
156250
781250
.......
"""

# printing square between 2 to 5

def print_square(start, end):
    for n in range(start, end):
        yield  n**2
for n in print_square(2,5):
    print(n)











