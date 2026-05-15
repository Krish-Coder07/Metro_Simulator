Additional Features Implemented

The project was extended with several additional functionalities to improve the overall journey planning experience and provide more realistic metro travel information.

The following enhancements were added:

Fare calculation integrated with the journey planner
Support for additional metro lines:
Red Line
Violet Line
Grey Line
Total distance calculation between stations
Fare Calculation System

The metro fare is calculated using distance-based fare slabs inspired by the official DMRC fare structure.

Distance Travelled	Fare
Up to 2 km	₹11
2 – 5 km	₹21
5 – 12 km	₹32
12 – 21 km	₹43
21 – 32 km	₹54

The fare is automatically computed after determining the shortest valid route between the selected stations.

Data Collection

The dataset used in the project was compiled from multiple verified sources.

Station names were collected from the official DMRC website.
Travel time between adjacent stations was obtained from DMRC route information.
Distance between stations was collected using:
Google Maps
MyMetro.in

Distance values are approximate and rounded for simplicity.

Some station naming conventions differed across sources; therefore, users are advised to refer to the provided station data file for exact station names and spellings.

Assumptions

The following assumptions were considered during implementation:

Grey Line
Terminal stations:
Dwarka
Dhansa Bus Stand
Red Line
Terminal stations:
Shaheed Sthal (New Bus Adda)
Rithala
Violet Line
Terminal stations:
Kashmere Gate
Raja Nahar Singh (Ballabgarh)
Metro Timings
Metro services are assumed to begin operating from terminal stations at 6:00 AM.
If the user enters a time beyond operational hours (approximately after 11:00 PM), the program may indicate that metro services are unavailable.
Working of the Program

The Journey Planner computes the optimal path between the source and destination stations while handling line interchanges and route selection automatically.

The system provides:

Route planning
Interchange handling
Distance calculation
Fare estimation
Journey details
Distance Calculation Logic

The total journey distance is calculated using the following approach:

The program reads the distance between consecutive stations from the dataset.
User inputs for source and destination stations are treated as case-insensitive.
If a station belongs to multiple lines, all valid route combinations are explored.
For each possible route, the algorithm calculates the cumulative distance step-by-step.
Interchange stations are handled seamlessly while switching lines.
The route with the minimum total distance is selected.
The final output displays:
Total distance travelled
Route used
Interchange details (if applicable)
Fare Calculation Logic

The fare calculation process follows these steps:

The total travel distance is computed using the route planning algorithm.
The distance is mapped to the corresponding fare slab.
The appropriate fare is then calculated automatically.
The final output displays:
Total distance travelled
Calculated metro fare
User Guide

When the user selects the Journey Planner option and enters:

Source station
Destination station
Current time

the program displays:

Optimal route
Interchanges
Journey details
Total travel distance
Estimated metro fare
References
Delhi Metro Rail Corporation (DMRC)
Google Maps
MyMetro.in
start from basic include lal metro lines ek mein hi bonus wlaa read kar dhankse then usko
Metro Lines Added

The project was extended by adding support for the following Delhi Metro lines:

Red Line
Violet Line
Grey Line

Along with the existing functionality of the Journey Planner and Subsequent Metro modules, the following additional features were also implemented:

Fare Calculation System
Total Distance Calculation between source and destination stations
Fare Calculation

The fare is calculated using distance-based fare slabs inspired by the official DMRC fare structure.

Distance Travelled	Fare
Up to 2 km	₹11
2 – 5 km	₹21
5 – 12 km	₹32
12 – 21 km	₹43
Above 32 km	₹54

The fare is automatically determined after calculating the shortest valid route between the selected stations.

Data Collection

The dataset used in this project was compiled using multiple verified sources.

Station names were collected from the official DMRC website.
Travel time between adjacent stations was obtained from DMRC route information.
Distance between consecutive stations was collected using:
Google Maps
MyMetro.in

Distance values are approximate and rounded for simplicity.

Some station naming conventions differed across sources, so users are advised to refer to the provided station data file for exact spellings.

Assumptions

The following assumptions were considered during implementation:

Grey Line

Terminal stations:

Dwarka
Dhansa Bus Stand
Red Line

Terminal stations:

Shaheed Sthal (New Bus Adda)
Rithala
Violet Line

Terminal stations:

