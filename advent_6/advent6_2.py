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
    print(f"{buffer} from {operation} of {r}")
    total += buffer

def process(compute_range):
    VALID_OPERATIONS = {"*", "+"}
    
    combined_list = []
    for r in compute_range:
        combined_list.append("".join(r).strip())

    num_list = []
    operation = ""
    for r in combined_list:
        if not r:
            compute(num_list, operation)
            num_list = []
            operation = ""
            continue

        if r[-1] in VALID_OPERATIONS:
            operation = r[-1]
            num_list.append(r[:-1])
            continue
        
        num_list.append(r)

def main():
    with open(INPUT, "r") as file:
        lines = file.readlines()
        compute_range = [[] for _ in range(len(lines[0]))]

        for line in lines:
            for i, var in enumerate(line):
                compute_range[i].append(var)
        
        process(compute_range)

    print(compute_range)
    print(f"Total: {total}")

if __name__ == "__main__":
    main()