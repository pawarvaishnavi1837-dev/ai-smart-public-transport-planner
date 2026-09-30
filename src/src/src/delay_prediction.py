def predict_delay(current_delay, traffic_level, historical_delay):
    """
    Estimate bus delay using current traffic and historical delay.
    """

    traffic_factor = {
        "Low": 0,
        "Medium": 5,
        "High": 10
    }

    predicted_delay = (
        current_delay
        + traffic_factor.get(traffic_level, 0)
        + historical_delay
    ) / 2

    return round(predicted_delay, 1)


if __name__ == "__main__":
    current_delay = 5
    traffic_level = "High"
    historical_delay = 8

    delay = predict_delay(
        current_delay,
        traffic_level,
        historical_delay
    )

    print("Predicted Delay:", delay, "minutes")
