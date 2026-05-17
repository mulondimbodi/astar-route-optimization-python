import time

from astar_search import find_optimal_route


def simulate_path(path):
    print("\nTruck traveling...\n")

    for node in path:
        print(f"Truck is now at: {node}")
        time.sleep(1)

    print("\nDestination reached!")


def main():
    start = "Disaneng"
    goal = "Coligny"
    path, visited_order, total_cost = find_optimal_route(start, goal)

    simulate_path(path)

    print("\nRoute Optimization Summary")
    print("Start:", start)
    print("Goal:", goal)
    print("Visited Order:", visited_order)
    print("Optimal Path:", path)
    print("Total Cost:", total_cost)


if __name__ == "__main__":
    main()