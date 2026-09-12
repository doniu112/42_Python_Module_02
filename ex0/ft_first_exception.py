def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature(testing_value):
    try:
        temperature = input_temperature(testing_value)
        return f"Temperature is now {temperature}°C"
    except ValueError:
        return (
                f"Caught input_temperature error: invalid "
                f"literal for int() with base 10: '{testing_value}'"
        )


if __name__ == '__main__':
    print("=== Garden Temperature ===\n")

    value = '25'
    print(f"Input data is '{value}'")
    print(f"{test_temperature(value)}\n")

    value = 'abc'
    print(f"Input data is '{value}'")
    print(f"{test_temperature(value)}\n")

    print("All tests completed - program didn't crash!")
