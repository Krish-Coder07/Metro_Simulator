File = "metro_data.txt"
#checking that whether station exist or not in the text file
def station_exist_on_metro_line(line, station) :
    f = open(File, "r")    
    for lines in f :
        lines = lines.strip()

        if lines == "" or lines[0] == "#" or lines[0] == "-" :  #skipping the commented lines in the text file
            continue
        list1 = lines.split(",")
        if len(list1) < 2 :  #in this skipping of the texts like [Blue line or such texts which are further comments in the file]
            continue
        if list1[0].strip() == line and list1[1].strip() == station :
            f.close()
            return True
    f.close()
    print("Station not found on this line.")
    return False

#It is defined as an empty dictionary which is later appended with the data from the text file.
#dictionary_of_routes[line] = list of connections on that line.
dictionary_of_routes = {}

#It maps each station to all metro lines that pass through it.
#for exxample: station_lines["Dwarka"] = ["Blue", "Magenta"]
station_lines = {}
#neighbour_station list for each metro line to use in distance andtime calculations between stations
neighbour_station = {}
def time_in_minutes(t) :
   #in this converting the time in minutes so that , I can easily add subtract the frequnecy after what tome next metro comes.
    h, m = t.split(":") # hour, minute being splitted by ':'
    return int(h) * 60 + int(m)

def minutes_to_time(total_minutes) :
   #in the last function I converted the actual time into minutes but now for printing the output , converting ito the formatted time is necessary.
    hour = total_minutes // 60
    minute = total_minutes % 60

    if hour < 10 :
        h = "0" + str(hour)
    else :
        h = str(hour)

    if minute < 10 :
        m = "0" + str(minute)
    else :
        m = str(minute)
    return h + ":" + m#printing the time in HH:MM format.

def frequency_of_metros(t) :
    #t is minutes of current time
    #in this checking whether current time is under peak hours or not.
    if (480 <= t < 600) or (1020 <= t < 1140) :
        return 4 #peak hours
    else :
        return 8 #non peak hours

def formatting_interchange(details) :
    details = details.strip()
    if details == "no" :
        return (False, "", 0)
    #example format:Yes-Magenta(5 minutes interchange) according to textfile I made
    #to rmeove yes and further details which interchange it is
    temp = details.replace("yes-", "")  #now text file will be read as Magenta(5 minutes interchange)

    #now splitting on "("
    parts = temp.split("(")
    line_name = parts[0]  #now it will become "Magenta"
    if len(parts) < 2 :
        return (True, line_name, 0)

   #now extracting number before first space
    time_part = parts[1]             #"5 minutes interchange)"
    minutes = time_part.split(" ")[0]  #"5" in order to make calculations of total time ,necessary to extract
    return (True, line_name, int(minutes))

