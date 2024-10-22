def find_greatest_product(T, test_cases):
    results = []
    
    for i in range(T):
        N, K = test_cases[i][0]
        num_str = test_cases[i][1]
        
        max_product = 0
        
        for j in range(N - K + 1):
            product = 1
            for digit in num_str[j:j + K]:
                product *= int(digit)
            max_product = max(max_product, product)
        
        results.append(max_product)
    
    return results

# Input format
T = int(input())
test_cases = []

for _ in range(T):
    N, K = map(int, input().split())
    num_str = input().strip()
    test_cases.append(((N, K), num_str))

# Find greatest product for each test case
results = find_greatest_product(T, test_cases)

# Output results
for result in results:
    print(result)
