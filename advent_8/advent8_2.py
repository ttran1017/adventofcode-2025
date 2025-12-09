INPUT = "advent_8/input.txt"

import math

nodes = []
weights = []
groups = []

def process(line: str):
    global nodes
    nodes.append(line.split(","))

def calc_weights():
    global weights
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            weights.append((i, j, calc_distance(nodes[i], nodes[j])))
    weights = sorted(weights, key=lambda w: w[2])

def calc_distance(node1, node2):
    x_diff = abs(int(node1[0]) - int(node2[0]))
    y_diff = abs(int(node1[1]) - int(node2[1]))
    z_diff = abs(int(node1[2]) - int(node2[2]))
    return math.sqrt(x_diff * x_diff + y_diff * y_diff + z_diff * z_diff)

def connect_nodes():
    global weights
    for i in range(len(weights)):
        weight = weights[i]
        add_to_group(weight)
        if len(groups[0]) == 1000:
            print(f"FINAL CONNECTION {nodes[weight[0]]} and {nodes[weight[1]]}")
            print(f"ANSWER: {int(nodes[weight[0]][0]) * int(nodes[weight[1]][0])}")
            return

def add_to_group(weight):
    global groups

    join_index = []
    for i, group in enumerate(groups):
        if weight[0] in group and weight[1] in group:
            join_index.append(-1)
            break
        
        elif weight[0] in group:
            join_index.append(i)
            group.add(weight[0])
            group.add(weight[1])

        elif weight[1] in group:
            join_index.append(i)
            group.add(weight[0])
            group.add(weight[1])

    if not join_index:
        groups.append({weight[0], weight[1]})
        return
            
    if len(join_index) > 1:
        groups[join_index[0]].update(groups[join_index[1]])
        groups.pop(join_index[1])

def print_answer():
    global groups
    groups = sorted(groups, key=len, reverse=True)
    print(groups)

def main():
    with open(INPUT, "r") as file:
        lines = file.readlines()

        for line in lines:
            process(line.strip())
        
    calc_weights()
    connect_nodes()
    print_answer()



        

if __name__ == "__main__":
    main()