def extracting_metro_routes() :
    # again it's the same type of formatting that we used earlier while reading the file
    f = open(File, "r")
    for line in f :
        line = line.strip()

        #skipping the blank lines, comments, headings
        if line == "" or line[0] == "#" or line[0] == "-" :
            continue
        parts = line.split(",")
        #to skip all those comments which are not required for the file.
        if len(parts) < 5 :  #if all the main things are there or not like line,station,next station , time , ineterchange
            continue

        #stripping lines in order t avoid \t and \n keywords while reading the files
        metro_line = parts[0].strip().lower()
        station = parts[1].strip()
        next_station = parts[2].strip()
        time_part = parts[3].strip()

        #skipping header lines also
        if time_part == "TravelTime(min)" or not time_part.isdigit() :
            continue

        travel_time_total = int(time_part)
        interchanges_information = formatting_interchange(parts[4].strip())

        #reading distance (km) safely, ignoring inline comments after '#'
        distance_km = 0.0
        if len(parts) >= 6 :
            distance = parts[5] #6th column is of distance in the text ile.
            if "#" in distance :
                distance = distance.split("#")[0]
            distance = distance.strip() #stripping spaces also so that error do not comes if space is there
            if distance != "" : #removing inline comments also
                try :
                    distance_km = float(distance) #if everything is fine then it will be easily converted into distance.
                except :
                    distance_km = 0.0

        # adding a new metro line if it is not there in routes
        if metro_line not in dictionary_of_routes : #to check whether till now this line has been encounetered or not.
            dictionary_of_routes[metro_line] = [] #if not then make a new line and load that station in that in the routes dictionary.

        #this append simply stores 1 station's full travelling info inside the line's list.
        dictionary_of_routes[metro_line].append({
            "station" : station, "next" : next_station, "time" : travel_time_total,"interchange" : interchanges_information,"distance":  distance_km})

        #building neighbour_station list for this line
        if metro_line not in neighbour_station : # if this metro line is not already in the neighbour_station list, it will create an empty entry for it
            neighbour_station[metro_line] = {}
        if station not in neighbour_station[metro_line] : # if this station does not exist under this metro line,it will create a list for its connections
            neighbour_station[metro_line][station] = []
        if next_station != "end" : # only add next_station if it is not "end"
            if next_station not in neighbour_station[metro_line] : # make sure next station also exists in the neighbour_station list
                neighbour_station[metro_line][next_station] = []
            neighbour_station[metro_line][station].append((next_station, travel_time_total))#add a conection from station to next station along with travel time
            neighbour_station[metro_line][next_station].append((station, travel_time_total))#add the reverse connection next station to station for easy lookup

        # keeping track of station list in metro lines now
        #adding the current station to station lines if it isn't there already in sttaion lines
        if station not in station_lines :
            station_lines[station] = []

        #adding the line name under this station (only once)
        if metro_line not in station_lines[station] :
            station_lines[station].append(metro_line)

        #doing this also for the same sttaion.
        #ensuring whether that next station also exist in the dictionary.
        if next_station not in station_lines :
            station_lines[next_station] = []

        #adding the line to the next station (only once)
        if metro_line not in station_lines[next_station] :
            station_lines[next_station].append(metro_line)

    f.close()

reversed_done = False  # initially route is not reversed
#now making this for reverse route also becuase previously made for one direction onnly  but what if direction gets reversed
def reverse_routes() :
    #making reverse connections in routes (for both travel directions)
    global reversed_done
    if reversed_done :
        return
    reversed_done = True #now route is reversed.

    for line in dictionary_of_routes :
        new_entries = []
        for info in dictionary_of_routes[line] :
            start = info["station"]
            end = info["next"]
             #for each station , reversing the station and next station.
            if end == "end" :
                continue
             #now loading each sttaion's information like which sttaion is current , what will be the next station,interchange information,etc.
            reverse = {
                "station" : end, "next" : start, "time" : info["time"], "interchange" : info["interchange"],"distance" : info.get("distance", 0.0)}
            new_entries.append(reverse)
        for item in new_entries :
            dictionary_of_routes[line].append(item)

#first trains at 06:00 from these terminal stations.
#this is important as through this only metro will originate first
#on blue line terminal stations which I am assuming Dwarka sec 21 , vaishali and noida electronic city to be terminal sttaions.
first_metro_originates = {
    "blue" : [ "dwarka sector 21","vaishali","noida electronic city"],
    #on magemta line terminal stations are Janakpuri west and botanical garden only.
    "magenta" : ["janakpuri west","botanical garden"],
    #on red line terminal stations are Shaheed Sthal (New Bus Adda) and Rithala only.
    "red" : ["shaheed sthal (new bus adda)","rithala"],
    #on grey line terminal stations are Dwarka and Dhansa Bus Stand only
    "grey" : ["dwarka","dhansa bus stand"],
    #on red line terminal stations are Kashmere Gate and Raja Nahar Singh (Ballabgarh).
    "violet" : ["kashmere gate","raja nahar singh (ballabgarh)"]
    }

first_arrival_of_metro = {} #first metro arrival getting stored in this,
first_arrival_from_terminal = {} #from which terminal metro is coming on specific metro line.

def compute_first_arrivals() :
#this function is used to calculate the first metro reach at every station from the terminal stations
#where metro is starting at 6 A.M
    global first_arrival_of_metro, first_arrival_from_terminal
    first_arrival_of_metro = {}
    first_arrival_from_terminal = {}

    first_metro_time = time_in_minutes("06:00")

