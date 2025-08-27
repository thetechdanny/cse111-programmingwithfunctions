# Import the math library to make use of the math.pi function
import math

# Define the main function
def main():

    # Get the list values of each can and store them in different lists
    can_names = [
        "#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5",
        "#6Z", "#8Z short", "#10", "#211", "#300", "#303"
    ]
    can_radiuses = [
        6.83, 7.78, 8.73, 10.32, 10.79, 13.02,
        5.4, 6.83, 15.72, 6.83, 7.62, 8.1
    ]
    can_heights = [
        10.16, 11.91, 11.59, 11.91, 17.78, 14.29,
        8.89, 7.62, 17.78, 12.38, 11.27, 11.11
    ]
    can_costs = [
        0.28, 0.43, 0.45, 0.61, 0.86, 0.83,
        0.22, 0.26, 1.53, 0.34, 0.38, 0.42
    ]

    best_storage_efficiency = -1
    best_cost_efficiency = -1
    best_can_storage = ""
    best_can_cost = ""
    
   
    # Print the volume, surface area, storage efficiency and cost efficiency values for each can
    for i in range(len(can_names)):
        
        # Call the volume function
        volume = compute_volume(can_radiuses[i], can_heights[i])

        # Call the surface area function
        surface_area = compute_surface_area(can_radiuses[i], can_heights[i])

        # Call the storage efficiency function
        storage_efficiency = compute_storage_efficiency(volume, surface_area)

        # Call the cost efficiency function
        cost_efficiency = compute_cost_efficiency(volume, can_costs[i])
        
        print(f"{can_names[i]} - volume: {volume:.2f}, surface area: {surface_area:.2f}, storage efficiency: {storage_efficiency:.2f} and cost efficiency: {cost_efficiency:.2f}")
        
        if storage_efficiency > best_storage_efficiency:
            best_storage_efficiency = storage_efficiency
            best_can_storage = can_names[i]

        if cost_efficiency > best_cost_efficiency:
            best_cost_efficiency = cost_efficiency
            best_can_cost = can_names[i]

    print(f"The best can storage efficiency is {best_can_storage} with storage efficiency of {best_storage_efficiency}\n and the best can with cost efficiency is {best_can_cost} with cost efficiency of {best_cost_efficiency}")

# Define the volume function
def compute_volume(radius, height):

    # Compute the volume
    volume = math.pi * radius**2 * height
    
    # Return the volume to be used later in the program
    return volume

# Define the surface area function
def compute_surface_area(radius, height):

    # Compute the surface area
    surface_area = (2 * math.pi * radius * (radius + height))

    # Return the surface area to be used later in the program
    return surface_area

# Define the storage efficiency function
def compute_storage_efficiency(volume, surface_area):
    
    # Compute the storage efficiency
    storage_efficiency = volume / surface_area

    # Return the value of storage efficiency to be used later in the program
    return storage_efficiency

# Define the cost efficiency
def compute_cost_efficiency(volume, cost):
    cost_efficiency = volume / cost
    return cost_efficiency

main()