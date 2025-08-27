# For creativity, I added a function (compute_element_analysis) that computes the chemical formula analysis, showing the name and number of atoms each element in the chemical compound is made up of 

# Import the csv module to be used in reading a csv file later in the code
import csv

# Import the parse formula from the formula library to converts a chemical formula for a molecule into a compound list
from formula import parse_formula

# Define a function with no parameter, that reads a csv file of chemical elements and returns them as a dictionary
def make_periodic_table():

    # Create an empty dictionary variable that stores the lists of chemical elements to be returned when the function is called
    dictionary = {}

    # Open the cvs file
    with open("elements.csv", "rt", encoding="utf-8") as csv_file:

        # Call the reader object in the csv module that reads the csv file and retuns each row as a list and stores in the reader variable
        reader = csv.reader(csv_file)

        # Skip the header row of the cvs file 
        next(reader)  

        # Loop through each list 
        for row_list in reader:
            element_symbol = row_list[0] # Store the element symbol in a variable using its index
            element_name = row_list[1]   # Store the element name in a variable using its index
            atomic_mass = float(row_list[2]) # Store the element's atomic mass in a variable using its index
            if atomic_mass.is_integer():  # Retains the data type of the atomic mass if it's an integer
                atomic_mass = int(atomic_mass)

             # Store teh element's name and atomic mass in the dictionary using the symbol as the key  
            dictionary[element_symbol] = [element_name, atomic_mass]

    return dictionary

# Define a function that computes and returns the molar mass of all elements found in a compound list
def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    total_mass = 0  # Set the initial value of 0 to the total_mass
    
    # Loop through each element in the list
    for symbol in symbol_quantity_list:
        element = symbol[0]                 # Store element symbol in a variable using its index
        quantity_of_atoms = symbol[1]       # Store the number of atoms of the element in a variable using the index
        
        # If the element is in the periodic table, get its atomic weight
        if element in periodic_table_dict:
            atomic_weight = periodic_table_dict[element][1]  # Get the atomic weight from the dictionary
            mass = quantity_of_atoms * atomic_weight         # Calculate the mass 
            total_mass += mass                               # Add to total mass
    return total_mass

# Define a function that returns the number of atoms of individual elements
def compute_element_analysis(chemical_formula, periodic_table_dict):
    symbol_quantity_list = parse_formula(chemical_formula, make_periodic_table())
    
    element_analysis_list = []  # Initialize list to hold analysis strings for each element
    
    # Loop through each element 
    for symbol in symbol_quantity_list:
        element_symbol = symbol[0]     # Store the element symbol in a variable using its index
        quantity = symbol[1]           # Store the number of atom of the element in a variable using its index
        
        # Check if the element exists in the periodic table
        if element_symbol in periodic_table_dict:
            element_name = periodic_table_dict[element_symbol][0] # Get the element's full name using its index and store it in a variable
            element_analysis_list.append(f"{quantity} atoms of {element_name}") # Add to the list
    return "Your chemical formula analysis: " + ", ".join(element_analysis_list) # Join analysis together

# Define a main function to receive user input and perform calculation
def main():
    
    # Ask user for a chemical formula
    print("Chemical formula are case sensitive, use proper casing for elements")
    chemical_formula = input("Input a chemical formula: ")
    sample_size = float(input("What is the sample size in grams: "))
    print()

    # Extract element symbols and quantities
    element_and_quantity = parse_formula(chemical_formula, make_periodic_table())

    # Create a dictionary representing the periodic table
    elements_dictionary = make_periodic_table()

    # Compute and print the element's molar mass
    molar_mass = compute_molar_mass(element_and_quantity, elements_dictionary)
    print(f"The element's molar mass is {molar_mass}")

    # Calculate and print the number of moles
    moles = sample_size / molar_mass
    print(f"The number of moles is {moles}")

    # Compute and print element's analysis
    analysis = compute_element_analysis(chemical_formula, make_periodic_table())
    print(analysis)
    print()


if __name__ == "__main__":
  main()