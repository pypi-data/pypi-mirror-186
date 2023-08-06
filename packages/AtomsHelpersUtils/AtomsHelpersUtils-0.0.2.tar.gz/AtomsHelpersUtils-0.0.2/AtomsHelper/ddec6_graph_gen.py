# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 02:57:28 2023

@author: eccn3
"""

import networkx as nx
import itertools
import numpy as np
import re
import time
import copy
import sys

from itertools import combinations_with_replacement

import matplotlib.pyplot as plt

def gen_graph_ddec6(directory = None, bader = False):

    if directory:
        import os
        os.chdir(directory)
    
    periodic = np.array([p for p in itertools.product([-1, 0, 1], repeat=3)])

    ads_atoms = ['adsorbate', 'adsorbate surface coordinated']    
    nac = open('DDEC6_even_tempered_net_atomic_charges.xyz')
    
    graph = nx.Graph()
    
    num_atoms = int(next(nac))
    next(nac)
    
    metals = ['Pt', 'Ni', 'Pd', 'Ir']
    
    for count, i in enumerate(itertools.islice(nac, num_atoms)):
        
        element, x, y, z, charge = i.split()
        if count == 0:
            if element in metals:
                graph.graph['surface']=element
            else:
                graph.graph['surface']='gas'
        if any(element == i for i in metals):
            typ = 'slab'
        else:
            typ = 'adsorbate'
        
        graph.add_node(count,
                       element = element,
                       system_type = typ,
                       position = [float(x),float(y),float(z)],
                       charge = float(charge))

    bo = open('DDEC6_even_tempered_bond_orders.xyz')
    next(bo)
    
    cell_text = next(bo)
    cell_text_split = re.split('[{}]', cell_text)
    
    cell_x = np.array([float(i) for i in cell_text_split[3].split()])
    cell_y = np.array([float(i) for i in cell_text_split[5].split()])
    cell_z = np.array([float(i) for i in cell_text_split[7].split()])                  
    
    cell_dims = np.vstack([cell_x, cell_y, cell_z])
    
    for count, i in enumerate(itertools.islice(bo, num_atoms)):
        element, x, y, z, total = i.split()
        
        position = [float(i) for i in [x,y,z]]
        
        if graph.nodes[count]['position'] == position:
            graph.nodes[count]['bond_order_total'] = float(total)
        else:
            print(count, "Uh oh it doesn't match up")
    
    for i in bo:
        if 'Printing BOs for ATOM #' in i:
            index = int(i.split()[5])-1
            next(bo)
            j=next(bo)
            while 'Bonded to the' in j:
                j_split = j.split()
                
                weight = float(j_split[20])
     
                index2 = int(j_split[12])-1
                

                periodic_img_pos = graph.nodes[index2]['position'] + np.matmul(periodic, cell_dims)
                
                distance = np.min(np.linalg.norm(np.subtract(graph.nodes[index]['position'],
                                       periodic_img_pos), axis = 1))
                
                
                graph.add_edge(index, index2, 
                               weight = weight,
                               distance = distance)

                j = next(bo)
    if bader:
        graph = bader_charge_assign(graph)
    return graph

def bader_charge_assign(graph):
    
    bader_infos = np.array([])
    try:
        bader_charge = open('ACF.dat')
    except:
        print('No ACF.dat detected. Bader charges not assigned.')
        return 

    next(bader_charge)
    next(bader_charge)
    i = next(bader_charge)
    bader_infos = np.array([float(j) for j in i.split()][1:5])
    
    i = next(bader_charge)
    
    
    while '-----' not in i:
         bader_infos = np.vstack([bader_infos, np.array([float(j) for j in i.split()][1:5])])
         i = next(bader_charge)
    
    bader_pos = bader_infos[:, :3]
    bader_cha = bader_infos[:, 3]

    for i in graph.nodes:
        node_pos = graph.nodes[i]['position']
        dist_crd = bader_pos - node_pos
        dist_vec = np.linalg.norm(dist_crd, axis = 1)
        closest = np.argmin(dist_vec)
        graph.nodes[i]['bader charge'] = bader_cha[closest]

    return graph

if __name__=='__main__':
    
    graph = gen_graph_ddec6('Examples')
    