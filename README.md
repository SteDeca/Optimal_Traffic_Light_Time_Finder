# Traffic Light Optimization Simulation

This project provides a Python simulation to optimize traffic light timings for a junction with three roads. It uses stochastic modeling (Poisson distribution) to simulate car arrivals and calculates the optimal green light duration to minimize the average waiting time for all vehicles.
It was made after a job interview, since I was asked how to find the optimal traffic light cycle length and at the moment I didn't know how to answer, so I writed a script in python to find the solution to this problem.

## 🚦 Overview

Managing traffic flow efficiently is a common urban challenge. This script simulates a simple cycle where three roads get green lights sequentially. By varying the duration of the green light for the primary road, the simulation identifies the "sweet spot" that minimizes the overall average wait time for all commuters.

## ✨ Features

- **Stochastic Car Arrival:** Uses `numpy.random.poisson` to simulate realistic car arrival patterns and batching.
- **Multi-Road Simulation:** Models three different roads with varying traffic intensities:
  - **Road 1:** High traffic intensity.
  - **Road 2:** Medium traffic intensity.
  - **Road 3:** Low traffic intensity.
- **Optimization:** Automatically identifies the optimal green light duration based on the simulation results.
- **Data Visualization:** Generates a clear Matplotlib plot showing the relationship between green light timing and waiting times, including the highlighted optimal point.

## 🛠️ Prerequisites

To run this script, you need Python installed along with the following libraries:

```bash
pip install numpy matplotlib
```

## 🚀 Usage

Simply run the script using Python:

```bash
python Traffic_Light.py
```

The script will:
1. Simulate car waiting times across a range of green light durations.
2. Calculate the average wait time for each road and the total system average.
3. Display a plot showing the results and the optimal timing point.

## 📊 How it Works

1. **Car Generation:** The `Car.Wait_time_cars` method generates arrival times based on traffic intensity parameters (Lambda).
2. **Cycle Logic:** The simulation assumes a sequential green light cycle (Road 1 → Road 2 → Road 3).
3. **Wait Time Calculation:** It accounts for:
   - Initial wait time (time arrived before green).
   - Cycle delays (waiting for other roads to finish).
   - Exit time (the time it takes for cars ahead in the queue to clear the junction).
4. **Visualization:** The resulting plot helps visualize how increasing or decreasing the green light duration impacts the efficiency of the junction.

## 📈 Example Output

The script generates a plot where:
- **X-axis:** Green light duration for the first road (seconds).
- **Y-axis:** Average waiting time (seconds).
- An **Annotation** marks the optimal point where the general average waiting time is at its minimum.

---
*Developed as a useful project for traffic analysis and optimization.*
