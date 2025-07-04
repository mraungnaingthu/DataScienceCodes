from functools import lru_cache

@lru_cache(maxsize=5)
def fact(n):
    print(f"calling function with n = {n}")
    return 1 if n<1 else n * fact(n-1)


print(fact(7))
print("After printing factorial 7...")
print(fact(8))