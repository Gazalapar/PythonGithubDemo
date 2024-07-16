# Writing data to the file
'''f = open("C:\\Users\\gazala parveen\\OneDrive\\Documents\\txt files\\Exercise1.txt", "w")
f.write("6,8 \n7,6 \n2,8 \n9,5\n9,6")
f.close()

def countNum(num):
    count = 0
    with open("C:\\Users\\gazala parveen\\OneDrive\\Documents\\txt files\\Exercise1.txt", "r") as f_read:
        for line in f_read:
            tokens = line.split(",")
            # Convert tokens to integers and strip whitespace
            tokens = [int(token.strip()) for token in tokens]
            # Count occurrences of the number
            count += tokens.count(num)
    return count

# Example usage
num_to_count = 9
occurrences = countNum(num_to_count)
print(f'The number {num_to_count} appears {occurrences} times in the file.')'''
# Writing initial data to the file
file_path = "C:\\Users\\gazala parveen\\OneDrive\\Documents\\txt files\\Exercise1.txt"
with open(file_path, "w") as f:
    f.write("6,8 \n7,6 \n2,8 \n9,5\n9,6")


def update_file_with_sums(file_path):
    # Read the lines from the file
    with open(file_path, "r") as f:
        lines = f.readlines()

    # Process each line and store updated lines
    updated_lines = []
    for line in lines:
        # Remove whitespace, split by comma, and convert to integers
        numbers = [int(num.strip()) for num in line.split(",")]
        # Calculate the sum of numbers in the line
        line_sum = sum(numbers)
        # Create the new line format
        updated_line = f"sum:{line_sum}| " + ",".join(map(str, numbers)) + "\n"
        updated_lines.append(updated_line)

    # Write the updated lines back to the file
    with open(file_path, "w") as f:
        f.writelines(updated_lines)


# Call the function to update the file
update_file_with_sums(file_path)

# Read and print the updated file content to verify
with open(file_path, "r") as f:
    updated_content = f.read()
    print(updated_content)











