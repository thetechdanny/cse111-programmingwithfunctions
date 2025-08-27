# Import the csv module to be used in reading a csv file later in the code
import csv

# Define a function with no parameter, that reads a csv file of chemical elements and returns them as a dictionary
def make_periodic_table():
    # Create an empty dictionary variable that stores the lists of chemical elements to be returned when the function is called
    dictionary = {}
    # Open the cvs file
    with open("elements.csv", "rt", encoding="utf-8") as csv_file:
        # Call the reader object in the csv module that reads the csv file and retuns each row as a list and stores in the reader variable
        reader = csv.reader(csv_file)
        ## Skip the header row of the cvs file 
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

# Define the main function that calls make_periodic_function and prints the elements in the dictionary
def main():
    periodic_table = make_periodic_table()
    print(periodic_table)

if __name__ == "__main__":
  main()

#   def compute_element_analysis(chemical_formula):
#     symbol_quantity_list = parse_formula(chemical_formula, make_periodic_table())
#     analysis_lines = []
#     for symbol, number_of_atoms in symbol_quantity_list:
#         analysis_lines.append(f"{number_of_atoms} atoms of {symbol}")
#     element_analysis = "Your element analysis: " + ", ".join(analysis_lines)
#     return element_analysis