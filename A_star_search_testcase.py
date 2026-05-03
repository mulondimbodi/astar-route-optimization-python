import time
from A_star_search import path, visited_order, total_cost

def simulate_path(path):
    print("\nTruck traveling...\n")

    for node in path:
        print(f"Truck is now at: {node}")
        time.sleep(1)

    print("\nDestination reached!")
    print("\nVisited Order:", visited_order)
    print("Optimal Path:", path)
    print("Total Cost:", total_cost)

simulate_path(path)