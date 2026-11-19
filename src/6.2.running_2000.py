

import time
from typing import Any, Callable


def timer(f: Callable[..., Any], *args: Any, **kwargs: Any) -> float:
    """
    Measure the execution time of a function.
    """
    start_time = time.perf_counter()

    f(*args, **kwargs)

    end_time = time.perf_counter()

    return end_time - start_time


def main():
    print(timer(print, "Hello"))

    print(timer(zip, [1, 2, 3], [4, 5, 6]))

    print(timer("Hi {name}".format, name="Bug"))


if __name__ == "__main__":
    main()
