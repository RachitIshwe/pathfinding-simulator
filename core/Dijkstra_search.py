import heapq

def Dij(world_data):
    # Pull needed items out of the passed dictionary
    WayPoints = world_data["WayPoints"]
    start = world_data["start"]
    target = world_data["target"]
    connections = world_data["connections"]
    distance_to_target = world_data["distance_to_target"]
    cost = {}

    # Reset colors locally
    for w in WayPoints: 
        w.color = (255, 0, 0)

    cost[start] = 0
    queue = [(0, start)]
    parent = {start: None}
    Visiting_Node = []

    while queue:
        current_cost, current_node = heapq.heappop(queue)
        Visiting_Node.append(current_node)

        if current_node == target:
            break
        if current_cost > cost[current_node]:
            continue

        for neighbor, weight in connections[current_node].items():
            new_cost = cost[current_node] + weight
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                parent[neighbor] = current_node
                heapq.heappush(queue, (new_cost, neighbor))
        
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
            wp1_num = path[index]      
            wp2_num = path[index + 1]  
            Shortest_path_line.append(((WayPoints[wp1_num - 1].x, WayPoints[wp1_num - 1].y), (WayPoints[wp2_num - 1].x, WayPoints[wp2_num - 1].y)))
            
        current_path_index = 0
        robot_x = WayPoints[path[0] - 1].x
        robot_y = WayPoints[path[0] - 1].y
    else:
        path_string = "No Path Found"
        total_cost = 0

    # Return the calculations back to main
    return path, total_cost, Shortest_path_line, path_string