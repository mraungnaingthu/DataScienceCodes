from selectors import SelectSelector


def myCaches(func):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result

    return wrapper

@myCaches
def fibo(n):
    return 1 if n < 3 else fibo(n-1) + fibo(n-2)

if __name__ == "__main__":
    print(fibo(10))