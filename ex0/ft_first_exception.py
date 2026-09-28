def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature(testing_value) -> None:
    print(f"Input data is '{testing_value}'")
    try:
        temperature = input_temperature(testing_value)
        print(f"Temperature is now {temperature}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print()


def main() -> None:
    print("=== Garden Temperature ===\n")

    test_temperature('25')

    test_temperature('abc')

    test_temperature('100')

    test_temperature('-50')

    print("All tests completed - program didn't crash!")


if __name__ == '__main__':
    main()
