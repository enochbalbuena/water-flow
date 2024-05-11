def water_column_height(tower_height, tank_height):
    return tower_height + (3 * tank_height) / 4

def pressure_gain_from_water_height(height):
    density_water = 998.2
    gravity = 9.80665
    return (density_water * gravity * height) / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    density_water = 998.2
    return (-friction_factor * pipe_length * density_water * fluid_velocity**2) / (2000 * pipe_diameter)
