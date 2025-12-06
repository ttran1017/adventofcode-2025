
dial = 50
count_zero = 0

NUM_TICKS = 100
INPUT_FILE = "input.txt" 

def parse_ins(ins: str):
    global dial, count_zero
    rotation = int(ins[1:])

    count_zero += rotation // NUM_TICKS
    rotation %= NUM_TICKS

    if(ins[0] == "L"):
        if(dial != 0 and dial - rotation <= 0):
            count_zero += 1
        dial = (dial - rotation) % NUM_TICKS
    if(ins[0] == "R"):
        if(rotation + dial >= NUM_TICKS):
            count_zero += 1
        dial = (dial + rotation) % NUM_TICKS

    print(f"Rotated {ins} - Dial {dial} - Zero Count {count_zero}")


def main():
    with open(INPUT_FILE, "r") as file:
        instructions = file.readlines()
        for ins in instructions:
            parse_ins(ins[:-1])
    print(count_zero)
    

if __name__ == "__main__":
    main()
