
dial = 50
count_zero = 0

def parse_ins(ins: str):
    global dial, count_zero
    rotation = int(ins[1:])
    if(ins[0] == "L"):
        dial = (dial - rotation) % 100
    if(ins[0] == "R"):
        dial = (dial + rotation) % 100
    if not dial:
        count_zero += 1
    print(f"Rotated {ins[:-1]} - Dial {dial} - Zero Count {count_zero}")


def main():
    INPUT_FILE = "test.txt" 
    with open(INPUT_FILE, "r") as file:
        instructions = file.readlines()
        for ins in instructions:
            parse_ins(ins[:-1])
    print(count_zero)
    

if __name__ == "__main__":
    main()