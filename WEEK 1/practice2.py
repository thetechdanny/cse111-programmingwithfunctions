# Define the main function
def main():
    # Get the start, end and fuel values from user
    start_value = float(input("What is the start value: "))
    end_value = float(input("What is the end' value: "))
    fuel_price = float(input("What is the fuel price: "))
       
    # Call the miles per gallon function and save its value in a variable
    fuel_efficiency_mpg = miles_per_gallon(start_value, end_value, fuel_price)
        
    # Call the mpg convertion funtion to litres per 100 kilometer
    fuel_efficiency_lp100k = litres_per_kilometer(fuel_efficiency_mpg)

    # Print the fuel efficiencies in mpg and in lp100k
    print(f"The fuel efficiency in mpg is: {fuel_efficiency_mpg}")
    print(f"The fuel efficiency in litre per 100 kilometers is: {fuel_efficiency_lp100k}")

# Define a function called miles_per_gallon to calculate fuel efficiecny in mpg
def miles_per_gallon(start, end, gallons):
    
    # Compute the fuel efficiency
    fuel_efficiency = ((end - start) / gallons)

    # Return the fuel efficiency to be used later in the program
    return fuel_efficiency

# Define a function called litres per kilometers to convert the mpg to lp100k
def litres_per_kilometer(mpg, constant = 235.215):
    
    # Compute the fuel efficiency
    fuel_efficiency = constant / mpg

    # Return the fuel efficiency to be used later in the program
    return fuel_efficiency

main()