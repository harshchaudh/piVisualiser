piDigits = '141592653589793238462643383279502884197'
def value(place):
    values = []
    stringValues = piDigits[(place * 9):((place + 1) * 9)]
    for i in range(0, 3):
        values.append(float(stringValues[(i * 3):((i + 1) * 3)]))
    return values

# Converts three - three digit number into an RGB value.
def converter(values):
    rgbValues = []
    for color in values:
        if color > 255:
            while color > 255:
                color -= 255
        rgbValues.append(color)
    
    return rgbValues