"""
When applied to a function, this will raise an exception if the input types don't match the type hints
The type enforcer is expensive to run (~1ms per run), so use it only for user facing functions
"""

import inspect


def type_enforcer(input_function):
    """
        raises a type error if the given arguments don't match the signature
        try to do as much at initialisation, to lower performance cost (and increase memory cost)
    """
    signature = inspect.signature(input_function)
    required_args = [signature.parameters[x].annotation for x in signature.parameters.keys()]
    required_kwargs = {x: signature.parameters[x].annotation for x in signature.parameters.keys() if
                       signature.parameters[x].default != signature.empty}

    def function_wrapper(*args, **kwargs):
        # test positional arguments
        correct_args = [isinstance(x, required_args[n]) for n, x in enumerate(args) if
                        required_args[n] is not inspect._empty]
        if not all(correct_args):
            raise TypeError

        # test keyword arguments
        correct_kwargs = [isinstance(val, required_kwargs[key]) for key, val in kwargs.items()]
        if not all(correct_kwargs):
            raise TypeError

        return input_function(*args, **kwargs)

    return function_wrapper


if __name__ == "__main__":
    # local imports for tests
    from time import perf_counter_ns

    ns_to_ms = 1e-6


    # local tests to check type enforcement and give examples of how to use it
    @type_enforcer
    def simple_test(x: int, y: str, a: int = 2, b: str = "x"):
        return x, y, a, b


    print('\n' + '=' * 20)
    print("Running simple tests")
    print("Running passing simple test")
    simple_test(1, "string", 1, b="string")
    print("Passing state successfully passed\n")
    print("Running failing simple test")
    try:
        # your IDE should highlight the following statement
        simple_test("string", 1, a='x')
    except TypeError as e:
        print("Failing state successfully failed\n")


    @type_enforcer
    def multi_types(x: int | str, y, z: dict | tuple = ()):
        return x, y, z


    print('\n' + '=' * 20)
    print("Running multiple type tests")
    print("Running passing multiple type test")
    multi_types("string", 1.0, {'key': 'value'})
    print("Passing state successfully passed\n")
    print("Running failing multiple type test")
    try:
        multi_types(5, ("tuple"), [1])
    except TypeError as e:
        print("Failing state successfully failed\n")


    # benchmark tests
    def benchmark_control(x: int):
        return x + 1


    @type_enforcer
    def benchmark_test(x: int):
        return x + 1


    print('\n' + '=' * 20)
    print("Running benchmark tests")

    control_start_time = perf_counter_ns()
    for _ in range(100000):
        benchmark_control(1)
    control_end_time = perf_counter_ns() - control_start_time

    print(f"Control benchmark complete, elapsed time: {control_end_time * ns_to_ms}s")

    test_start_time = perf_counter_ns()
    for _ in range(100000):
        benchmark_test(1)
    test_end_time = perf_counter_ns() - test_start_time

    print(f"Simple benchmark complete, elapsed time: {test_end_time * ns_to_ms}s")
