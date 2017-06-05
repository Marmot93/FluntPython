import time


def colck(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked


@colck
def snooze(seconds):
    time.sleep(seconds)


@colck
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


# if __name__ == '__main__':
#     print('*' * 40, 'Calling snooze(.123)')
#     snooze(.123)
#     print('*' * 40, 'Calling factorial(6)')
#     print('factorial(6)=', factorial(6))


# 测试标准库装饰器,优化递归的@functools.lru_cache()
# 1
@colck
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


if __name__ == "__main__":
    print(fib(8))

# 2
import functools

@functools.lru_cache()
@colck
def fib2(n):
    if n < 2:
        return n
    else:
        return fib2(n - 2) + fib2(n - 1)

if __name__ == "__main__":
    print(fib2(8))
