
# Given integer n, returns True or False based on reachability of goal
# See write up for "rules" for bears
def bears(n: int) -> bool:
    print(f"n: {n}")
    if n == 42:
        return True
    if n < 42:
        print(f"less than 42: {n}")
        return False
    if n % 5 == 0:
        check = bears(n - 42)
        if check is True:
            return True
    if n % 2 == 0:
        print(f"2% test: {(n // 10) * (n % 10)}")
        check = bears(n // 2)
        if check is True:
            return True
    if n % 3 == 0 or n % 4 == 0:
        print(f"mod test: {(n // 10) * (n % 10)}")
        check = bears(n - ((n // 10) * (n % 10)))
        if check is True:
            return True
    return False


