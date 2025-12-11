INPUT = "advent_9/input.txt"

def within_or_no_collision(r1, r2) -> bool:
    r1_x1, r1_y1 = r1[1]
    r1_x2, r1_y2 = r1[2]
    r1_top, r1_bottom = (r1_y1, r1_y2) if r1_y1 > r1_y2 else (r1_y2, r1_y1)
    r1_left, r1_right = (r1_x1, r1_y2) if r1_x1 > r1_x2 else (r1_x2, r1_x1)

    r2_x1, r2_y1 = r2[1]
    r2_x2, r2_y2 = r2[2]
    r2_top, r2_bottom = (r2_y1, r2_y2) if r2_y1 > r2_y2 else (r2_y2, r2_y1)
    r2_left, r2_right = (r2_x1, r2_y2) if r2_x1 > r2_x2 else (r2_x2, r2_x1)

    within = r1_top <= r2_top and r1_bottom >= r2_bottom and r1_left >= r2_left and r1_right <= r2_right
    no_collision = not (r1_top > r2_bottom or r1_bottom < r2_top or r1_left < r2_right or r1_right > r2_left)
    return within or no_collision

def check_first_valid(recntangles):
    for i in range(len(recntangles)):
        found = True
        target = recntangles[i]
        for j in range(i+1, len(recntangles)):
            compare = recntangles[j]
            if not within_or_no_collision(target, compare):
                found = False
                break

        if found:
            print(target)

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

    rectangles = []
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            rectangles.append((area(nodes[i], nodes[j]), nodes[i], nodes[j]))

    sorted_rectangles = sorted(rectangles, key=lambda x: x[0], reverse=True)
    check_first_valid(sorted_rectangles)

if __name__ == "__main__":
    main()