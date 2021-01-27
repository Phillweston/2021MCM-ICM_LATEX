#!/usr/bin/python3
import random
import matplotlib.pyplot as plt
import turtle as t
# Using dictionary to store adjacent_matrix
graph = {'A': [(7, 'A', 'B'), (5, 'A', 'D')],
         'B': [(7, 'B', 'A'), (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E')],
         'C': [(8, 'C', 'B'), (5, 'C', 'E')],
         'D': [(5, 'D', 'A'), (9, 'D', 'B'), (15, 'D', 'E'), (6, 'D', 'F')],
         'E': [(7, 'E', 'B'), (5, 'E', 'C'), (15, 'E', 'D'), (8, 'E', 'F'), (9, 'E', 'G')],
         'F': [(6, 'F', 'D'), (8, 'F', 'E'), (11, 'F', 'G')],
         'G': [(9, 'G', 'E'), (11, 'G', 'F')]
         }

# Plot the graph from the dict above
plt_width = 650
plt_height = 350
pen_size = 1
graph_plt = [[0 for col in range(2)] for row in range(len(graph))]
for row in range(len(graph)):
    for col in range(2):
        if col == 0:
            graph_plt[row][col] = random.randint(-int(plt_width/2 - 10), int(plt_width/2 - 10))
        else:
            graph_plt[row][col] = random.randint(-int(plt_height/2 - 10), int(plt_height/2 - 10))
t.setup(plt_width, plt_height)
t.penup()
t.pensize(1)
t.pencolor("red")
for i in range(len(graph)):
    t.goto(graph_plt[i][0], graph_plt[i][1])
    t.write(chr(i+65), font=("Arial", 16, "normal"))
    t.pendown()
    t.goto(graph_plt[i][0], graph_plt[i][1])
    t.penup()

def graph_to_adjacent_matrix(graph):
    vertex_num = len(graph)
    # Define the corresponding number to the letter
    dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
    # Structure a vertex_num * vertex_num adjacent_matrix
    adjacent_matrix = [[0 if row == col else float('inf') for col in range(vertex_num)] for row in range(vertex_num)]
    # Return all the keys in the dictionaries
    vertices = graph.keys()
    # Traverse the vertices
    for vertex in vertices:
        # The traversal of the edges corresponding to each vertices
        for edge in graph[vertex]:
            # The following three variables correspond in turn to the variables in the dictionary key value pair
            w, u, v = edge
            # Transforms the graph into an adjacent matrix, where each variable holds the weight of the edge
            adjacent_matrix[dict.get(u)][dict.get(v)] = w
    return adjacent_matrix


# After the adjacent matrix is generated, it is passed into the floyd function
# The adjacent matrix constructed is a square matrix
def floyd(adjacent_matrix):
    vertex_num = len(adjacent_matrix)
    a = [[adjacent_matrix[row][col] for col in range(vertex_num)] for row in range(vertex_num)]
    # The n_vertex matrix in the n_vertex[i][j]
    # represents the successor vertex of vi in the shortest circuit between vi and vj,
    # depending on the matrix, you can get the vertex points that pass through the middle of any shortest circuit
    n_vertex = [[-1 if adjacent_matrix[row][col] == float('inf') else col for col in range(vertex_num)] for row in
                range(vertex_num)]
    # print(adjacent_matrix)
    # Selected point
    for k in range(vertex_num):
        # Start point
        for i in range(vertex_num):
            # End point
            for j in range(vertex_num):
                # If three vertices, the value of the edges of two of them is less than the third side,
                # the third side weight is the same as the two sides
                if a[i][j] > a[i][k] + a[k][j]:
                    a[i][j] = a[i][k] + a[k][j]
                    n_vertex[i][j] = n_vertex[i][k]
    return n_vertex, a


adjacent_matrix = graph_to_adjacent_matrix(graph)
n_vertex, a = floyd(adjacent_matrix)
# Print the original adjacent matrix
for i in range(len(adjacent_matrix)):
    for j in range(len(adjacent_matrix[0])):
        print(adjacent_matrix[i][j], end="\t")
    print()  # Print a line and line it back
# Print the vertices passed next
print()
for i in range(len(n_vertex)):
    for j in range(len(n_vertex[0])):
        print(n_vertex[i][j], end="\t")
    print()  # Print a line and line it back
# Print the shortest distance between them
print()
for i in range(len(a)):
    for j in range(len(a[0])):
        print(a[i][j], end="\t")
    print()  # Print a line and line it back
# Initialize the dict_passed array to zero
vertex_passed = [0 for i in range(len(a))]
# Initialize the visited_matrix
visited_matrix = [[0 for col in range(len(graph))] for row in range(len(graph))]
times = int(input("Input cycle times, input 0 to manually input start_point and end_point"))
if times == 0:
    start_point = ord(input("Input Start Point, for example, A, B, C, ...")) - 65
    end_point = ord(input("Input End Point, for example, A, B, C, ...")) - 65
    row_num = start_point
    # Add start_point and end_point to the dict_passed array
    vertex_passed[start_point] += 1
    while row_num != end_point:
        vertex_passed[n_vertex[row_num][end_point]] += 1
        visited_matrix[row_num][n_vertex[row_num][end_point]] += 1
        t.goto(graph_plt[row_num][0], graph_plt[row_num][1])
        t.pendown()
        row_num = n_vertex[row_num][end_point]
        t.goto(graph_plt[row_num][0], graph_plt[row_num][1])
        t.penup()
else:
    for i in range(times):
        start_point = random.randint(0, 6)
        end_point = random.randint(0, 6)
        print("Start point is: ", chr(start_point+65), "End point is: ", chr(end_point+65))
        row_num = start_point
        # Add start_point and end_point to the dict_passed array
        vertex_passed[start_point] += 1
        while row_num != end_point:
            t.pensize(pen_size)
            vertex_passed[n_vertex[row_num][end_point]] += 1
            visited_matrix[row_num][n_vertex[row_num][end_point]] += 1
            t.goto(graph_plt[row_num][0], graph_plt[row_num][1])
            t.pendown()
            row_num = n_vertex[row_num][end_point]
            t.goto(graph_plt[row_num][0], graph_plt[row_num][1])
            t.penup()
            pen_size += 1
x = []
y = []
# Print the number of the vertex passed
for i in range(len(a)):
    print(chr(i+65), ": ", vertex_passed[i])
    x.append(chr(i+65))
    y.append(vertex_passed[i])
# Show the vertex visited graph
plt.plot(x, y, color="r", linestyle="-", linewidth=1)
plt.show()
for i in range(len(graph)):
    for j in range(len(graph)):
        if adjacent_matrix[i][j] == float('inf'):
            visited_matrix[i][j] = float('inf')
        print(visited_matrix[i][j], end="\t")
    print()  # Print a line and line it back
t.done()
