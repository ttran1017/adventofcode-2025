INPUT="input.txt"

CHECK_DISTANCE = 1
ROLL_LIMIT = 4

total=0
diagram = []

def is_valid(i: int, j: int):
    global diagram
    sum = 0
    for i_offset in range(i-CHECK_DISTANCE, i+CHECK_DISTANCE+1):
        if i_offset < 0 or i_offset == len(diagram):
            continue

        for j_offset in range(j-CHECK_DISTANCE, j+CHECK_DISTANCE+1):
            if j_offset < 0 or j_offset == len(diagram[i_offset]):
                continue

            if i == i_offset and j == j_offset:
                continue

            sum += diagram[i_offset][j_offset]

    print(f"[{i},{j}] is {"valid" if sum < ROLL_LIMIT else "invalid"}")
    return sum < ROLL_LIMIT


def process():
    global diagram, total
    rolls_left = sum(map(sum,diagram))

    while True:
        for i in range(len(diagram)):
            for j in range(len(diagram[i])):
                if(diagram[i][j] and is_valid(i, j)):
                    total += 1
                    diagram[i][j] = 0

        if(rolls_left == sum(map(sum,diagram))):
            break

        rolls_left = sum(map(sum,diagram))

def main():
    global diagram, total
    with open(INPUT, "r") as file:
        rows = file.readlines()
        for i, row in enumerate(rows):
            diagram.append([])
            for col in row:
                diagram[i].append(1 if col == "@" else 0)

    process()

    print(f"Answer: {total}")


if __name__ == "__main__":
    main()