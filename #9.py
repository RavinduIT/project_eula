import math

def find_max_triplet(N):
    max_product = -1
    # Iterate over possible values of m and n, where m > n > 0
    for m in range(2, int(math.sqrt(N)) + 1):
        for n in range(1, m):
            if (m - n) % 2 == 1 and math.gcd(m, n) == 1:  # m - n is odd and gcd(m, n) == 1 (for primitive triplets)
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                # Now scale this triplet by k such that a + b + c = N
                sum_abc = a + b + c
                if sum_abc > N:
                    continue
                k = N // sum_abc  # Maximum possible scaling factor
                scaled_a = k * a
                scaled_b = k * b
                scaled_c = k * c
                if scaled_a + scaled_b + scaled_c == N:
                    product = scaled_a * scaled_b * scaled_c
                    max_product = max(max_product, product)
    return max_product if max_product != -1 else -1

# Read input
T = int(input())  # Number of test cases
for _ in range(T):
    N = int(input())
    result = find_max_triplet(N)
    print(result)
