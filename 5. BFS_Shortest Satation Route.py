print("\n----------------------------------- BFS (Breadth-First Search) ----------------------------------- ")
from collections import deque

#STATION
class Station:
    # variables
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_connection(self, another_station):
        # put another station in neighbors in self class
        self.neighbors.append(another_station)

        # put self in neighbors in another_station
        another_station.neighbors.append(self)

# Breadth-First Search Algorithms
def bfs(start, goal):
    # variables
    previous = {}
    queue = deque()             # station list
    current = None

    # initial setting
    previous[start] = None      # key if from value station
    queue.append(start)

    # look if there is unseen station and doesn't find the destination yet 
    while len(previous) > 0 and current != goal:        # done if false (continue if true)
        current = queue.popleft()

        for neighbor in current.neighbors:
            if neighbor not in previous.keys():
                queue.append(neighbor)
                previous[neighbor] = current

    if goal == current:
        path = [goal]
        start = previous[goal]       # previous[current] = previous station
        path.append(start)
        while previous[start] != None:
            path.append(previous[start])
            start = previous[start]
        return path
    else:
        return None


#READ
stations = {}
in_file = open('stations.txt')

# loop for subway line
for line in in_file:
    data_w_space = line.strip().split(" - ")
    previous_station = None

    # loop for stations
    for name in data_w_space:
        station_name = name.strip()

        # register key & instance into dictionary if it's not registered yet
        if station_name not in stations.keys():
            current_station = Station(station_name)         # current_station의 이름은 station_name이다. add_connection에 쓸 수 있도록 current_station 설정
            stations[station_name] = current_station        # 사전 등록: stations 사전에 역 이름 (current station instance)를 등록

        else:
            current_station = stations[station_name]        # current_station을 역 이름 (value)로 전환

        # connect neighbor stations add_connection
        if previous_station != None:                            # 첫번째 역은 연결시킬 필요가 없음
            current_station.add_connection(previous_station)    # 현재 역과 전 역을 neighbor로 추가

        # convert current station to prev station
        previous_station = current_station

in_file.close()

# TEST
start_name = input("Start:")
goal_name = input('Destination:')

start = stations[start_name]
goal = stations[goal_name]

path = bfs(start, goal)
for station in path:
    print(station.name)
