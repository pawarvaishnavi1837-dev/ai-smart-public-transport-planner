def predict_crowd(passenger_count):
    """
    Predict crowd level based on passenger count.
    """

    if passenger_count < 15:
        return "Low"
    elif passenger_count < 30:
        return "Medium"
    else:
        return "High"


if __name__ == "__main__":
    passengers = 25

    crowd = predict_crowd(passengers)

    print("Passenger Count:", passengers)
    print("Predicted Crowd Level:", crowd)
