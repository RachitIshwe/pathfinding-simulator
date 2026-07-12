import heapq

def A(world_data):
    # Pull needed items out of the passed dictionary
    WayPoints = world_data["WayPoints"]
    start = world_data["start"]
    target = world_data["target"]
    connections = world_data["connections"]
    distance_to_target = world_data["distance_to_target"]

    # Reset colors locally
    for w in WayPoints: 
        w.color = (255, 0, 0)

    cost = {start: 0}
    initial_hn = distance_to_target[start]
    queue = [(0 + initial_hn, start)]
    parent = {start: None}
    Visiting_Node = []

    while queue:
        current_f, current_node = heapq.heappop(queue)
        Visiting_Node.append(current_node)

        if current_node == target:
            break
        
        current_g = current_f - distance_to_target[current_node]
        if current_g > cost[current_node] + 0.1:
            continue

        for neighbor, weight in connections[current_node].items():
            new_gn = cost[current_node] + weight
            if new_gn < cost.get(neighbor, float('inf')):
                cost[neighbor] = new_gn
                parent[neighbor] = current_node
                new_f = new_gn + distance_to_target[neighbor]
                heapq.heappush(queue, (new_f, neighbor))
    
    for v in Visiting_Node:
        WayPoints[v - 1].color = (255, 165, 0)

    path = []
    Shortest_path_line = []
    total_cost = 0
    path_string = "No Path Found"

    if target in cost:
        current = target
        while current is not None:
            path.append(current)
            current = parent.get(current)
        path.reverse()
        total_cost = round(cost[target], 1)
        path_string = " -> ".join(map(str, path))
        
        for index in range(len(path) - 1):
            wp1 = WayPoints[path[index] - 1]
            wp2 = WayPoints[path[index + 1] - 1]
            Shortest_path_line.append(((wp1.x, wp1.y), (wp2.x, wp2.y)))

    # Return the calculations back to main
    return path, total_cost, Shortest_path_line, path_string