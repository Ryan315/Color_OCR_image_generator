import random

# Function to crop lines longer than N characters into separate lines
def random_crop_lines(input_file_path, output_file_path, N):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        line = line.rstrip('\n')  # Remove newline character at the end of the line
        while len(line) > N:
            # Randomly choose a position to split the line
            split_position = random.randint(50, 100)
            new_lines.append(line[:split_position] + '\n')
            line = line[split_position:]
        new_lines.append(line + '\n')

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Example usage
input_file_path = './corpus/Cht_sanguoyanyi.txt'  # Replace with your input file path
output_file_path = './output.txt'  # Replace with your desired output file path
N = 150  # Replace with your desired line length

# Call the function
random_crop_lines(input_file_path, output_file_path, N)

output_file_path 