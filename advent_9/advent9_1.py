INPUT = "advent_9/input.txt"


def area(n1, n2):
    x1, y1 = [int(k) for k in n1]
    x2, y2 = [int(k) for k in n2]

    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
 
def main():
    with open(INPUT, "r") as file:
        lines = file.readlines()

    nodes = []
    for line in lines:
        nodes.append(line.strip().split(","))

    weights = []
    for i in range(len(nodes)):
        for j in range(i, len(nodes)):
            weights.append((area(nodes[i], nodes[j]), i, j))

    sorted_weights = sorted(weights, key=lambda x: x[0], reverse=True)
    print(sorted_weights)

    largest_area, n1, n2 = sorted_weights[0]
    print(f"LARGEST AREA: {largest_area}, n1: {nodes[n1]}, n2: {nodes[n2]}")

if __name__ == "__main__":
    main()