from mpl_toolkits.basemap import Basemap
from queue import PriorityQueue
from data import get_graph, NUMBER_OF_CITIES
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np


#Define the test graph for debuggin
graph = {}

graph['start'] = {}
graph['a'] = {}
graph['b'] = {}
graph['c'] = {}
graph['d'] = {}
graph['fin'] = {}
graph['start']['a'] = [1,2]
graph['start']['b'] = [4,6]
graph['start']['c'] = [5,1]
graph['a']['b'] = [2,3]
graph['a']['c'] = [3,2]
graph['a']['d'] = [2,4]
graph['b']['fin'] = [2,7]
graph['c']['d'] = [2,2]
graph['c']['fin'] = [1,8]
graph['d']['fin'] = [3,6]


def dijkstra_priority_queue(graph, start_node, target_node):
    distances = {}              #O(1)
    parents = {}
    parents[start_node] = [None]
    distances[start_node] = [[0,0]]

    Q = PriorityQueue()
    visited = set()
    for node in graph.keys():   #O(V)
        if node != start_node:
            distances[node] = [[float('inf'), float('inf')]]
            parents[node] = [None]
    Q.put((start_node, distances[start_node]))
    visited.add(start_node)
    while Q.empty() == False:
        current_vertex = Q.get()[0]     #O(logE)
        for neighbor in graph[current_vertex].keys():
            if neighbor not in visited:                     #O(1)
                Q.put((neighbor, distances[neighbor]))      #O(logE)
                visited.add(neighbor)                       #O(1)
            for distance in distances[current_vertex]:      #O(E)
                cost = distance[0] + graph[current_vertex][neighbor][0]
                time = distance[1] + graph[current_vertex][neighbor][1]
                distances[neighbor].append([cost, time])
                parents[neighbor].append(current_vertex)
            
            best_cost = [float('inf'), float('inf')]
            best_time = [float('inf'), float('inf')]
            best_parent_cost = None
            best_parent_time = None

            for i in range(len(distances[neighbor])):
                if distances[neighbor][i][0] < best_cost[0]:
                    best_cost = distances[neighbor][i]
                    best_parent_cost = parents[neighbor][i]
                if distances[neighbor][i][1] < best_time[1]:
                    best_time = distances[neighbor][i]
                    best_parent_time = parents[neighbor][i]
            
            distances[neighbor] = [best_cost, best_time]
            parents[neighbor] = [best_parent_cost, best_parent_time]

    if parents[target_node] is None:
        return -1
    else:
        # Knowing the target we can find the shortest path in terms of weight from starting node to it.
        final_node = target_node
        final_path1 = []
        final_path2 = []
        while final_node is not start_node:
            final_path1.append(final_node)
            final_node = parents[final_node][0]
        final_path1.append(start_node)
        final_node = target_node
        while final_node is not start_node:
            final_path2.append(final_node)
            final_node = parents[final_node][1]
        final_path2.append(start_node)
        final_path1.reverse()
        final_path2.reverse()
        return distances[target_node],final_path1, final_path2

    '''

    Clasical implementation of Dijkstra, O(E*logE)
    
    while Q.empty() == False:
        current_vertex = Q.get()[0]
        if current_vertex not in visited:
            visited.add(current_vertex)
            for neighbor in graph[current_vertex].keys():
                if distances[neighbor] > distances[current_vertex] + graph[current_vertex][neighbor]:
                    distances[neighbor] = distances[current_vertex] + graph[current_vertex][neighbor]
                    parents[neighbor] = current_vertex
                    Q.put((neighbor, distances[neighbor]))
    '''


# Make a plot showing the given route after doing Dijkstra

'''def printing_route(graph, start_node, target_node):
    calculated_path = []
    grafo = data.grafo_for_dijkstra
    value = dijkstra_priority_queue(graph, start_node, target_node)
    if value != -1:
        calculated_path = value[1]

    # Create a sub-graph which is the trajectory we are looking for.
    path_graph = {}
    path_graph[start_node] = {}
    path_graph[start_node][calculated_path[0]] = grafo[start_node][calculated_path[0]]

    for k in range(0, len(calculated_path)-1):
        path_graph[calculated_path[k]] = {}
        path_graph[calculated_path[k]][calculated_path[k+1]] = grafo[calculated_path[k]][calculated_path[k+1]]
    
    return path_graph'''
    
def plot_graph(cities: pd.DataFrame, graph: dict, starting_city_index:int, target_city:int):
    G = nx.DiGraph()
    m = Basemap(projection = 'merc',
            llcrnrlat = -4,
            urcrnrlat = 12.5,
            llcrnrlon = -80,
            urcrnrlon = -65,
            lat_ts = 20,
            resolution = 'c')
    x = np.array(cities['Longitud']) 
    y = np.array(cities['Latitud']) 

    x,y = m(x,y)
    pos = {}
    for k in range(NUMBER_OF_CITIES):
        G.add_node(cities['Ciudad'][k])
        pos[cities['Ciudad'][k]] = (x[k],y[k]) 

    for ori_node_index in graph.keys():
        for dest_node_index in graph[ori_node_index].keys():
                G.add_edge(cities['Ciudad'][ori_node_index],cities['Ciudad'][dest_node_index],weight = graph[ori_node_index][dest_node_index])

    plt.figure(figsize = (6,7))
    nx.draw(G,pos,node_color = 'k',node_size = 30)
    m.drawcoastlines()
    m.drawcountries(linewidth = 3)
    m.drawmapboundary(fill_color = 'aqua')
    m.fillcontinents(color = 'coral', lake_color = 'aqua')


    shortest_paths = dijkstra_priority_queue(graph, starting_city_index, target_city)

    F = nx.DiGraph()
    posF = {}
    for node_index in shortest_paths[1]:
        F.add_node(cities['Ciudad'][node_index])
        posF[cities['Ciudad'][node_index]] = (x[int(node_index)],y[int(node_index)]) 
    
    for i in range(1,len(shortest_paths[1])):
        F.add_edge(cities['Ciudad'][shortest_paths[1][i-1]], cities['Ciudad'][shortest_paths[1][i]])

    nx.draw(F,posF, node_color = 'r', node_size = 5, edge_color = 'r')

    H = nx.DiGraph()
    posH = {}
    for node_index in shortest_paths[2]:
        H.add_node(cities['Ciudad'][node_index])
        posH[cities['Ciudad'][node_index]] = (x[int(node_index)],y[int(node_index)]) 
    
    for i in range(1,len(shortest_paths[2])):
        H.add_edge(cities['Ciudad'][shortest_paths[2][i-1]], cities['Ciudad'][shortest_paths[2][i]])

    nx.draw(H,posH, node_color = 'green', node_size = 30, edge_color = 'b')

    #weight_labels = nx.get_edge_attributes(G,'weight')
    #nx.draw_networkx_edge_labels(G,pos,edge_labels=weight_labels)

    nx.draw_networkx_labels(G,pos,font_size = 8)
    plt.axis('equal')
    plt.show()


#print(printing_route(graph_cities, starting_city, destination_city))
#plot_graph()

def run():
    cities, graph = get_graph()

    STARTING_CITY = 21 #medellin
    DESTINATION_CITY = 16 #yopal

    plot_graph(cities, graph, STARTING_CITY, DESTINATION_CITY)




run()
