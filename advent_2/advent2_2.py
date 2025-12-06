INPUT = "input.txt"

total = 0

def check_invalid(num: int):
    global total
    str_num = str(num)
    str_len = len(str_num)

    for chunk_len in range(1, str_len):
        chunks = []
        for chunk_start in range(0, str_len, chunk_len):
            if chunk_start + chunk_len > str_len:
                chunks.append(str_num[chunk_start])
            else:
                chunks.append(str_num[chunk_start:chunk_start+chunk_len])
        if len(set(chunks)) == 1:
            total += num
            print(f"Found: {num}")
            return

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