#going through every metro line in routes , and if there is no neighbour_station data , it is getting skipped.
    for line in dictionary_of_routes :
        if line not in first_metro_originates :
            continue
        if line not in neighbour_station :
            continue

        #list of all stations on this line
        stations_on_line = list(neighbour_station[line].keys()) #here keys are the the name of all sttaions present on that line.

        #list all_possible_ways[] where it stores station1, seond sttaion and travel time on this line
        all_possible_ways = []
        for i in neighbour_station[line] :
            neighbours = neighbour_station[line][i]
            for neighbour, travel_time in neighbours :
                all_possible_ways.append((i, neighbour, travel_time))

        #now checking for each terminal
        for terminal in first_metro_originates[line] :
            #skipping if the terminal is not found in neighbour_station_list.
            if terminal not in neighbour_station[line] :
                continue
            # terminal_to_station dictionary  will store the travel time (in minutes) also it finds the minimum time.
            # from this terminal to every other station
            terminal_to_station = {}
            for i in stations_on_line :
                terminal_to_station[i] = None #menas no path found.
            terminal_to_station[terminal] = 0  #time from terminal to itself terminal will be 0 minutes

            n = len(stations_on_line) #n = total sttaions on the metro line.
            #going through all the stations which is present on that particular metro line and finding the best time and updating it.
            i = 0
            while i < n - 1:
                flag = False #it becomes true if any terminal_to_station time value becomes better else it remains same.
                #here original , final are just for reference which means from any X station to any Y station.
                for original,final,time_from_original_to_final in all_possible_ways:
                    if terminal_to_station[original] is not None :  
                #means that if we dont know how much time it will take to reach station that are prior to destination then we cant even find time to reach even destination.
                        new_time = terminal_to_station[original] + time_from_original_to_final #if metro reach original in x minutes then x+t for reaching to final sttaion.
                        if terminal_to_station[final] is None or new_time < terminal_to_station[final] : 
                            #means we havent find any possible time to reach final sttaion or we found the better time to reach that final sttaion.
                            terminal_to_station[final] = new_time #updating that shortest time.
                            flag = True
                if not flag :
                    break #if time doesnt get improved then loop gets breaked.
                i = i + 1
            
            #for each station on that line , if time from terminal to the station is known , adding that to 06:00 AM and storing in a tuple
            for i in stations_on_line :
                if terminal_to_station[i] is not None :
                    arrival_time = first_metro_time + terminal_to_station[i]
                    first_arrival_from_terminal[(line, terminal, i)] = arrival_time #storing that time in a tuple

                    key = (line, i) #updating the overall earliest time for this sttaion on the line.
                    if key not in first_arrival_of_metro or arrival_time < first_arrival_of_metro[key] :
                        first_arrival_of_metro[key] = arrival_time

def get_first_arrival_time(line, station) :
#tellswhen first metro reach at a particular station of that particular metro line,
#it will be used to calculate next metro as frequency will be added in this now for next metros.
    key = (line, station) #converts into the tuple.
    if key not in first_arrival_of_metro:
        return None
    return first_arrival_of_metro[key] #same format which I did in first_arrival

def get_first_arrival_time_from_terminal(line, station, terminal) :
    #this is to get first-arrival time from a specific terminal as a metro line can have different terminals.
    key = (line, terminal, station)
    if key not in first_arrival_from_terminal :
        return None
    return first_arrival_from_terminal[key] #returns total time in minutes

#calling of the func in the particular order only becuase :
#first data will be extracted from the text file and route will be loaded then it forms reverse root as it should be bidirectional.
#now calling first_arrival_of_metro function becuase after this only next metros will be calculated on the basis of this function
extracting_metro_routes()
reverse_routes()
compute_first_arrivals()

#function to calculate travel time between two stations on same line
def time_on_same_line(line, start_station, end_station) :
    total_time = 0 #initally total time is 0
    found_start = 0 #initially initialised that sttaion is not found so inititalised by 0
    for info in dictionary_of_routes[line] :
        station = info["station"]
        next_station = info["next"]
        if station == start_station:
            found_start = 1 #when station is found
        if found_start == 1 :
            if next_station == end_station :
                total_time = total_time + info["time"] 
                return total_time
            if next_station != "end" :
                total_time = total_time + info["time"]
    return -1 #if station not found due to any kind of error whether if it's there in naming issue.

