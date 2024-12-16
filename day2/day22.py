safe = 0
unsafe = 0

def is_line_safe(sequence):
    i = 0
    ascending = None  # Keep track of current trend (ascending/descending)
    while i < len(sequence) - 1:
        if sequence[i] < sequence[i + 1]:
            if ascending is False:
                return False
            ascending = True
        elif sequence[i] > sequence[i + 1]:
            if ascending is True:
                return False
            ascending = False
        else:
            return False

        if abs(sequence[i] - sequence[i + 1]) > 3:
            return False

        i += 1

    return True

with open('input21.txt', 'r') as file:
    for line in file:
        input_sequence = list(map(int, line.split()))
        if is_line_safe(input_sequence):
            safe += 1
        else:
            line_safe_after_removal = False
            for j in range(len(input_sequence)):
                modified_sequence = input_sequence[:j] + input_sequence[j+1:]
                if is_line_safe(modified_sequence):
                    line_safe_after_removal = True
                    break

            if line_safe_after_removal:
                safe += 1
            else:
                unsafe += 1

print(f"safe = {safe}")
print(f"unsafe = {unsafe}")
