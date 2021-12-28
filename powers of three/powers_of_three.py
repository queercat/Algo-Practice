'''
Example: Print all positive integer solutions to the equation a^3 + b^3 = C^3 + D^3
and d are integers between 1 and 1000. 
'''

memo = {}

for c in range(1, 1000):
    for d in range(1, 1000):
        result = pow(c, 3) + pow(d, 3)
        
        if result not in memo:
            memo[result] = []

        memo[result].append((c, d))

for a in range(1, 1000):
    for b in range(1, 1000):
        result = pow(a, 3) + pow(b, 3)
        
        if result in memo:
            for pair in memo[result]:
                print((a, b), pair)

# O(n^2)