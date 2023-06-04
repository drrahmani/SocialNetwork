file_path = 'email-Eu-core.txt'

def calculate_average_degrees(file_path):
    num_nodes = 0
    total_degree = 0
    total_in_degree = 0
    total_out_degree = 0

    with open(file_path, 'r') as file:
        for line in file:
            sender, receiver = map(int, line.strip().split())
            total_out_degree += 1
            total_in_degree += 1

            num_nodes = max(num_nodes, sender, receiver)

    total_degree = total_out_degree + total_in_degree
    num_nodes += 1

    average_degree = total_degree / num_nodes
    average_in_degree = total_in_degree / num_nodes
    average_out_degree = total_out_degree / num_nodes

    return average_degree, average_in_degree, average_out_degree


# Example usage:
average_degree, average_in_degree, average_out_degree = calculate_average_degrees(file_path)

print("Average Degree:", average_degree)
print("Average In-Degree:", average_in_degree)
print("Average Out-Degree:", average_out_degree)
