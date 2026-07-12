import random
import pygame
import math
from .settings import Width, Height

class Waypoint:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number = number
        self.color = (255, 0, 0)
        self.radius = 8

def generate_new_world():
    number_of_waypoints = 50
    waypoint_buffer = 60
    WayPoints = []

    while len(WayPoints) < number_of_waypoints:
        random_x = random.randint(100, Width - 100)
        random_y = random.randint(100, Height - 100)
        
        is_valid = True
        for existing_wp in WayPoints:
            distance = math.hypot(random_x - existing_wp.x, random_y - existing_wp.y)
            if distance < waypoint_buffer:
                is_valid = False
                break
                
        if is_valid:
            WayPoints.append(Waypoint(random_x, random_y, len(WayPoints) + 1))

    # Obstacles Generation
    number_of_obstacles = 70
    Obstacles = []
    width, height = 50, 50
    buffer = 20

    while len(Obstacles) < number_of_obstacles:
        random_x = random.randint(100, Width - 100)
        random_y = random.randint(100, Height - 100)
        new_obstacle = pygame.Rect(random_x, random_y, width, height)
        
        is_valid = True
        for existing_obs in Obstacles:
            if new_obstacle.colliderect(existing_obs):
                is_valid = False
                break
                
        if is_valid:
            for wp in WayPoints:
                wp_rect = pygame.Rect(
                    wp.x - wp.radius - buffer,
                    wp.y - wp.radius - buffer,
                    (wp.radius + buffer) * 2,
                    (wp.radius + buffer) * 2
                )
                if new_obstacle.colliderect(wp_rect):
                    is_valid = False
                    break
                    
        if is_valid:
            Obstacles.append(new_obstacle)

    start = random.randint(1, 4)
    target = random.randint(number_of_waypoints - 3, number_of_waypoints)
    connections = {i + 1: {} for i in range(number_of_waypoints)}
    valid_lines = []

    for i in range(len(WayPoints)):
        for j in range(i + 1, len(WayPoints)):
            w1 = WayPoints[i]
            w2 = WayPoints[j]
            
            collision_detected = False
            for obstacle in Obstacles:
                if obstacle.clipline((w1.x, w1.y), (w2.x, w2.y)):
                    collision_detected = True
                    break
            
            if not collision_detected:
                valid_lines.append(((w1.x, w1.y), (w2.x, w2.y)))
                distance = round(math.hypot((w2.x - w1.x), (w2.y - w1.y)), 1)
                connections[i + 1][j + 1] = distance
                connections[j + 1][i + 1] = distance

    # Heuristics
    distance_to_target = {}
    target_wayp = WayPoints[target - 1]
    for w in WayPoints:
        dis = math.hypot((target_wayp.x - w.x), (target_wayp.y - w.y))
        distance_to_target[w.number] = round(dis, 1)

    # Return everything as a dictionary paket
    return {
        "WayPoints": WayPoints,
        "Obstacles": Obstacles,
        "valid_lines": valid_lines,
        "connections": connections,
        "start": start,
        "target": target,
        "distance_to_target": distance_to_target,
        "obstacle_color": (25, 255, 255)
    }