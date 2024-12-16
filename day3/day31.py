import re

def extract_sequences_and_sum_from_file(file_path):
    # Define the regex pattern
    pattern = r"mul\(\d+,\d+\)"

    # Read the content of the file
    with open(file_path, 'r') as file:
        input_string = file.read()

    # Find all matches in the input string
    matches = re.findall(pattern, input_string)

    total_sum = 0
    for match in matches:
        # Extract the numbers from each match
        numbers = list(map(int, re.findall(r"\d+", match)))
        # Multiply the numbers and add to the total sum
        total_sum += numbers[0] * numbers[1]

    return matches, total_sum

# Example usage
if __name__ == "__main__":
    file_path = "input31.txt"  # Path to the input file
    results, total = extract_sequences_and_sum_from_file(file_path)
    print("Matches:", results)
    print("Total Sum:", total)
