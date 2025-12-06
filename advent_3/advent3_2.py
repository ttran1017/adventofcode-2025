INPUT = "input.txt"

TOTAL = 0
NUM_DIGITS = 12

RED = "\033[31m"
RESET = "\033[0m"

def print_highlighted(max_pointers: list, line: str):
    pointer_set = set(max_pointers)
    for i in range(len(line)):
        if i in pointer_set:
            print(f"{RED}{line[i]}{RESET}", end="")
        else:
            print(line[i], end="")
    print("")

def process(line: str):
    global TOTAL
    digits = []
    max_pointers = []
    barrier = 0

    for pointer in range(len(line) - NUM_DIGITS, len(line)):
        max_pointer = pointer 
        while(pointer > barrier):
            pointer -= 1
            if int(line[pointer]) >= int(line[max_pointer]):
                max_pointer = pointer
        
        barrier = max_pointer + 1
        digits.append(line[max_pointer])
        max_pointers.append(max_pointer)
    
    value = int("".join(digits))
    print(f"Got {value} from ", end="")
    print_highlighted(max_pointers, line)
    max_pointers = []
    TOTAL += value


def main():
    with open(INPUT, "r") as file:
        lines = file.readlines()
        for line in lines:
            process(line[:-1])
    print(f"Answer: {TOTAL}")


if __name__ == "__main__":
    main()