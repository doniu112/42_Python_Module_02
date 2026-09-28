class GardenError(Exception):
	def __init__(self, message: str = "Unknown garden error") -> None:
		Exception.__init__(self, message)


class PlantError(GardenError):
	def __init__(self, message: str = "Unknown plant error") -> None:
		super().__init__(message)


class WaterError(GardenError):
	def __init__(self, message: str = "Unknown water error") -> None:
		super().__init__(message)


def check_plant(is_wilting: bool) -> None:
	if is_wilting:
		raise PlantError("The tomato plant is wilting!")


def check_water(water_level: int) -> None:
	if water_level < 1:
		raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
	print("=== Custom Garden Errors Demo ===\n")

	print("Testing PlantError...")
	try:
		check_plant(True)
	except PlantError as error:
		print(f"Caught PlantError: {error}")

	print("\nTesting WaterError...")
	try:
		check_water(0)
	except WaterError as error:
		print(f"Caught WaterError: {error}")

	print("\nTesting catching all garden errors...")
	try:
		check_plant(True)
	except GardenError as error:
		print(f"Caught GardenError: {error}")

	try:
		check_water(0)
	except GardenError as error:
		print(f"Caught GardenError: {error}")

	print("\nTesting normal operations...")
	check_plant(False)
	check_water(10)
	print("Plant and water checks passed!")

	print("\nAll custom error types work correctly!")


def main() -> None:
	test_custom_errors()


if __name__ == "__main__":
	main()
