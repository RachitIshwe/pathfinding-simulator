# Path Finding Simulation (A* vs Dijkstra)

This is a Pygame application that shows how A* and Dijkstra's algorithms find the shortest path through a randomly generated map. It generates a map of waypoints and obstacles, finds a path when you press a key, and animates a robot moving along that path.

## How it Works

1. **The Map:** The program automatically places 50 waypoints and 70 obstacles on the screen. Waypoints are connected by green lines as long as an obstacle isn't blocking the path.
2. **The Search:** It picks a random start and target node. You can trigger either A* or Dijkstra to calculate the quickest route.
3. **The Robot:** Once a path is found, a purple circle moves step-by-step from the start node to the destination.

## File Structure

- `main.py`: Runs the window, handles keyboard controls, and draws everything to the screen.
- `core/settings.py`: Sets the screen size and font configurations.
- `core/world_generation.py`: Spawns the waypoints and blocks, and checks which paths are unblocked.
- `core/AStar_Search.py`: Calculates the path using the A* algorithm.
- `core/Dijkstra_search.py`: Calculates the path using Dijkstra's algorithm.
- `core/robot_properties.py`: Holds the size, speed, and position settings for the moving robot.

## How to Run It

### Installation
Make sure you have Python installed, then clone this repository and install Pygame:

```bash
git clone [https://github.com/RachitIshwe/shortest-path.git](https://github.com/RachitIshwe/shortest-path.git)
cd shortest-path
pip install pygame