def get_common_line(station1, station2) :
    #this is used to define that which metro line is common between two stations.
    if station1 not in station_lines or station2 not in station_lines: #checks stations
        return "" #this means no common metro line.
    #now get list of all lines present on that station.
    lines1 = station_lines[station1]
    lines2 = station_lines[station2]
    for line in lines1 :
        if line in lines2 :
            return line #checking for common metro line
    return ""

def find_interchange_station(line1, line2) :
    #finds interchange station where more than 1 metro line is there.
    for station in station_lines: #itertaing over each station.
        lines = station_lines[station]
        if line1 in lines and line2 in lines:
            return station
    return "" #means no interchange metro station.

minimum_time = None
shortest_route = None

def find_shortest_route(start_station, end_station) :
    global minimum_time, shortest_route #made global so they can be modified while finding better route and minimum time.
    #resetting to none is important as every time we start a new shortest-route search.
    minimum_time = None
    shortest_route = None

    if start_station not in station_lines or end_station not in station_lines :
        #This checks if the stations actually exist in the file and same for end stations.
        return None, None

    combinations = set() #set to store all combinations for example jankapuri west can have two combiation which is (janakpuri west , blue and janakpuri , magenta)
    all_possible_ways = [] # to compute shortest route

    for line in dictionary_of_routes :
        for info in dictionary_of_routes[line] :
            station = info["station"]
            next_station = info["next"]
            travel_minutes = info["time"]
            inter = info["interchange"]

            combinations.add((station, line)) #add in combinations set in format of (station,line)
            if next_station != "end" :
                combinations.add((next_station, line)) #adding next sttaion one that line in the set.
                all_possible_ways.append(((station, line), (next_station, line), travel_minutes))

            if inter[0] :  #if there is an interchange
                target_line = inter[1]
                delay = inter[2] 
                combinations.add((station, target_line))
                all_possible_ways.append(((station, line), (station, target_line), delay))

    if not combinations :  # if for some reason states set is empty
        return None, None

    time_from_start = {} #stores minimum time from source to every (station, line) state
    previous_state = {} #stores from which state we came to this state (for route reconstruction)

    #initialize distances
    for i in combinations :
        time_from_start[i] = None #no time known yet to reach this state
        previous_state[i] = None # no previous stations known yet for this state

    #starting states : all lines that pass through the start station
    start_states = [] #stores (station,line) from where journey will be started
    for line in station_lines[start_station] :
        s = (start_station, line) #making tuple
        if s in time_from_start: #checks whether valid state or not
            time_from_start[s] = 0 
            start_states.append(s)

    if not start_states:
        return None, None #if station do not have valid metro line m it will return none and "no route" will be displayed,

    n = len(combinations) #all possible states (station,line)
    i = 0
    while i < n - 1:
        flag = False
        for (x, j, k) in all_possible_ways: #x is start , j is reaaching station , k is travel time
            if time_from_start[x] is not None :
                new_time = time_from_start[x] + k #calculating new travel time.
                if time_from_start[j] is None or new_time < time_from_start[j]:
                    time_from_start[j] = new_time #updating if new time is better.
                    previous_state[j] = x
                    flag = True
        if not flag: #if no change
            break
        i = i + 1

    #same logic as done for start states.
    end_states = [] 
    for line in station_lines[end_station] : 
        s = (end_station, line)
        if s in time_from_start and time_from_start[s] is not None:
            end_states.append(s)
    if not end_states :
        return None, None
    
    best_end_state = None #will store that from which state it is best
    best_time_value = None
    for i in end_states:
        if best_time_value is None or time_from_start[i] < best_time_value: #comparing which state and best time state is better
            best_time_value = time_from_start[i]
            best_end_state = i

    path = [] #final metro route
    current = best_end_state
    while current is not None:
        path.append(current) #making reverse route through which it will reach source station
        current = previous_state[current]
    path.reverse() #when route is reversed , reversing it again will give route in the required direction.

    minimum_time = best_time_value
    shortest_route = path

    return minimum_time,shortest_route

