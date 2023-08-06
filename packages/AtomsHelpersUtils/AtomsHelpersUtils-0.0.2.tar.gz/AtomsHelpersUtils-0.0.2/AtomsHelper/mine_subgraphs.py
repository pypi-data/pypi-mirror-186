# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 12:45:27 2022

@author: eccn3
"""

import networkx as nx
import networkx.algorithms.isomorphism as iso

import numpy as np
import matplotlib.pyplot as plt

import itertools

def enumerate_subgraphs(graph):
    
    G = graph
    all_connected_subgraphs = []
    
    # here we ask for all connected subgraphs that have at least 2 nodes AND have less nodes than the input graph
    for nb_nodes in range(2, G.number_of_nodes()):
        for SG in (G.subgraph(selected_nodes) for selected_nodes in itertools.combinations(G, nb_nodes)):
            if nx.is_connected(SG):
                print(SG.nodes)
                all_connected_subgraphs.append(SG)
                
    return all_connected_subgraphs

def draw_graph(graph):
    """
    Displays the graph
    :param graph: networkx graph object
    :return: None
    """
    
    Pt = [i for i in graph.nodes() if 'Pt' in graph.nodes[i]['element']]
    spaced = np.vstack((np.linspace(-0.95, 0.95, len(Pt)), np.ones(len(Pt))*-1)).T
    fixed_positions = {i: tuple(spaced[count]) for count, i in enumerate(Pt)}
    for i in graph.nodes:
        if graph.nodes[i]['element'] != 'Pt':
            fixed_positions[i] = (np.random.uniform(-1, 1), np.random.uniform(0,1))
            
    
    if bool(fixed_positions):
        try:
            if graph.graph['bonds_solved'] == "Problem with solver":
                pos = nx.spring_layout(graph, pos = fixed_positions, weight=None)
            else:
                pos = nx.spring_layout(graph, pos = fixed_positions)
        except:
            pos = nx.spring_layout(graph, pos = fixed_positions)
            
    else:
        pos = nx.spring_layout(graph)
    plt.figure(figsize = (5,3), dpi = 300)
    nx.draw(graph, with_labels=False, node_size=1500, node_color="skyblue",
            node_shape="o", alpha=0.5, linewidths=4, font_size=25,
            font_color="black", font_weight="bold", width=2, edge_color="grey",
            pos=pos)
    node_labels = nx.get_node_attributes(graph, 'element')
    edge_labels = nx.get_edge_attributes(graph,'weight')
    nx.draw_networkx_labels(graph, pos, node_labels)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels)
    plt.show()

def draw_all_graphs(graphs):
    for i in graphs:
        draw_graph(i)

def draw_all_graph_in_objects(objects):
    for i in objects:
        draw_graph(objects.graph)

def check_iso(graph1, graph2):
    """ Check isomorphism using node attribute {atomic_number} and
    edge attribute {type}.
    Parameters
    ----------
    graph1: networkx Graph object.
    graph2: networkx Graph object.
    Returns
    -------
        bool
        True is graph1 and graph 2 are isomorphic.
    """
    return nx.is_isomorphic(graph1, graph2,
                            node_match=iso.categorical_node_match(
                                'element', 'C'),
                            edge_match=iso.categorical_edge_match('weight', 1))

def check_iso_arrays(array1, array2):
    
    has_iso1 = np.full(len(array1), False)
    has_iso2 = np.full(len(array2), False)
    
    for count1, i in enumerate(array1):
        for count2, j in enumerate(array2):
            if check_iso(i,j):
                has_iso1[count1] = count2
                has_iso2[count2] = count1
                
    return has_iso1, has_iso2

def update_X_descriptors(X, descriptors, graphs):
    """Updates coefficient matrix with counts of graph descriptors
    and creates new column for descriptor not seen before.
    Parameters
    ---------
    X: list
        Coefficient matrix with each row for  a molecule and
        each column for a coefficient of descriptor in molecule
    descriptor: list
        Unique graphs which form basis set of molecule expansion
    graphs: list
        Subgraphs of a molecule.
    Returns
    -------
        list, list
    (updated) X, descriptors
    """
    row_entry = list()
    row_entry.extend([0] * len(descriptors))
    for graph in (graphs):
        graph_classified = False # if graph has been assigned a descriptor
        for index, descriptor in enumerate(descriptors):
            if not len(descriptor.nodes()) == len(graph.nodes()) or \
                    not len(descriptor.edges()) == len(graph.edges()):
                continue
            if check_iso(graph, descriptor):
                row_entry[index] +=1
                graph_classified = True
                break  # stop going thru descriptors
        if not graph_classified:
            # graph is a descriptor not seen previously
            descriptors.append(graph)
            row_entry.append(1)
    X.append(row_entry)
    
    return X, descriptors

def get_subgraphs(G, max_graph_length=5):
    
    if not max_graph_length:
        max_graph_length = G.number_of_nodes()
    
    all_connected_subgraphs = []
    for nb_nodes in range(1, max_graph_length+1):
        for SG in (G.subgraph(selected_nodes) for selected_nodes in itertools.combinations(G, nb_nodes)):
            if nx.is_connected(SG):
                all_connected_subgraphs.append(SG)
            
    return all_connected_subgraphs

def get_graph_descriptors(graphs, max_graph_length=5):
    
    X,descriptors = list(), list()
    
    if not max_graph_length:
        max_graph_length = max([len(i.nodes()) for i in graphs])
    
    for count, graph in enumerate(graphs):
        
        print('Enumerating subgraphs in graph ', count)
        
        subgraphs = get_subgraphs(graph, max_graph_length = max_graph_length)
        
        X, descriptors = update_X_descriptors(X=X, descriptors=descriptors, graphs=subgraphs)
        
        assert len(X[-1]) == max([len(row) for row in X])
        
        def complete_rows(n):
            """ Given a 2D array, make it a square,
            i.e. make all rows of length n by padding
            the missing entries with zero.
            Parameters
            ----------
            n: int
                Size of max row.
            Returns
            -------
                list
                Squared matrix
            """
            X_out = []
            for row in X:
                row.extend([0] * (n - len(row)))
                # row_entry.extend([0] * len(descriptors))
                X_out.append(row)
            return X_out
        
        X = complete_rows(n=len(X[-1]))
    
    return X, descriptors