file_path = 'email-Eu-core.txt'

def calculate_degrees(file_path):
    in_degrees = {}
    out_degrees = {}
    degrees = {}

    with open(file_path, 'r') as file:
        for line in file:
            sender, receiver = map(int, line.strip().split())
            out_degrees[sender] = out_degrees.get(sender, 0) + 1
            in_degrees[receiver] = in_degrees.get(receiver, 0) + 1

    for node in in_degrees:
        degrees[node] = in_degrees[node] + out_degrees.get(node, 0)

    return in_degrees, out_degrees, degrees

in_degrees, out_degrees, degrees = calculate_degrees(file_path)

for node in list(in_degrees.keys())[:5]:
    print('Node:', node)
    print('In_degree:', in_degrees.get(node, 0))
    print('Out_degree:', out_degrees.get(node, 0))
    print('Degree:', degrees.get(node, 0))
    print()

