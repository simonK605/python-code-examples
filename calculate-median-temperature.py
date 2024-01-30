import statistics


def calculate_median_temperature(temperature_list):
    return statistics.median(temperature_list)


def main() -> None:
    monthly_temperatures = [5, 6, 7, 8]

    median_temperature = calculate_median_temperature(monthly_temperatures)
    print(f"The median temperature is {median_temperature} degrees.")  # Output: The median temperature is 6.5 degrees.


if __name__ == "__main__":
    main()