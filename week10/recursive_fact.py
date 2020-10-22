def recursive_fact(n):
    if n <= 0:
        raise Exception("Can't factorial a number less than 0")
    if n == 1:
        return n
    answer = recursive_fact(n - 1) * n
    return answer


if __name__ == "__main__":
    for x in range(1, 21):
        print(f"Recursive Factorial of {x} is {recursive_fact(x)}")