Kashmere Gate
Raja Nahar Singh (Ballabgarh)
Metro Timings
Metro services are assumed to begin operating from terminal stations at 6:00 AM.
If the user enters a time beyond operational hours (approximately after 11:00 PM), the program may indicate that metro services are unavailable.
Working of the Program

The Journey Planner and Subsequent Metro functionalities work similarly across all added metro lines.

The system provides:

Route planning
Interchange handling
Distance calculation
Fare estimation
Journey details
Distance Calculation Logic

The total travel distance is calculated using the following process:

The program reads the distance between consecutive stations from the dataset.
User inputs for source and destination stations are case-insensitive.
If a station belongs to multiple lines, all possible valid routes are explored.
For every possible route, the algorithm calculates cumulative distance step-by-step.
Interchanges are handled automatically while switching between metro lines.
The route with the minimum total distance is selected.
The final output displays:
Total distance travelled
Route selected
Interchange details (if applicable)
Fare Calculation Logic

The fare calculation process follows these steps:

The total journey distance is first calculated using the route planning algorithm.
The computed distance is mapped to the appropriate fare slab.
The final fare is then generated automatically.
The output displays:
Total distance travelled
Calculated metro fare
User Guide

When the user selects the Journey Planner option and enters:

Source station
Destination station
Current time

the program displays:

Optimal route
Interchanges
Journey details
Total distance travelled
Estimated metro fare
References
Delhi Metro Rail Corporation (DMRC)
Google Maps
MyMetro.in
\# Delhi Metro Simulator

A comprehensive command-line simulator for the Delhi Metro system that provides real-time journey planning, fare calculation, and metro scheduling information.

## Overview

The Delhi Metro Simulator helps users navigate the Delhi Metro system by offering:
- **Real-time metro schedules** with frequency-based calculations
- **Optimized route planning** across multiple metro lines
- **Intelligent fare calculation** based on distance slabs
- **Support for 5 metro lines** with transfer stations and interchanges

## Features

### 1. Subsequent Metros
Displays upcoming metro arrivals at a selected station with:
- Current metro timing based on peak/non-peak hours
- 4-5 subsequent metro departure times
- Identification of terminal stations for each metro
- Dynamic frequency calculation:
  - **Peak hours** (8–10 AM, 5–7 PM): 4-minute frequency
  - **Non-peak hours**: 8-minute frequency

### 2. Journey Planner
Computes the optimal route between two stations with:
- **Shortest path routing** considering all metro lines
- **Transfer optimization** with 5-minute interchange time
- **Distance calculation** with journey breakdown
- **Fare computation** based on distance slabs
- **Real-time arrival estimates**
- **Interchange details** including number and duration

### 3. Fare Calculator
Automated fare calculation based on DMRC (Delhi Metro Rail Corporation) distance slabs:
- 0–2 km: ₹11
- 2–5 km: ₹11
- 5–12 km: ₹21
- 12–21 km: ₹32
- 21–32 km: ₹43
- 32+ km: ₹54

## Supported Metro Lines

| Line | Terminal Stations | Status |
|------|-------------------|--------|
| **Blue Line** | Dwarka Sector 21, Noida Electronic City, Botanical Garden |
| **Magenta Line** | Janakpuri West, Botanical Garden |
| **Red Line** | Shaheed Sthal (New Bus Adda), Rithala |
| **Violet Line** | Kashmere Gate, Raja Nahar Singh (Ballabgarh) |
| **Grey Line** | Dwarka, Dhansa Bus Stand |

## Data Collection Methodology

### Sources
- **Station Names**: Delhi Metro Rail Corporation (DMRC) official website
- **Distances**: Google Maps and MyMetro.in verification
- **Travel Times**: DMRC official timetables

### Quality Assurance
- All distances verified against multiple authoritative sources
- Station name spellings cross-referenced with official DMRC data
- Travel times validated against published schedules

> **Note**: Please verify station names in the accompanying data file (metro_data.txt) for accuracy, as some naming conventions may have variations.

## System Assumptions

1. **Service Hours**: First metro departs from terminal stations at 6:00 AM
2. **Service End**: After 11:00 PM, no additional metro schedules are available
3. **Interchange Time**: Fixed 5-minute duration at all transfer stations
4. **Blue Line Interchange**: Yamuna Bank serves as a non-displayed interchange for routes between Noida Electronic City and Vaishali
5. **Magenta Line**: Krishna Park extension station not included in current version

## Usage Guide

### Starting the Program ehdnakse kar and add jo miss ho rha h
Delhi Metro Simulator

