"""

"""

def add_recursive(n):
    if n == 1:
        return 1
    else:
        return n + add_recursive(n - 1)

def add_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    else:
        memo[n] = n + add_memoized(n - 1, memo)
        return memo[n]

print(add_recursive(5))  # Output: 15
print(add_memoized(5))   # Output: 15
