def convert_length(value, direction):
    # 1 meter = 3.28084 feet
    if direction == 1:
        return value * 3.28084, "feet"
    elif direction == 2:
        return value / 3.28084, "meters"
    return None, ""

def convert_weight(value, direction):
    # 1 kilogram = 2.20462 pounds
    if direction == 1:
        return value * 2.20462, "lbs"
    elif direction == 2:
        return value / 2.20462, "kg"
    return None, ""

def convert_temperature(value, direction):
    if direction == 1:
        # Celsius to Fahrenheit
        return (value * 9/5) + 32, "°F"
    elif direction == 2:
        # Fahrenheit to Celsius
        return (value - 32) * 5/9, "°C"
    return None, ""

def main():
    print("====================================")
    print("   MULTI-UNIT CONVERTER TOOL")
    print("====================================")
    print("1. Distance (Meters <-> Feet)")
    print("2. Weight (Kilograms <-> Pounds)")
    print("3. Temperature (Celsius <-> Fahrenheit)")
    
    try:
        category = int(input("\nSelect category (1-3): "))
        if category not in [1, 2, 3]:
            print("Invalid category selection.")
            return

        print("\nDirection:")
        if category == 1:
            print("  1. Meters to Feet")
            print("  2. Feet to Meters")
        elif category == 2:
            print("  1. Kilograms to Pounds")
            print("  2. Pounds to Kilograms")
        elif category == 3:
            print("  1. Celsius to Fahrenheit")
            print("  2. Fahrenheit to Celsius")

        direction = int(input("Select direction (1-2): "))
        val = float(input("Enter value to convert: "))

        if category == 1:
            result, unit = convert_length(val, direction)
        elif category == 2:
            result, unit = convert_weight(val, direction)
        elif category == 3:
            result, unit = convert_temperature(val, direction)

        if result is not None:
            print(f"\nResult: {val} -> {result:.2f} {unit}")
        else:
            print("Invalid conversion choice.")

    except ValueError:
        print("Error: Please enter valid numerical inputs only.")

if __name__ == "__main__":
    main()
