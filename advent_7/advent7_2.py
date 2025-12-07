INPUT = "advent_7/input.txt"


def print_line(tracker, line):
    counter = 0
    for i, char in enumerate(line):
        if char == "^":
            print("^", end="")
        elif tracker[i]:
            counter += int(tracker[i])
            print(tracker[i], end="")
        else:
            print(".", end="")
    print(f" Count: {counter}")

def process(tracker: list, line: list):
    global counter
    for i, char in enumerate(line):
        if char == "S":
            tracker[i] = 1
        if char == "^" and tracker[i]:
            if i != 0:
                tracker[i-1] += tracker[i]
            if i != len(line) - 1:
                tracker[i+1] += tracker[i]
            tracker[i] = 0
    print_line(tracker, line)

def main():
    with open(INPUT, "r") as file:
        global counter
        lines = file.readlines()
        tracker = [0 for _ in range(len(lines[0]))]

        for line in lines:
            process(tracker, line)

if __name__ == "__main__":
    main()