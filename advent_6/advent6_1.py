INPUT="advent_6/input.txt"
total=0
compute_range = []

def compute(r: list, operation: str):
    global total
    buffer = int(r[0])
    for num in r[1:]:
        if operation == "*":
            buffer *= int(num)
        if operation == "+":
            buffer += int(num)
    # print(f"{buffer} from {operation} of {r}")
    total += buffer



def process():
    global compute_range
    for r in compute_range:
        operation = r[-1]
        working_range = r[:-1]
        compute(working_range, operation)


def main():
    global total, compute_range
    with open(INPUT, "r") as file:
        lines = file.readlines()
        compute_range = [[] for _ in range(len(lines[0].split()))]

        for line in lines:
            split_line = line.split()
            for i, var in enumerate(split_line):
                compute_range[i].append(var)

        process()
    print(f"Total: {total}")

if __name__ == "__main__":
    main()