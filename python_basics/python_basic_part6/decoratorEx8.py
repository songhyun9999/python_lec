
def type_check(type_a, type_b):
    def real_decorator(func):
        def wrapper(n1, n2):
            if isinstance(n1, type_a) and isinstance(n2, type_b):
                return func(n1, n2)
            else:
                raise RuntimeError('자료형이 올바르지 않습니다.')
        return wrapper
    return real_decorator


@type_check(int, int)
def add(n1, n2):
    return n1 + n2

@type_check(float, float)
def multiply(n1, n2):
    return n1 * n2

# print(add(10, 20))
# print(add(10, 20.44))
print(multiply(323.32, 634.4))
print(multiply(323.32, 634))