# To exceed requirement, I defined a function that converts kilopascals to pounds per square inch and prints both values to the user

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
WATER_DENSITY=998.2                  # density of water (998.2 kilogram / meter^3)

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    pressure_in_pounds_square_inch = convert_kilopascals_to_pounds_per_square_inch(pressure)
    print()
    print(f"Pressure at house in kilopascals: {pressure:.1f}kPa")
    print(f"Pressure at house in pounds per squre inch: {pressure_in_pounds_square_inch:.1f}psi")
    print()

def water_column_height(tower_height, tank_height):
    return tower_height + 3 * tank_height / 4

def pressure_gain_from_water_height(height):
    #TODO: Need to implement
    pressure = (998.2 * 9.80665 * height) / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    numerator = -friction_factor * pipe_length * WATER_DENSITY * fluid_velocity ** 2
    denominator = 2000 * pipe_diameter
    return numerator / denominator

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    return -.04 * WATER_DENSITY * fluid_velocity ** 2 * quantity_fittings / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
      #TODO: Need to implement
      rey_numb = (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / 0.0010016
      return rey_numb

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    k=(0.1 + (50 / reynolds_number)) * (((larger_diameter / smaller_diameter) ** 4) - 1)
    pressure = (-k * WATER_DENSITY * fluid_velocity ** 2) / 2000
    return pressure

def convert_kilopascals_to_pounds_per_square_inch(kilopascals):
    pressure_in_pounds_per_square_inch = kilopascals * 0.145038
    return pressure_in_pounds_per_square_inch

if __name__ == "__main__":
    main()