# For creativity, I included a discount for a particular product (product no. D083) 
# which only discounts the price of one its items when a customer buys more than one quantity of the product

import csv
import datetime

# Define a function that reads a CSV file and returns a dictionary using a specified column as the key
def read_dictionary(filename, key_column_index):
    dictionary = {}
    with open (filename, "rt") as csv_file:
        # Read through each row in the csv file and convert them to strings using the .reader function from the csv module
        reader = csv.reader(csv_file)
        # Skip the header row
        next(reader) 
        # Loop through each row in the list
        for row_list in reader:
            if len(row_list) != 0:  # Skip empty rows
                # Store intended key in a variable 
                key = row_list[key_column_index]
                dictionary[key] = row_list  # Use the specified column as the key
    return dictionary 
    
def main():
    PRODUCT_NUM_INDEX = 0  # Index of product number in the products.csv file

    # Read product data into a dictionary
    products_dict = read_dictionary("products.csv", PRODUCT_NUM_INDEX)

    count = 0  # Track total number of items purchased
    sub_total = 0  # Track subtotal amount

    # Print store name which will be displayed on the receipt
    print("Danny All-Purpose Store")
    print()
    print(f"Your requested item(s): ")
    
    # Write a try statement that check for possible errors in the code blocks
    try:
        # Open and process the request file
        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)  # Skip header row
            # Loop through each row in request file
            for row_list in reader:
                if len(row_list) != 0:  # Skip empty rows
                    request_no = row_list[0]  # Store the product ID number in a variable
                    quantity = int(row_list[1])  # Store the product quantity in a variable

                    
                product_name = products_dict[request_no][1] # Get the product name from the dictionary and store in a variable using its index
                product_price = float(products_dict[request_no][2]) # Get the product price from the dictionary and store in a variable using its index
                print(f"{product_name}: {quantity} @ {product_price}") # Print purchase details 

                count += quantity  # Get count of the quantity of items requested
                sub_total += product_price * quantity  # Get a sub_total price of requested items
        print()     
        # Print a purchase summary
        print("Purchase Summary")
        print()
        print(f"Number of purchased items: {count}") 
        
        sales_tax = sub_total * (6 / 100)  # Calculate price for 6% of sales tax
        print(f"Subtotal: {sub_total:.2f}") 
        print(f"Sales Tax: {sales_tax:.2f}")

        amount_due = sub_total + sales_tax # Calculate total amount (i.e with tax included)
        print(f"Total: {amount_due:.2f}")
        print()

        print("We are giving a discount for Product No. D083 when a purchase of more than one is made.")
        print(f"A 50% discount will be given to only one of the purchased item")
        print()

        # Check for discount on specific product (Product No. "D083")
        total_quantity = 0
        product_price = float(products_dict["D083"][2])  # Store price of product D083 in a variable using its index

        # Count how many units of product "D083" were requested
        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)
            for row_list in reader:
                if row_list[0].strip() == "D083":
                    total_quantity += int(row_list[1])

        # Apply discount if more than one unit of product "D083" is purchased
        if total_quantity > 1:
            quantity_difference = total_quantity - 1  # Get number of items after deduction
            price = quantity_difference * product_price  # Get price of items without discount
            print(f"Price for {quantity_difference} items is {price} @ {product_price} each")
            discount_item = product_price * 0.5  # Get price of item with 50% discount
            print(f"Price for discounted item is {discount_item}")
            # Calculate amount payable after discount deduction
            total_amount_due = price + discount_item                   
            print(f"Therefore total amount due is {total_amount_due:.2f}")
        else:
            print("No discount applied for product D083.")

        print()

        # Print closing message with current date and time
        print("Thanks for your patronage!")
        now = datetime.datetime.now()
        formatted_date = now.strftime("%a %b %e %H:%M:%S %Y")
        print(formatted_date)

    # Handle file not found error
    except FileNotFoundError as file_not_found_err:
        print(file_not_found_err)
        print(f"Cannot open intended file because it does not exist")

    # Handle permission error when reading files
    except PermissionError as perm_err:
        print(perm_err)
        print(f"Cannot read from intended file because you do not have permission to access it")

    # Handle error when a product ID from the request file doesn't exist in the products dictionary
    except KeyError as key_err:
        print(key_err)
        print(f"Reconfirm product ID because intended product ID does not exist in the dictionary")


if __name__ == "__main__":
    main()
