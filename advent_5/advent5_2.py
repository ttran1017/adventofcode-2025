INPUT="advent_5/input.txt"

total=0
fresh_ranges = []

def count_ranges():
    global total
    sorted_fresh_ranges = sorted(fresh_ranges, key=lambda r: r[0])
    low, high = sorted_fresh_ranges[0]
    for r in sorted_fresh_ranges[1:]:
        compare_low, compare_high = r
        if high >= compare_low:
            high = max(high, compare_high)
        else:
            total += high - low + 1
            low = compare_low
            high = compare_high
    total += high - low + 1

def process_range(r: str):
    global fresh_set
    start, stop = r.split("-")
    fresh_ranges.append((int(start), int(stop)))

def main():
    with open(INPUT, "r") as file:
        lines = file.readlines()

        breakpoint = lines.index("\n")
        ranges = lines[:breakpoint]

        for r in ranges:
            process_range(r)

        count_ranges()

    print(f"Total items: {total}")



if __name__ == "__main__":
    main()