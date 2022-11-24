import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np
import random
from math import sqrt

np.set_printoptions(suppress=True)

#NUMBER_OF_CITIES = 327
NUMBER_OF_CITIES = 22
KILOMETER_VALUE = 252.69
TRAVEL_SPEED = 90
KILOMETRES_PER_GRADE = 111.12

def load_data() -> pd.DataFrame:
    # Set the database we are going to use for modeling our graph

    file = 'archive/DatasetCoordenadas.csv'

    # Load the data into a dataframe

    cities = pd.read_csv(file)

    print("#"*16)
    print(cities.head())
    print("#"*16)
    print(cities.describe())
    print("#"*16)
    
    return cities



def get_distance(ori_lon:float, ori_lat:float, dest_lon:float, dest_lat:float) -> float:

    #It calculates the distances between the two cities, using its coordinates.
    #Then, it gets multiplied by the amount of kilometers in one grade of coordinate
    
    return sqrt((dest_lat - ori_lat)**2 + (dest_lon - ori_lon)**2) * KILOMETRES_PER_GRADE

def get_cost(ori_lon:float, ori_lat:float, dest_lon:float, dest_lat:float) -> float:

    #Gets the cost multiplying the distance by a value per kilometer found on internet
    #The cost is in COP

    distance = get_distance(ori_lon, ori_lat, dest_lon, dest_lat)
    random_factor = random.randrange(1,1000) /1000

    return distance * KILOMETER_VALUE * random_factor

def get_time(ori_lon:float, ori_lat:float, dest_lon:float, dest_lat:float) -> float:

    #Gets the time dividing the distance by a travel speed found on internet
    #The time is in hours

    distance = get_distance(ori_lon, ori_lat, dest_lon, dest_lat)
    random_factor = random.randrange(1,1000) /1000

    return (distance / TRAVEL_SPEED) * random_factor


def get_posible_travels(cities: pd.DataFrame, num_of_travels : int) -> np.ndarray:
    #Initializes all the travels between the cities, in other words, the edges of our future graph

    travels_list = []
    random.seed(1)

    while len(travels_list) < num_of_travels:
        #Gets two random cities
        ori_city_index = random.randint(0,NUMBER_OF_CITIES-1)
        dest_city_index = random.randint(0,NUMBER_OF_CITIES-1)

        if ori_city_index != dest_city_index:
            #Calculates the cost and the time to travel from city A to city B
            cost = get_cost(cities['Longitud'][ori_city_index], cities['Latitud'][ori_city_index], cities['Longitud'][dest_city_index], cities['Latitud'][dest_city_index])
            time = get_time(cities['Longitud'][ori_city_index], cities['Latitud'][ori_city_index], cities['Longitud'][dest_city_index], cities['Latitud'][dest_city_index])
            travels_list.append([ori_city_index, dest_city_index, cost, time])
    
    travels = np.array(travels_list)

    print("#"*16)
    print(travels[:10][:])
    print("#"*16)

    return travels

def build_graph(travels: np.ndarray) -> dict:
    graph = {}

    #It creates all the nodes for the cities
    for index in range(NUMBER_OF_CITIES):
        graph[index] = {}

    #it fills all the edges with the possible travels
    for travel in travels:
        graph[travel[0]][travel[1]] = [travel[2], travel[3]]

    print("#"*16)
    print(dict(list(graph.items())[0:10]))
    print("#"*16)

    return graph

def get_graph() -> tuple([pd.DataFrame, dict]):

    cities = load_data()
    travels = get_posible_travels(cities.head(22), 50)
    graph = build_graph(travels)

    return cities, graph