def compute_total_distance(route ):
    #calculating total distance (in km) for the given path
    if route is None:
        return 0.0
    cumulative_distacnce= 0.0 #initally it is 0.
    for i in range(1, len(route)) :
        station, line = route[i - 1] #parwise station distance calculation.
        next_station, next_line = route[i]
        if line != next_line: #line change distnace ignoring
            continue
        for info in dictionary_of_routes[line] :
            if info["station"] == station and info["next"] == next_station: #now storing in actual list
                cumulative_distacnce = cumulative_distacnce + info.get("distance", 0.0)
                break
    return cumulative_distacnce

def calculate_fare(distance_km): #using distance_km varibale which I initialized earlier
    # fare calculation based on distance slabs availabile on dmrc site.
    if distance_km <= 2: #if distance is less than 2km fare will be 11rs.
        return 11
    elif distance_km <= 5: #if distance is greater than 2km less than equal to 5km fare will be 11rs.
        return 11
    elif distance_km <= 12: #if distance is greater than 5km less than equal to 12km fare will be 21.
        return 21
    elif distance_km <= 21: #if distance is greater than 12km less than equal to 21km fare will be 32rs.
        return 32
    elif distance_km <= 32: #if distance is greater than 21km less than equal to 32km fare will be 43rs.
        return 43
    else:
        return 54 #if distance is greater than 43km fare will be 54rs.

def next_times_for_terminal(line, station, current_time_minutes, terminal, count_limit):
    # compute upcoming arrival times at a station coming from a particular terminal
    service_start = time_in_minutes("06:00") #initialising the service hours , at 6
    service_end = time_in_minutes("23:00") #at 11 PM service will be closed.

    station_first = get_first_arrival_time_from_terminal(line, station, terminal) #on this station when firts metro will arrive from terminal.
    if station_first is None or station_first >= service_end: #if after 11pm metro comes then it returns none.
        return [] 

    # ensure we start no earlier than first arrival for this direction and service hours
    t = current_time_minutes
    if t < service_start: #if time is before 6AM it will set as current time 6 AM
        t = service_start
    if t < station_first: #same for this if current time is before first metro arrival , current time will be set to first metro arrival.
        t = station_first

    result = []
    while t < service_end and len(result) < count_limit:
        freq_value = frequency_of_metros(t) #at that time metro is coming at which frequency is stored in freq_value
        minutes_from_first_here = t - station_first #time from first metro to current time.
        if minutes_from_first_here < 0:
            minutes_from_first_here = 0
        remainder = minutes_from_first_here % freq_value #checks current time is in which interval metro time.
        if remainder != 0:
            t = t + (freq_value - remainder) 
            if t >= service_end: #after 11pm service ends.
                break
        result.append(t) #storing the frequencies time in the list.
        t = t + freq_value #calculating next metro time.
    return result

def NextMetros(line, station, current_time_str):
    #checking whether station exists or not
    if not station_exist_on_metro_line(line, station): #if station not found function gets terminated.
        return
    service_start = time_in_minutes("06:00") #convert service times into minutes
    service_end = time_in_minutes("23:00")
    current_time_minutes = time_in_minutes(current_time_str) #user input in string also gets converted into minutes.

    if current_time_minutes >= service_end: #if input is after 11pm , service gets closed.
        print("Metro service is closed for today. Last metro before 23:00.")
        return
    #if we do not have terminal information for this line
    if line not in first_metro_originates :
        #calculating first arrival of metro at this station on this line
        earliest_arrival_time = get_first_arrival_time(line, station) #when first metro arrives the station.
        if earliest_arrival_time is None or earliest_arrival_time >= service_end:
            print("No metro reaches this station on this line.")
            return

        if current_time_minutes < earliest_arrival_time: #if time is before first metro arrival time , current time gets set to first metro arrival time.
            current_time_minutes = earliest_arrival_time 
        else:
            if current_time_minutes < service_start: #service gets closed.
                current_time_minutes = service_start

        freq_value = frequency_of_metros(current_time_minutes) #at what frequency metro is coming at current time.
        minutes_from_first_here = current_time_minutes - earliest_arrival_time #current time in minutes from arrival of first metro.
        remainder = minutes_from_first_here % freq_value #how much extra time is left from the last metrp

        if remainder == 0:
            next_metro_in = current_time_minutes #next mettro will be current one which has arrived the station.
        else:
            wait = freq_value - remainder #wait is time that user needs to wait.
            next_metro_in = current_time_minutes + wait

        if next_metro_in >= service_end:
            print("Metro service is closed for today. No more metros.")
            return

        print()
        print("Next metro at", minutes_to_time(next_metro_in))
        print("Subsequent metros at:", end=" ")

        time_of_next_metro = next_metro_in
        for i in range(4):
            new_frequency = frequency_of_metros(time_of_next_metro) 
