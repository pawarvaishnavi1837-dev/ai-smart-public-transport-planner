def recommend_route(routes):
    """
    Recommend a route based on predicted travel time.
    """

    best_route = min(routes, key=lambda route: route["travel_time"])

    return best_route


if __name__ == "__main__":
    routes = [
        {"name": "Route A", "travel_time": 35},
        {"name": "Route B", "travel_time": 25},
        {"name": "Route C", "travel_time": 40}
    ]

    recommended = recommend_route(routes)

    print("Recommended Route:", recommended["name"])
    print("Estimated Travel Time:", recommended["travel_time"], "minutes")
