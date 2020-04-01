distance_to_pump=50
mpg=2
fuel_left=25
def zero_fuel(distance_to_pump,mpg,fuel_left):
    if (fuel_left*mpg>=distance_to_pump):
        return True
    else:
        return False