#finding frequency each time because there can be case when time is 9:48 then metro will arrive 9:52 then 9:56 
#but now it will come at 10:04 becuase now it comes under non peak hours where frequency is of 8 minutes.
            time_of_next_metro = time_of_next_metro + new_frequency
            if time_of_next_metro >= service_end: #if serive hours get finished.
                break
            print(minutes_to_time(time_of_next_metro), end="")
            if i < 3: 
                print(", ", end="")
            else:
                print(" ...", end="")
        print()
        return

    metros = [] #list of tuples (arrival_time, terminal_name)
    for terminal in first_metro_originates[line]: #from which temrinal metro is coming
        times = next_times_for_terminal(line, station, current_time_minutes, terminal, 5)
        for t in times:
            metros.append((t, terminal))

    if not metros: #if no possible time for metro found then :
        print("No metro reaches this station on this line.")
        return

    #sorting the tuple in ascending order from which terminal which metro is coming.
    metros.sort()
    five_distinct_metros = []
    passed = set() #to ensure that same(time,terminal) do not comes again.
    for t, terminal in metros:
        key = (t, terminal) #this makes unique tuple 
        if key in passed: #means already added in the set
            continue
        passed.add(key)
        five_distinct_metros.append((t, terminal))
        if len(five_distinct_metros) >= 5: #showing only 5 metros on the output.
            break

    print("Next metros from " + station + " on " + line + " Line:")
    for t, terminal in five_distinct_metros:
        print(minutes_to_time(t) + " coming from " + terminal)
    print()

def journey_planner(start, end, travel_time):
   #convert metro service start and end times into minutes again.
    service_start = time_in_minutes("06:00")
    service_end = time_in_minutes("23:00")
    # convert the user's entered time (HH:MM) into minutes
    current_minutes = time_in_minutes(travel_time)
   # to check if the user is trying to travel outside metro operating hours
    if current_minutes < service_start or current_minutes >= service_end:
        print("No service available. Metro operates from 06:00 AM to 11:00 PM.")
        return

    total_travel_time, route = find_shortest_route(start, end) # shortest route which icluded only travel and interchange sttaion time.
    if total_travel_time is None:
        print("Route not found.") #no possible time found
        return

     #calculation of total distance and fare for this shortest route.
    total_distance = compute_total_distance(route)
    fare = calculate_fare(total_distance)

    start_station, start_line = route[0] #searching for starting line for the route
    station_first = get_first_arrival_time(start_line, start_station)#calculating first arrival at source on that line
    if station_first is None:
        station_first = service_start

    if current_minutes < station_first:  #if time is before first metro arrival time , current time gets set to first metro arrival time.
        current_minutes = station_first

    freq_value = frequency_of_metros(current_minutes)#calculating the next metro at the source based on current time and frequency.
    minutes_from_first_here = current_minutes - station_first
    remainder = minutes_from_first_here % freq_value

    if remainder == 0:
        next_metro = current_minutes
    else:
        next_metro = current_minutes + (freq_value - remainder)

    if next_metro >= service_end:
        print("Metro service is closed for today. No more metros.")
        return
    print()
    print("Next metro at " + minutes_to_time(next_metro))
    print("Start from " + start_station + " on " + start_line + " Line")
    print("Board metro at " + minutes_to_time(next_metro))

    current_time = next_metro   #travel time till now.

    total_interchange_time = 0
    interchange_count = 0

    for i in range(1, len(route)): #looping through route where station and line are stored.
        station, line = route[i - 1]
        next_station, next_line = route[i]

        if line == next_line: #if the metro line is same.
            next_station_time = 0 
            for info in dictionary_of_routes[line]:
                if info["station"] == station and info["next"] == next_station:
                    next_station_time = info["time"]
                    break
            current_time = current_time + next_station_time #total time

        else:
            #line change at station if there is interchange station.
            print("Reach " + station + " at " + minutes_to_time(current_time))
            interchnage_time = 0 #now storing interchange time from the text file.
            for info in dictionary_of_routes[line]:
                if (info["station"] == station and info["interchange"][0] and info["interchange"][1] == next_line) :
                    interchnage_time = info["interchange"][2]
                    break

            # if interchange_time is zero but there is a line change, still count it as interchange with 0 min
            total_interchange_time = total_interchange_time + interchnage_time
            interchange_count = interchange_count + 1

           #time of boarding next line after interchange
            ready_time = current_time + interchnage_time

            if ready_time < service_start:
                ready_time = service_start

            freq2 = frequency_of_metros(ready_time) #now again calculating the frequency for next line.
            station_first2 = get_first_arrival_time(next_line, station)#again getting arrival time of first metro on new line.
            if station_first2 is None :
                station_first2 = service_start

            minutes_from_first_here2 = max(0, ready_time - station_first2)
            remainder2 = minutes_from_first_here2 % freq2

            if remainder2 == 0 :
                departure_time_after_interchange = ready_time #next departure metro time on new metro line.
            else :
                departure_time_after_interchange = ready_time + (freq2 - remainder2)

            print("Interchange time: " + str(interchnage_time) + " minutes")
            print("Change to " + next_line + " Line at " + station)
            print("Board metro on " + next_line + " Line at " + minutes_to_time(departure_time_after_interchange))

            current_time = departure_time_after_interchange

   #printing fare,distance,total journey time and arrival time of the metro at the destination sttaion.
    print("Arrive at " + end + " at " + minutes_to_time(current_time))
    print()
    print("Total journey time: " + str(current_time - next_metro) + " minutes")
    print("Total distance: " + str(round(total_distance, 2)) + " km")
    print("Fare: Rs " + str(fare))
    print("Number of interchanges: " + str(interchange_count))
    print("Total interchange time: " + str(total_interchange_time) + " minutes")
    print()


