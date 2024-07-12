def decorator1(func):
    def wrapper(param, *args, **kwargs):
        initial_value = "value from decorator1"
        print(f"{initial_value=}")
        return func(param, initial_value)

    return wrapper


def decorator2(func):
    def wrapper(param, input_from_decorator=None, *args, **kwargs):
        derived_value = f"value from decorator2 derived from {input_from_decorator}"
        print(f"{derived_value=}")
        return func(param, derived_value)

    return wrapper


@decorator1
@decorator2
def my_function(param, input_from_decorator=None):
    return f"{param=} and {input_from_decorator=}"


if __name__ == "__main__":
    result = my_function("example_param")  # Example usage
    print(f"{result=}")
