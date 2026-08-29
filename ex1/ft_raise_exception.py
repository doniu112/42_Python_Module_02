def input_temperature(temp_str: str) -> int:
    try:
        if temp_str < 0 or temp_str > 40:
            temperature = int(temp_str)
    except ValueError:
        print()
    else:
        return temperature

def test_temperature(testing_value):
    try:
        temperature = input_temperature(testing_value)
        return f"Temperature is now {temperature}°C"
    except ValueError:
        return f"Caught input_temperature error: invalid literal for int() with base 10: '{testing_value}'"



if __name__ == '__main__':
    print("=== Garden Temperature ===\n")

    value = '25'
    print(f"Input data is '{value}'")
    print(f"{test_temperature(value)}\n")

    value = 'abc'
    print(f"Input data is '{value}'")
    print(f"{test_temperature(value)}\n")

    print("All tests completed - program didn't crash!")