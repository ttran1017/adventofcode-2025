INPUT="advent_5/input.txt"

total=0

fresh_ranges = []

def process_id(i: str):
    id = int(i)
    global fresh_ranges, total
    for r in fresh_ranges:      
        if id >= r[0] and id <= r[1]:
            total += 1
            print(f"id: {id} is fresh")
            break

def process_range(r: str):
    global fresh_set
    start, stop = r.split("-")
    fresh_ranges.append((int(start), int(stop)))

def main():
    with open(INPUT, "r") as file:
        lines = file.readlines()

        breakpoint = lines.index("\n")
        ranges = lines[:breakpoint]
        ids = lines[breakpoint + 1:]

        for r in ranges:
            process_range(r)

        for i in ids:
            process_id(i)

    print(f"Total fresh: {total}")



if __name__ == "__main__":
    main()