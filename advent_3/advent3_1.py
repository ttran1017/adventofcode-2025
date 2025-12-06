INPUT="input.txt"

TOTAL = 0

def process(line: str):
    global TOTAL
    l = 0
    r = len(line) - 1

    max_l = l
    max_r = r
    while(l < r-1):
       l += 1
       l_value = int(line[l])
       if(l_value > int(line[max_l])):
           max_l = l
           
       if(int(line[max_l] == 9)):
           break

    while(r > max_l+1):
        r -= 1
        r_value = int(line[r])
        if(r_value > int(line[max_r])):
            max_r = r
    
    value = int(f"{line[max_l]}{line[max_r]}")
    print(f"Got {value} from {line}")
    TOTAL += value


def main():
    with open(INPUT, "r") as file:
        lines = file.readlines()
        for line in lines:
            process(line[:-1])
    print(f"Answer: {TOTAL}")


if __name__ == "__main__":
    main()