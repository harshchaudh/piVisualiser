# Define the paths for the original and new files
original_file_path = "pi.txt"
new_file_path = "formatted_file.txt"

# Open the original file in read mode
with open(original_file_path, "r") as original_file:
    # Read all lines from the original file
    lines = original_file.readlines()

    # Open the new file in write mode
    with open(new_file_path, "w") as new_file:
        # Iterate through each line
        for i, line in enumerate(lines):
            # Remove any leading/trailing whitespace and split the line into a list of individual digits
            digits = line.strip()

            # Pad the line with spaces to make it 81 digits per line
            padded_line = digits + " " * (81 - len(digits))

            # Check if the line has less than 81 digits
            if len(digits) < 81 and i + 1 < len(lines):
                # Read the next line
                next_line_digits = lines[i + 1].strip()

                # Calculate how many digits to take from the next line
                remaining_digits = 81 - len(padded_line)

                # Concatenate the necessary digits from the next line
                padded_line += next_line_digits[:remaining_digits]

            # Write the padded line to the new file
            new_file.write(padded_line + "\n")
