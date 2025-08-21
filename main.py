def sort(width, height, length, mass):
    # Check for bulky
    volume = width * height * length
    is_bulky = (
        volume >= 1_000_000 or
        width >= 150 or
        height >= 150 or
        length >= 150
    )
    
    # Check for heavy
    is_heavy = mass >= 20

    # Determine the correct stack
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

print(sort(100, 100, 100, 10))  # STANDARD
print(sort(200, 50, 20, 10))    # SPECIAL (bulky due to width)
print(sort(50, 50, 50, 25))     # SPECIAL (heavy)
print(sort(200, 200, 200, 25))  # REJECTED (both heavy and bulky)

