
safe = 0
unsafe = 0

with open('input21.txt', 'r') as file:
    for line in file:


        i = 0
        is_safe = True
        ascending = None  # Keep track of current trend (ascending/descending)
        print(line)
        input = list(map(int, line.split()))
        while i < len(input) - 1 and is_safe:
            # Check if current segment is ascending or descending
            if input[i] < input[i + 1]:
                if ascending is False:  # Switching from descending to ascending
                    unsafe += 1
                    is_safe = False
                ascending = True
            elif input[i] > input[i + 1]:
                if ascending is True:  # Switching from ascending to descending
                    unsafe += 1
                    is_safe = False
                ascending = False
            else:  # Values are equal
                unsafe += 1
                is_safe = False

            if (abs(input[i] - input[i+1])) > 3:
                unsafe += 1
                is_safe = False
            i += 1

        if is_safe:
            safe += 1



print(f"safe = {safe}")
print(f"unsafe = {unsafe}")
