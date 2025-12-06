INPUT="input.txt"
TOTAL=0

def process():
    pass

def main():
    with open(INPUT, "r") as file:
        lines = file.readlines()
        for line in lines:
            process(line[:-1])
    print(f"Answer: {TOTAL}")


if __name__ == "__main__":
    main()