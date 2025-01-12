# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """
    Main function to handle user interaction and temperature conversion.
    """
    try:
        # Prompt the user to enter a temperature
        temperature = input("Enter the temperature to convert: ").strip()
        
        # Validate that the input is numeric
        if not temperature.replace('.', '', 1).isdigit() and not temperature.lstrip('-').replace('.', '', 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        temperature = float(temperature)
        
        # Prompt the user to specify the unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit not in ["C", "F"]:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        
        # Perform the appropriate conversion
        if unit == "F":
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp:.2f}°C")
        elif unit == "C":
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp:.2f}°F")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
