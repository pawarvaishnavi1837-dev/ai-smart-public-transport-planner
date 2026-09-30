from src.crowd_prediction import predict_crowd
from src.seat_prediction import predict_seat_status
from src.delay_prediction import predict_delay
from src.route_recommendation import recommend_route


# Sample transport data
passenger_count = 32
total_seats = 40

current_delay = 5
traffic_level = "High"
historical_delay = 8

routes = [
    {"name": "Route A", "travel_time": 35},
    {"name": "Route B", "travel_time": 25},
    {"name": "Route C", "travel_time": 40}
]


# AI predictions
crowd = predict_crowd(passenger_count)

seats, seat_status = predict_seat_status(
    passenger_count,
    total_seats
)

delay = predict_delay(
    current_delay,
    traffic_level,
    historical_delay
)

recommended_route = recommend_route(routes)


# Display results
print("===================================")
print(" SMART PUBLIC TRANSPORT PLANNER")
print("===================================")

print("Passenger Count:", passenger_count)
print("Crowd Level:", crowd)

print("Estimated Seats Available:", seats)
print("Seat Status:", seat_status)

print("Predicted Delay:", delay, "minutes")

print("Recommended Route:",
      recommended_route["name"])

print("Estimated Travel Time:",
      recommended_route["travel_time"],
      "minutes")

print("===================================")
