piFile = open("pi.txt", "r")
line0 = piFile.readline()
piDigits = piFile.readline()

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
        while color > 255:
            color -= 255
        rgbValues.append(color)
    
    return rgbValues

# We will use an n x 9 grid (n - rows and 9 columns)
print(len(piDigits))
print(value(5))