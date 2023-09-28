def factoriel(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def test(n):
    res = factoriel(n)
    print(f"The factorial of {n} is {res}")

def main():
    test(10)

main()