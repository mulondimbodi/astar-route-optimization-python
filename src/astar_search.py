import heapq


GRAPH = {
    "Disaneng": ["Mahikeng", "Madibogo"],
    "Mahikeng": ["Disaneng", "Mmabatho", "Slurry", "Bakerville", "Madibogo"],
    "Mmabatho": ["Mahikeng", "Slurry"],
    "Slurry": ["Mahikeng", "Mmabatho", "Zeerust", "Groot Marico", "Bakerville"],
    "Zeerust": ["Slurry", "Groot Marico"],
    "Groot Marico": ["Slurry", "Zeerust"],
    "Bakerville": ["Mahikeng", "Slurry", "Lichtenburg"],
    "Lichtenburg": ["Bakerville", "Coligny"],
    "Coligny": ["Lichtenburg", "Ottosdal"],
    "Ottosdal": ["Coligny", "Sannieshof"],
    "Sannieshof": ["Ottosdal", "Delareyville", "Madibogo"],
    "Delareyville": ["Sannieshof"],
    "Madibogo": ["Disaneng", "Mahikeng", "Sannieshof"]
}


WEIGHTS = {
    ("Disaneng", "Mahikeng"): 25,
    ("Disaneng", "Madibogo"): 35,
    ("Mahikeng", "Mmabatho"): 10,
    ("Mahikeng", "Slurry"): 20,
    ("Mahikeng", "Bakerville"): 35,
    ("Mahikeng", "Madibogo"): 30,
    ("Mmabatho", "Slurry"): 15,
    ("Slurry", "Zeerust"): 35,
    ("Slurry", "Groot Marico"): 40,
    ("Slurry", "Bakerville"): 25,
    ("Zeerust", "Groot Marico"): 20,
    ("Bakerville", "Lichtenburg"): 20,
    ("Lichtenburg", "Coligny"): 30,
    ("Coligny", "Ottosdal"): 35,
    ("Ottosdal", "Sannieshof"): 25,
    ("Sannieshof", "Delareyville"): 30,
    ("Madibogo", "Sannieshof"): 35
}


HEURISTIC = {
    "Disaneng": 70,
    "Mahikeng": 50,
    "Mmabatho": 55,
    "Slurry": 45,
    "Zeerust": 65,
    "Groot Marico": 75,
    "Bakerville": 30,
    "Lichtenburg": 20,
    "Coligny": 0,
    "Ottosdal": 25,
    "Sannieshof": 40,
    "Delareyville": 55,
    "Madibogo": 60
}


def get_cost(a, b, weights=WEIGHTS):
    if (a, b) in weights:
        return weights[(a, b)]

    if (b, a) in weights:
        return weights[(b, a)]

    raise ValueError(f"No weight found between '{a}' and '{b}'")


def astar_search(graph, weights, heuristic, start, goal):
    open_set = []
    heapq.heappush(open_set, (heuristic[start], start))

    came_from = {}
    g_score = {node: float("inf") for node in graph}
    g_score[start] = 0

    f_score = {node: float("inf") for node in graph}
    f_score[start] = heuristic[start]

    visited_order = []

    while open_set:
        _, current = heapq.heappop(open_set)

        if current not in visited_order:
            visited_order.append(current)

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path, visited_order, g_score[goal]

        for neighbor in graph[current]:
            cost = get_cost(current, neighbor, weights)
            tentative_g = g_score[current] + cost

            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic[neighbor]
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None, visited_order, float("inf")


def find_optimal_route(start="Disaneng", goal="Coligny"):
    return astar_search(GRAPH, WEIGHTS, HEURISTIC, start, goal)


def main():
    start = "Disaneng"
    goal = "Coligny"
    path, visited_order, total_cost = find_optimal_route(start, goal)

    print("A* Route Optimization")
    print(f"Start: {start}")
    print(f"Goal: {goal}")
    print("Visited Order:", visited_order)
    print("Optimal Path:", path)
    print("Total Cost:", total_cost)


if __name__ == "__main__":
    main()