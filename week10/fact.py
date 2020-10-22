def fact(n):
    if n <= 0:
        raise Exception("Can't factorial a number less than 0")
    answer = 1
    for x in range(1, n + 1):
        answer *= x
    return answer

if __name__ == "__main__":
    for x in range(20):
        print(f"Factorial of {x} is {fact(x)}")
