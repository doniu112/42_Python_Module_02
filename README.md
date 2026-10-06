*This project was created as part of the 42 curriculum by dswietoc.*

# Python Module 02 — Garden Guardian

Exception handling for garden data.

## Description

Exercises in building small, resilient programs with Python exceptions: validating temperature input, raising errors, defining custom exception classes, and cleaning up with finally.

## Requirements

- Python 3.10 or later.
- No third-party packages are needed to run the exercises.
- `flake8` and `mypy` are optional development tools for linting and type checking.

## Setup

```bash
git clone https://github.com/doniu112/42_Python_Module_02.git
cd 42_Python_Module_02
```

The commands below use a Linux, macOS, or WSL shell and `python3`.

## Exercises

| Exercise | File | Purpose |
| --- | --- | --- |
| ex0 | [ft_first_exception.py](ex0/ft_first_exception.py) | Convert temperature input and catch invalid integer conversion. |
| ex1 | [ft_raise_exception.py](ex1/ft_raise_exception.py) | Accept temperatures from 0 to 40 degrees Celsius, inclusive. |
| ex2 | [ft_different_errors.py](ex2/ft_different_errors.py) | Demonstrate four built-in exception types. |
| ex3 | [ft_custom_errors.py](ex3/ft_custom_errors.py) | Define and catch GardenError, PlantError, and WaterError. |
| ex4 | [ft_finally_block.py](ex4/ft_finally_block.py) | Close a simulated watering system even when a plant is invalid. |

## Usage

Run the demonstrations from the repository root:

```bash
python3 ex0/ft_first_exception.py
python3 ex1/ft_raise_exception.py
python3 ex2/ft_different_errors.py
python3 ex3/ft_custom_errors.py
python3 ex4/ft_finally_block.py
```

The scripts contain their own test inputs. No command-line arguments or interactive input are required.

## Implementation notes

- Exercise 1 accepts `"0"` and `"40"`; invalid numbers and temperatures outside that interval raise `ValueError`.
- Exercise 2 deliberately triggers `ValueError`, `ZeroDivisionError`, `FileNotFoundError`, and `TypeError`. The test function catches them and continues.
- Custom exceptions have default messages and can also receive a specific message.
- Catching `GardenError` also catches its subclasses `PlantError` and `WaterError`.
- Exercise 4 stops watering on the first invalid plant name. Its `finally` block still prints the cleanup message before control returns to the caller.

## Code quality

Create a virtual environment and install the development tools:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install flake8 mypy
```

From the repository root:

```bash
python3 -m flake8 ex*/*.py
python3 -m mypy --strict --explicit-package-bases ex*/*.py
```

**Expected mypy diagnostic:** exercise 2 intentionally evaluates `'something' + 1` to demonstrate a real `TypeError`. Therefore, the full check reports an `[operator]` error for that expression, as anticipated by the assignment. Do not remove the demonstration just to silence this diagnostic.

To check the other exercises separately:

```bash
python3 -m mypy --strict --explicit-package-bases ex0 ex1 ex3 ex4
```

## Related modules

- [Module 00 — Growing Code](https://github.com/doniu112/42_Python_Module_00)
- [Module 01 — Code Cultivation](https://github.com/doniu112/42_Python_Module_01)
- [Module 03 — Data Quest](https://github.com/doniu112/42_Python_Module_03)
- [Module 04 — Data Archivist](https://github.com/doniu112/42_Python_Module_04)

