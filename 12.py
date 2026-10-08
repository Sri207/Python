n = int(input("Enter number of cities: "))

print("Enter adjacency matrix:")
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

source = int(input("Enter source city: "))
destination = int(input("Enter destination city: "))

INF = 9999

distance = [INF] * n
visited = [False] * n
previous = [-1] * n

distance[source] = 0

for _ in range(n):
    min_distance = INF
    u = -1

    for i in range(n):
        if not visited[i] and distance[i] < min_distance:
            min_distance = distance[i]
            u = i

    if u == -1:
        break

    visited[u] = True

    for v in range(n):
        if graph[u][v] != 0 and not visited[v]:
            new_distance = distance[u] + graph[u][v]

            if new_distance < distance[v]:
                distance[v] = new_distance
                previous[v] = u

path = []
current = destination

while current != -1:
    path.append(current)
    current = previous[current]

path.reverse()

if distance[destination] == INF:
    print("No path exists.")
else:
    print("Shortest path:", " -> ".join(map(str, path)))
    print("Shortest distance:", distance[destination])