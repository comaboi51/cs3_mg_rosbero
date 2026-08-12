earth_weight = input("what is ur weight on earth (in kg)?")
destination = input("where r u going? Mars, Jupiter or the Moon?")

def calculate_space_weight(earth_weight, destination):
    Mars = 0.38
    Jupiter = 2.34
    Moon = 0.16
    if destination == 'Mars':
        return (earth_weight*Mars)
    elif destination == 'Jupiter':
        return (earth_weight*Jupiter)
    elif destination == 'Moon':
        return (earth_weight*Moon)
    else:
        print("ERROR")
        return None


calculate_space_weight(earth_weight,destination)
final = calculate_space_weight
print("ur space weight is:")
print(final)