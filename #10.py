MAX_N = 10**6

# Step 1: Sieve of Eratosthenes to find all primes up to MAX_N
is_prime = [True] * (MAX_N + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX_N**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_N + 1, i):
            is_prime[j] = False

# Step 2: Create cumulative sum array
prime_sum = [0] * (MAX_N + 1)
for i in range(1, MAX_N + 1):
    prime_sum[i] = prime_sum[i - 1]
    if is_prime[i]:
        prime_sum[i] += i

# Step 3: Process each test case
T = int(input())  # Number of test cases
for _ in range(T):
    N = int(input())
    print(prime_sum[N])
