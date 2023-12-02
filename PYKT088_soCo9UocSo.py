from math import *
def dem(n):
    cnt = 0
    prime = [i for i in range(isqrt(n) + 1)]
    tmp = isqrt(n)
    i = 2
    while i * i <= isqrt(n):
        if prime[i] == i:
            for j in range(i * i, isqrt(n) + 1, i):
                if prime[j] == j:
                    prime[j] = i
        i += 1

    for i in range(2, isqrt(n) + 1):
        a = prime[i]
        b = prime[i // prime[i]]
        if a * b == i and b != 1 and a != b:
            cnt += 1
        elif prime[i] == i:
            if i ** 8 <= n: cnt += 1
    return cnt

n = int(input())
print(dem(n))
"""
1.Use Sieve technique to mark the smallest prime factor of a number.
2.We just need to check for all the numbers in the range[1->sqrt(n)] that can be expressed in terms of p*q since (p^2*q^2) has 9 factors, 
hence (p*q)^2 will also have exactly 9 factors.
3.Iterate from 1 to sqrt(n) and check if i can be expressed as p*q, where p and q are prime numbers.
4.Also, check if i is prime then pow(i, 8)<=n or not, in that case, count that number also.
5.The summation of the count of numbers that can be expressed in the form p*q and p^8 is our answer.
"""
