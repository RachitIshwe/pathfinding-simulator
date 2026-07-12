import pygame
import sys
import math
from core import Width, Height, font, generate_new_world, A, Dij, Robot

pygame.init()
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Path Finding: A* vs Dijkstra")
clock = pygame.time.Clock()

# --- INITIALIZE APP STATES ---
world = generate_new_world()
robot = Robot()

path = []
total_cost = 0
Shortest_path_line = []
path_string = "Press 'A' for A* Search | Press 'D' for Dijkstra | 'R' to reset"

def update_hud(label, cost_val, path_str):
    t_start = font.render(f"Start: {world['start']}   |   Target: {world['target']}", True, (255, 255, 255))
    t_cost = font.render(f"Total Cost: {cost_val} ({label})", True, (255, 255, 255))
    t_path = font.render(f"Shortest Path: {path_str}", True, (255, 255, 255))
    return t_start, t_cost, t_path

text_start_target, text_cost, text_path = update_hud("None", total_cost, path_string)

# --- MAIN LOOP ---
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Running = False
            
            if event.key == pygame.K_r:
                world = generate_new_world()
                path = []
                Shortest_path_line = []
                robot.current_path_index = 0
                robot.x, robot.y = 0, 0
                text_start_target, text_cost, text_path = update_hud("Reset", 0, "Cleared")

            if event.key == pygame.K_a:
                path, total_cost, Shortest_path_line, path_string = A(world)
                if path:
                    robot.current_path_index = 0
                    robot.x = world["WayPoints"][path[0] - 1].x
                    robot.y = world["WayPoints"][path[0] - 1].y
                text_start_target, text_cost, text_path = update_hud("A*", total_cost, path_string)

            if event.key == pygame.K_d:
                path, total_cost, Shortest_path_line, path_string = Dij(world)
                if path:
                    robot.current_path_index = 0
                    robot.x = world["WayPoints"][path[0] - 1].x
                    robot.y = world["WayPoints"][path[0] - 1].y
                text_start_target, text_cost, text_path = update_hud("Dijkstra", total_cost, path_string)
                
    # --- ROBOT ENGINE ---
    if path and robot.current_path_index < len(path) - 1:
        wp2_num = path[robot.current_path_index + 1]  
        w2 = world["WayPoints"][wp2_num - 1]
        
        r = math.hypot((w2.x - robot.x), (w2.y - robot.y))
        if r < robot.desired_speed:
            robot.x = w2.x
            robot.y = w2.y
            robot.current_path_index += 1
        else:
            robot.x += ((w2.x - robot.x) / r) * robot.desired_speed
            robot.y += ((w2.y - robot.y) / r) * robot.desired_speed
            
    # --- DRAWING ---
    screen.fill((20, 20, 20))
    
    for line in world["valid_lines"]:
        pygame.draw.line(screen, (0, 255, 0), line[0], line[1], 1)
        
    for shortest_line in Shortest_path_line:
        pygame.draw.line(screen, (255, 255, 255), shortest_line[0], shortest_line[1], 4)

    for o in world["Obstacles"]:
        pygame.draw.rect(screen, world["obstacle_color"], o)
        
    for w in world["WayPoints"]:
        if w.number == world["start"]:
            pygame.draw.circle(screen, (0, 100, 255), (w.x, w.y), w.radius + 3)
        elif w.number == world["target"]:
            pygame.draw.circle(screen, (0, 255, 100), (w.x, w.y), w.radius + 3)
        else:
            pygame.draw.circle(screen, w.color, (w.x, w.y), w.radius)
            
    screen.blit(text_start_target, (20, 20))
    screen.blit(text_cost, (20, 50))
    screen.blit(text_path, (20, 80))
    
    if robot.x > 0 and robot.y > 0:
        pygame.draw.circle(screen, robot.color, (int(robot.x), int(robot.y)), robot.radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()