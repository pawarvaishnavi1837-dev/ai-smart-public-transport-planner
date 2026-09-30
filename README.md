# AI-Powered Smart Public Transport Planner

An AI-powered public transport planning system designed to improve commuter experience through intelligent crowd prediction, seat availability prediction, delay prediction, and alternative route recommendation.

## Problem

Public transport users often face overcrowding, uncertain seat availability, unexpected delays, and difficulty choosing alternative routes.

## Solution

The Smart Public Transport Planner uses AI and predictive analytics to provide:

- AI-based crowd level prediction
- Seat availability prediction
- Smart delay prediction
- Alternative route recommendation

## Key Features

### 1. Crowd Prediction
Uses passenger count data to classify crowd levels as Low, Medium, or High.

### 2. Seat Availability
Estimates available seats and displays:
- Seats Available
- Limited Seats
- Standing Only

### 3. Delay Prediction
Combines current delay, traffic conditions, and historical delay data to estimate expected delay.

### 4. Route Recommendation
Compares available routes and recommends a route based on estimated travel time.

## Technology

- Python
- Machine Learning concepts
- Predictive Analytics
- Computer Vision integration concept
- Edge AI concept
- NVIDIA Jetson / Snapdragon-compatible edge deployment concept

## Project Structure

```text
ai-smart-public-transport-planner/
│
├── main.py
├── README.md
├── requirements.txt
│
└── src/
    ├── crowd_prediction.py
    ├── seat_prediction.py
    ├── delay_prediction.py
    └── route_recommendation.py
```
##Future Scope
The system can be extended with real-time camera-based passenger counting, GPS data, traffic APIs, trained machine-learning models, and optimized edge-AI deployment.
Goal
To provide commuters with intelligent, real-time travel information and help them make better public transport decisions. 
