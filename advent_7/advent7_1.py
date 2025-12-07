INPUT = "advent_7/input.txt"

counter = 0

def print_line(tracker, line):
    for i, char in enumerate(line):
        if char == "^":
            print("^", end="")
        elif tracker[i]:
            print("|", end="")
        else:
            print(".", end="")
    print("")


def process(tracker: list, line: list):
    global counter
    for i, char in enumerate(line):
        if char == "S":
            tracker[i] = True
        if char == "^" and tracker[i]:
            counter += 1
            tracker[i] = False
            if i != 0:
                tracker[i-1] = True
            if i != len(line):
                tracker[i+1] = True
    print_line(tracker, line)

def main():
    with open(INPUT, "r") as file:
        global counter
        lines = file.readlines()
        tracker = [False for _ in range(len(lines[0]))]

        for line in lines:
            process(tracker, line)

        print(f"Final split count: {counter}")

if __name__ == "__main__":
    main()