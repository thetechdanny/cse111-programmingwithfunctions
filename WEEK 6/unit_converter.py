from pint import UnitRegistry, DimensionalityError

# Create a UnitRegistry instance from Pint for unit conversions
ureg = UnitRegistry()

# Create a dictionary that contains example unit each its SI unit as keys
unit_examples = {
    "length": "meter",
    "mass": "kilogram",
    "time": "second",
    "speed": "meter/second"
}

# List SI prefixes in text stored as a list
prefixes = ['kilo', 'hecto', 'deka', 'deci', 'centi', 'milli', 'micro', 'nano']

def main():
    # Print SI unit conversion menu for the user
    print("Select unit to convert and press 0 to quit:")
    print("1. Length\n2. Mass\n3. Time\n4. Speed\n")

    # Match each menu choices to SI unit types
    unit_list = {
        "1": "length",
        "2": "mass",
        "3": "time",
        "4": "speed"
    }

    try:
        exit_program = False
        # Loop until the user decides to exit
        while not exit_program:
            # Prompt user for unit type selection
            choice = input("Select a unit by typing in the associated number (1-4) or 0 to quit: ").strip()
            if choice == "0":
                print("Thanks for using my program. Goodbye!")
                break
            if choice not in unit_list:
                print("You typed an invalid number. Please select a valid number from the list.")
                continue
            # Get the selected unit type and its example unit
            choice_unit = unit_list[choice]
            example_unit = unit_examples[choice_unit]

            print()
            print(f"Units compatible with {choice_unit} and its common sub-units:")
            # Get all units compatible with the selected type
            compatible_units = sorted(ureg.get_compatible_units(example_unit), key=str)
            
            for unit in compatible_units:
                unit_str = str(unit)
                found_subunits = []
                # Try to find SI sub-units by prefixing the unit name
                for prefix in prefixes:
                    subunit_name = prefix + unit_str
                    try:
                        # Check if the prefixed unit is valid
                        ureg.parse_units(subunit_name)
                        subunit_qty = 1 * ureg(subunit_name)
                        base_qty = 1 * ureg(example_unit)
                        # Only add if dimensionality matches and it's not the base unit
                        if subunit_qty.dimensionality == base_qty.dimensionality and subunit_name != unit_str:
                            found_subunits.append(subunit_name)
                    except Exception:
                        continue
                print(f"-- {unit_str}")
                if found_subunits:
                    for sub in found_subunits:
                        print(f"    -- {sub}")
                else:
                    print("    -- No common SI sub-units found")
                print()

            # Get value to convert from user
            while True:
                value_str = input("Type the value to be converted (e.g 100, 20, 35): ").strip()
                try:
                    value = float(value_str)
                    break
                except ValueError:
                    print("Invalid number. Please type in a valid numeric value.")

            # Get initial and target units from user
            initial_unit = input("Type the initial unit: ").strip()
            converted_unit = input("Type the unit to convert to: ").strip()

            # Try to perform the conversion and handle errors
            try:
                conversion = convert_unit(initial_unit, converted_unit, value)
                print(f"Result: {value} {initial_unit} = {conversion:.3f} {converted_unit}")
            except DimensionalityError as dimerr:
                print(f"Error: {dimerr}\nPlease make sure you are converting between compatible units.")
            except Exception as e:
                print(f"Error: {e}\nPlease check your unit names and try again.")

            # Ask user if they want to continue
            while True:
                continue_choice = input("Do you want to perform another conversion? (yes/no): ").strip().lower()
                if continue_choice in ['yes', 'no']:
                    break
                print("Please type 'yes' or 'no'.")
            if continue_choice == 'no':
                print("Exiting the program. Goodbye!")
                exit_program = True

    except Exception as excep:
        print(f"Sorry, an unexpected error occurred: {excep}")

def list_units(unit_type):
    # Return a sorted list of all units compatible with the given type
    example_unit = unit_examples[unit_type]
    compatible_units = ureg.get_compatible_units(example_unit)
    return sorted([str(u) for u in compatible_units])

def convert_unit(from_unit, to_unit, number):
    # Convert a value from one unit to another using Pint
    quantity = number * ureg(from_unit)
    converted = quantity.to(to_unit)
    return converted.magnitude

if __name__ == "__main__":
    main()
