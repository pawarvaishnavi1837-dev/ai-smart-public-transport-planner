def predict_seat_status(passenger_count, total_seats=40):
    """
    Estimate seat availability from passenger count.
    """

    available_seats = max(total_seats - passenger_count, 0)

    if available_seats >= 10:
        status = "Seats Available"
    elif available_seats > 0:
        status = "Limited Seats"
    else:
        status = "Standing Only"

    return available_seats, status


if __name__ == "__main__":
    passengers = 32

    seats, status = predict_seat_status(passengers)

    print("Passenger Count:", passengers)
    print("Estimated Seats Available:", seats)
    print("Status:", status)