A comprehensive command-line based Delhi Metro Simulator designed to provide efficient route planning, metro scheduling, fare estimation, and distance calculation across multiple Delhi Metro lines.

The simulator models real-world metro operations by incorporating interchange handling, distance-based fare computation, and time-aware metro scheduling.

Overview

The project allows users to navigate the Delhi Metro network through features such as:

Real-time metro schedule simulation
Intelligent journey planning
Shortest route computation
Distance-based fare estimation
Interchange handling across metro lines
Travel distance calculation
Support for multiple Delhi Metro corridors

The simulator currently supports the following metro lines:

Blue Line
Magenta Line
Red Line
Violet Line
Grey Line
Features
1. Subsequent Metro Finder

Displays upcoming metro arrivals at a selected station based on the current time.

Functionalities
Shows next 4–5 metro timings
Identifies metro destination/terminal station
Simulates realistic metro frequency
Handles peak-hour and non-peak-hour scheduling
Metro Frequency Logic
Peak Hours
8:00 AM – 10:00 AM
5:00 PM – 7:00 PM
→ Metro frequency: every 4 minutes
Non-Peak Hours
→ Metro frequency: every 8 minutes
2. Journey Planner

Computes the optimal route between source and destination stations across all supported metro lines.

Functionalities
Shortest path route calculation
Automatic interchange handling
Travel distance computation
Estimated travel time
Fare calculation
Route breakdown with interchanges
Journey Planning Logic
All valid paths between stations are explored.
If a station belongs to multiple lines, interchange routes are considered automatically.
The algorithm computes cumulative distance step-by-step.
The route with minimum travel distance is selected as the optimal route.
3. Distance Calculator

Calculates the total travel distance between source and destination stations.

Working
Distance between adjacent stations is loaded from the dataset.
The program traverses all possible valid routes.
Distances are accumulated for each route.
Interchanges are handled seamlessly.
The minimum-distance valid path is selected.

The final output displays:

Total distance travelled
Selected route
Interchange stations (if any)
4. Fare Calculator

The simulator automatically computes metro fare using distance-based fare slabs inspired by the DMRC fare structure.

Distance Travelled	Fare
Up to 2 km	₹11
2 – 5 km	₹21
5 – 12 km	₹32
12 – 21 km	₹43
Above 32 km	₹54
Fare Calculation Process
Total journey distance is calculated.
Distance is mapped to the corresponding fare slab.
Final fare is displayed along with journey details.
Supported Metro Lines
Metro Line	Terminal Stations
Blue Line	Dwarka Sector 21 ↔ Noida Electronic City
Blue Line Branch	Yamuna Bank ↔ Vaishali
Magenta Line	Janakpuri West ↔ Botanical Garden
Red Line	Shaheed Sthal (New Bus Adda) ↔ Rithala
Violet Line	Kashmere Gate ↔ Raja Nahar Singh (Ballabgarh)
Grey Line	Dwarka ↔ Dhansa Bus Stand
Data Collection Methodology

The dataset used in the simulator was compiled using multiple verified sources.

Data Sources
Official DMRC website
Google Maps
MyMetro.in
Collected Information
Station names
Distance between consecutive stations
Travel time between stations
Interchange details
Notes
Distance values are approximate and rounded for simplicity.
Some station naming conventions vary across sources; therefore, users are advised to refer to the provided data file for exact spellings.
Assumptions

The following assumptions were considered during implementation:

Metro services begin operating from terminal stations at 6:00 AM.
After approximately 11:00 PM, metro services are assumed unavailable.
Interchange duration is fixed at 5 minutes for all interchange stations.
The following terminal stations are considered:
Grey Line: Dwarka ↔ Dhansa Bus Stand
Red Line: Shaheed Sthal (New Bus Adda) ↔ Rithala
Violet Line: Kashmere Gate ↔ Raja Nahar Singh (Ballabgarh)
User Guide
Journey Planner

When the user selects the Journey Planner option, the program requests:

Source station
Destination station
Current time

The simulator then displays:

Optimal route
Interchange stations
Estimated travel details
Total distance travelled
Calculated fare
Subsequent Metro Finder

When the user selects the Subsequent Metro option:

The user enters a station name and current time.
The program calculates upcoming metro timings.
The next 4–5 available metro departures are displayed.
References
Delhi Metro Rail Corporation (DMRC)
Google Maps
MyMetro.in
