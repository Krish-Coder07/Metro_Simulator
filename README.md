# Delhi Metro Simulator

A comprehensive command-line based Delhi Metro Simulator designed to provide efficient route planning, metro scheduling, fare estimation, and distance calculation across multiple Delhi Metro lines.

The simulator models real-world metro operations by incorporating interchange handling, distance-based fare computation, and time-aware metro scheduling.

---

# Overview

The project allows users to navigate the Delhi Metro network through features such as:

- Real-time metro schedule simulation
- Intelligent journey planning
- Shortest route computation
- Distance-based fare estimation
- Interchange handling across metro lines
- Travel distance calculation
- Support for multiple Delhi Metro corridors

The simulator currently supports the following metro lines:

- Blue Line
- Magenta Line
- Red Line
- Violet Line
- Grey Line

---

# Features

## 1. Subsequent Metro Finder

Displays upcoming metro arrivals at a selected station based on the current time.

### Functionalities
- Shows next 4–5 metro timings
- Identifies metro destination/terminal station
- Simulates realistic metro frequency
- Handles peak-hour and non-peak-hour scheduling

### Metro Frequency Logic

#### Peak Hours
- 8:00 AM – 10:00 AM
- 5:00 PM – 7:00 PM

Metro frequency: **Every 4 minutes**

#### Non-Peak Hours
Metro frequency: **Every 8 minutes**

---

## 2. Journey Planner

Computes the optimal route between source and destination stations across all supported metro lines.

### Functionalities
- Shortest path route calculation
- Automatic interchange handling
- Travel distance computation
- Estimated travel time
- Fare calculation
- Route breakdown with interchanges

### Journey Planning Logic
- All valid paths between stations are explored.
- If a station belongs to multiple lines, interchange routes are considered automatically.
- The algorithm computes cumulative distance step-by-step.
- The route with minimum travel distance is selected as the optimal route.

---

## 3. Distance Calculator

Calculates the total travel distance between source and destination stations.

### Working
1. Distance between adjacent stations is loaded from the dataset.
2. The program traverses all possible valid routes.
3. Distances are accumulated for each route.
4. Interchanges are handled seamlessly.
5. The minimum-distance valid path is selected.

### Output
- Total distance travelled
- Selected route
- Interchange stations (if any)

---

## 4. Fare Calculator

The simulator automatically computes metro fare using distance-based fare slabs inspired by the DMRC fare structure.

| Distance Travelled | Fare |
|-------------------|------|
| Up to 2 km | ₹11 |
| 2 – 5 km | ₹21 |
| 5 – 12 km | ₹32 |
| 12 – 21 km | ₹43 |
| Above 32 km | ₹54 |

### Fare Calculation Process
1. Total journey distance is calculated.
2. Distance is mapped to the corresponding fare slab.
3. Final fare is displayed along with journey details.

---

# Supported Metro Lines

| Metro Line | Terminal Stations |
|------------|------------------|
| Blue Line | Dwarka Sector 21 ↔ Noida Electronic City |
| Blue Line Branch | Yamuna Bank ↔ Vaishali |
| Magenta Line | Janakpuri West ↔ Botanical Garden |
| Red Line | Shaheed Sthal (New Bus Adda) ↔ Rithala |
| Violet Line | Kashmere Gate ↔ Raja Nahar Singh (Ballabgarh) |
| Grey Line | Dwarka ↔ Dhansa Bus Stand |

---

# Data Collection Methodology

The dataset used in the simulator was compiled using multiple verified sources.

## Data Sources
- Official DMRC website
- Google Maps
- MyMetro.in

## Collected Information
- Station names
- Distance between consecutive stations
- Travel time between stations
- Interchange details

## Notes
- Distance values are approximate and rounded for simplicity.
- Some station naming conventions vary across sources; therefore, users are advised to refer to the provided data file for exact spellings.

---

# Assumptions

The following assumptions were considered during implementation:

1. Metro services begin operating from terminal stations at **6:00 AM**.
2. After approximately **11:00 PM**, metro services are assumed unavailable.
3. Interchange duration is fixed at **5 minutes** for all interchange stations.

### Terminal Stations Considered
- Grey Line: Dwarka ↔ Dhansa Bus Stand
- Red Line: Shaheed Sthal (New Bus Adda) ↔ Rithala
- Violet Line: Kashmere Gate ↔ Raja Nahar Singh (Ballabgarh)

---

# User Guide

## Journey Planner

When the user selects the Journey Planner option, the program requests:
- Source station
- Destination station
- Current time

### Output
- Optimal route
- Interchange stations
- Estimated travel details
- Total distance travelled
- Calculated fare

---

## Subsequent Metro Finder

When the user selects the Subsequent Metro option:

1. The user enters a station name and current time.
2. The program calculates upcoming metro timings.
3. The next 4–5 available metro departures are displayed.

---

# References

- [Delhi Metro Rail Corporation (DMRC)](https://delhimetrorail.com/)
- Google Maps
- MyMetro.in
