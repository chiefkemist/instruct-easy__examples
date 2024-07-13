
from functools import wraps
from typing import Any, Callable


def decorator1(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(param: str, *args, **kwargs) -> Any:
        initial_value = "value from decorator1"
        print(f"{initial_value=}")
        return func(param, initial_value)

    return wrapper


def decorator2(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(param: str, input_from_decorator: str = None, *args, **kwargs) -> Any:
        derived_value = f"value from decorator2 derived from [{input_from_decorator=}]"
        print(f"{derived_value=}")
        return func(param, derived_value)

    return wrapper


@decorator1
@decorator2
def my_function(param: str, input_from_decorator: str = None) -> str:
    return f"{param=} and {input_from_decorator=}"


# decorator3 is similar to decorator1 but takes an initial parameter
# so that it is used as such @decorator3(initial_param)
# and the decorator3 function is defined as such:
def decorator3(initial_param: str) -> Callable:
    def decorator3_inner(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(param: str, *args, **kwargs) -> Any:
            dec3_param = f"value from decorator3 derived from [{initial_param=}] and {param=}"
            print(f"{dec3_param=}")
            return func(param, dec3_param)

        return wrapper

    return decorator3_inner


# In the same manner, decorator4 is similar to decorator2 but takes an initial parameter
# so that it is used as such @decorator4(initial_param)
# and the decorator4 function is defined as such:
def decorator4(initial_param: str) -> Callable:
    def decorator4_inner(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(param: str, input_from_decorator: str = None, *args, **kwargs) -> Any:
            dec4_param = f"value from decorator4 derived from [{initial_param=}] and [{input_from_decorator=}]"
            print(f"{dec4_param=}")
            return func(param, dec4_param)

        return wrapper

    return decorator4_inner


@decorator3("init_val3")
@decorator4("init_val4")
def my_other_function(param: str, input_from_decorator: str = None) -> str:
    return f"{param=} and {input_from_decorator=}"


if __name__ == "__main__":
    result = my_function("example_param")  # Example usage
    print(f"{result=}\n")

    other_result = my_other_function("other_example_param")  # Example usage
    print(f"{other_result=}\n")