#input from user :
while True:
    print("====================")
    print("  DELHI METRO HELP  ")
    print("====================")
    print("1. Subsequent Metros")
    print("2. Journey Planner")
    print("3. Exit")
    print("====================")
    print()

    choice = input("Enter your choice (1/2/3): ").strip()


    #option 1 : subsequent metros
    if choice == "1":
        print("=== Subsequent Metros ===")
        print()

        while True:
            try:
                line = input("Enter line name: ").strip().lower()

                if line not in dictionary_of_routes:
                    raise ValueError
                break
            except:
                print("Invalid line, Please enter a valid metro line name.")

        while True:
            try:
                station = input("Enter station name: ").strip().lower()

                if not station_exist_on_metro_line(line, station):
                    raise ValueError
                break
            except:
                print("Enter a valid station on the " + line +" line.")

        while True:
            try:
                current = input("Enter current time (HH:MM): ").strip()
                h, m = current.split(":")
                h = int(h)
                m = int(m)
                if not (0 <= h <= 23 and 0 <= m <= 59):
                    raise ValueError
                break
            except:
                print("Invalid time , Enter time in format HH:MM.")

        print()
        NextMetros(line, station, current)

    #  option 2 : journey planner
    elif choice == "2":
        print("=== Journey Planner ===")
        print()

        while True:
            try:
                source = input("Enter source station: ").strip().lower()
                if source not in station_lines:
                    raise ValueError
                break
            except:
                print("Enter a valid station")

        while True:
            try:
                destination = input("Enter destination station: ").strip().lower()
                if destination not in station_lines:
                    raise ValueError
                if destination == source:
                    raise Exception
                break
            except ValueError:
                print("Invalid station! Destination station does not exist.")
            except Exception:
                print("Source and destination cannot be same , Try again.")

        while True:
            try:
                travel_time = input("Enter time of travel (HH:MM): ").strip()
                h, m = travel_time.split(":")
                h = int(h)
                m = int(m)
                if not (0 <= h <= 23 and 0 <= m <= 59):
                    raise ValueError
                break
            except:
                print("Invalid time , enter time in format (HH:MM).")

        journey_planner(source, destination, travel_time)

    #option 3: exit
    elif choice == "3":
        print("Thank you for using Delhi Metro Help.")
        print()
        break
    else:
        print("Invalid option! Please enter 1, 2 or 3.")



