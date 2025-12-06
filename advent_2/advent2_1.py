INPUT = "input.txt"

total = 0

def check_invalid(num: int):
    global total
    str_num = str(num)

    midpoint = len(str_num) // 2
    if str_num[midpoint:] == str_num[:midpoint]:
        total += num
        print(f"Found: {num}")

def process(r: str):
    start, stop = r.split("-")
    start = int(start)
    stop = int(stop)
    for num in range(start, stop + 1):
        check_invalid(num)


def main():
    with open(INPUT, "r") as file:
        instructions = file.readline()
        rgs = instructions.split(",")
        for r in rgs:
            process(r)
    print(f"Answer: {total}")


if __name__ == "__main__":
    main()