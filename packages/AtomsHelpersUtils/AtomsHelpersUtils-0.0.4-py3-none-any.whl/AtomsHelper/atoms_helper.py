# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 13:23:21 2022

@author: eccn3
"""

import networkx as nx
import numpy as np
import copy
import itertools
import matplotlib.pyplot as plt
import pyomo.environ as pe
import pyomo.opt as po

import ipopt_wrapper

from ase.build import fcc111
from ase.data import atomic_numbers, covalent_radii

import pysmiles

from ase.io import read
from ase.visualize import view

class geom2graph:
    
    """
    
    Object containing vasp structure - to - networkx conversion
    
    :vasp: file location of structure to convert
    
    """
    
    def __init__(self, surface_type = 'Pt', vasp = None, atoms = None, solver = 'mindtpy', distance_tune = 1.2, H_dist = 2.75):
        
        self.surface_type = surface_type
        self.solver = solver            
        self.vasp = vasp    
        self.atoms = atoms
        self.distance_tune = distance_tune
        self.H_dist = H_dist
        
        self.get_atoms()
        self.elements = ['H','O','N','C',surface_type]
        
        self.gen_distance_dict()
        self.get_edge_dict()
        self.graph = None
    
    def gen_distance_dict(self):
        
        """
        Generates:
            self.element_distances: cutoff bounds per element as 
            self.distance_bound: cutoff bound per pair of elements. 
        
        """
        
        self.element_distances = dict()
        for i in self.elements:
            self.element_distances[i] = covalent_radii[atomic_numbers[i]] * self.distance_tune
        
        d1 = dict.fromkeys(self.elements)
        
        self.distance_bounds = dict.fromkeys(self.elements)
        
        for i in self.elements:
            self.distance_bounds[i] = copy.deepcopy(d1)
            for j in self.elements:
                self.distance_bounds[i][j] = self.element_distances[i] + self.element_distances[j]
        
    def get_atoms(self):
        
        # Generates:
            # self.symbols: array of each atom's symbol, in order of the self.atoms ASE atoms object
            # self.adsorbate_atoms: array of atom indices whose symbols are not that of the surface
                # TODO: better way to identify adsorbate; what about oxide surfaces?
            # self.positions: array of 3d arrays for each self.atom ASE atom object's atom positions

            # Additionally, if self.adsorbate_atoms is not empty, will center the 
            # self.atoms object around the lowest adsorbate atom (z-axis)
        
        if self.vasp:
            self.atoms = read(self.vasp)
            
        self.symbols = []
        for atom in self.atoms:
            self.symbols.append(atom.symbol)
            
        self.symbols = np.array(self.symbols)
        self.adsorbate_atoms = (self.symbols != self.surface_type).nonzero()[0]
        
        if len(self.adsorbate_atoms)>0:
            self.center_adsorbate()
        
        self.positions = []
        
        for atom in self.atoms:
            self.positions.append(atom.position)
            
        self.positions = np.array(self.positions)
        self.symbols = np.array(self.symbols)

      
    def center_adsorbate(self):
        
        # Routine to center the self.atoms object about the lowest adsorbate atom
        
        lowest = 100

        for i in self.adsorbate_atoms:
            if self.atoms[i].position[2] < lowest:
                lowest = self.atoms[i].position[2]
                center_about = self.atoms[i].position
        
        self.atoms = self.center(self.atoms, center_about)
        
    def center(self, atoms, about, wrap = True):
        
        # In:   *atoms: ASE atoms object* to center; 
        #       *about: 3D array* centroid to center around; 
        #       *wrap: boolean" to wrap atoms back within cell
        
        # Out:  *atoms object* centered. 
        
        cell_center = sum(atoms.cell)/2
        
        move = cell_center - about
        
        atoms.positions += [move[0], move[1], 0]
        
        if wrap:    
            atoms.wrap()
        
        return atoms
    
    def get_edge_dict(self, ):
        
        # Generates a dictionary of edges based on distances, from the adsorbate atom
        
        distances = []
        
        self.edge_dict = {}
        for i in self.adsorbate_atoms:
            
            symbol1 = self.symbols[i]
            
            r = self.positions - self.positions[i]
            distance = np.linalg.norm(r, axis = 1)
            
            distances.append(distance)
            
            neighbor = self.get_neighbors(distance, symbol1)
            
            self.edge_dict[i] = copy.deepcopy(neighbor)
        self.graph_atoms = set(itertools.chain.from_iterable(self.edge_dict.values()))
        self.active_site = list(self.graph_atoms-set(self.adsorbate_atoms))
        self.graph_atoms = list(self.graph_atoms)
                
    def get_neighbors(self, distance, symbol):
        
        # In:
            # *distance: 1D array* distance list of all other atoms in the ase.atoms object
            # *symbol: string* of what the element is. Used for indexing into the self.bounds
        
        if symbol == 'H':
            neighbor = int(np.argsort(distance)[1])

            return [neighbor]
            
        else:
            neighbor = self.find_neighbors(symbol, distance, self.distance_bounds)
        
        return neighbor
    
    def find_neighbors(self, symbol, distance, radii):
            
            neighbors = []
            
            closest = np.argsort(distance)
            
            for i in closest[1:]:
                
                if distance[i]>3.1:
                    return neighbors
                
                else: 
                    if distance[i] < radii[symbol][self.symbols[i]]:
                        neighbors.append(i)
                        
            return neighbors
    
    def add_h_surf_bonds(self):
        
        dist_H_surf = copy.deepcopy(self.distance_bounds)
        dist_H_surf['H'][self.surface_type] = self.H_dist
        dist_H_surf[self.surface_type]['H'] = self.H_dist
        
        for i in self.adsorbate_atoms:
        
            if self.symbols[i] =='H':
                r = self.positions - self.positions[i]
                distance = np.linalg.norm(r, axis = 1)
                neighbor = self.find_neighbors(self.symbols[i], distance, radii = dist_H_surf)
        
                for j in neighbor:
                    if self.symbols[j] == self.surface_type:
                    
                        self.edge_dict[i].append(j)
                        
                        if self.graph:
                            
                            if j not in self.graph.nodes:
                            
                                self.graph.add_node(j, element= self.surface_type, valency = 99, edges = 1, unoccupied = 98)
                            self.graph.add_edge(i,j, weight = 0)
    
    def get_gcn(self):
        
        # Returns Generalized Coordination Number 
        
        self.active_site_nn = self.find_active_site_x_nearest_neighbors()
        
        sum_cn = 0
        
        if not self.active_site:
            self.gcn = 0
            return
        
        for i in self.active_site_nn[1]:
            n = set(self.find_nearest_neighbors([i])) - set(self.adsorbate_atoms)
            sum_cn += len(n)
        
        bot_slab = fcc111(self.surface_type, (10,10,5), periodic = True)
        cell_center = np.median(bot_slab.positions, axis = 0)
        
        active_site_poss = self.atoms[self.active_site].positions
        active_site_center = np.mean(self.atoms[self.active_site].positions, axis = 0)        
        
        closest_active_site_to_center = np.argmin(np.linalg.norm(active_site_poss - active_site_center, axis = 1))
        
        new_coords = active_site_poss - active_site_poss[closest_active_site_to_center] + cell_center
        
        slab_ind = np.array([])
        
        for i in new_coords:
            slab_ind = np.append(slab_ind, np.argmin(np.linalg.norm(i-bot_slab.positions, axis = 1))).astype(int)
        
        slab = geom2graph(atoms = bot_slab, surface_type = self.surface_type)
        slab.active_site = slab_ind
        slab.active_site_nn = slab.find_active_site_x_nearest_neighbors()
        
        for i in slab_ind:
            slab.atoms[i].symbol = 'O'
            
        self.helper_gcn = slab
        
        cn_max = len(slab.active_site_nn[1])
        
        self.gcn = sum_cn / cn_max
        
        return
        
    def find_nearest_neighbors(self, atoms):
        
        # in:   'list' of 'atoms indices' to find the first-nearest neighbors of
        # out:  'list' of 'atoms indices' that are first-nearest neighbors of input atoms
        
        distances = []
        
        n = []
        
        for i in atoms:
            atoms_shift = self.center(self.atoms, self.atoms[i].position)
            symbol1 = self.symbols[i]
            r = atoms_shift.positions - atoms_shift.positions[i]
            distance = np.linalg.norm(r, axis = 1)
            distances.append(distance)
            neighbor = self.get_neighbors(distance, symbol1)
            n.append(neighbor)
            
        n = [i for j in n for i in j]
        
        
        if len(self.adsorbate_atoms)>0:
            self.center_adsorbate()
        
        return n
    
    def find_active_site_x_nearest_neighbors(self, nn_degree = 1):
        
        active_site_nn = {}
        for i in np.arange(1, nn_degree+1):
            
            if i == 1:
                active_site_nn[i] = set(self.find_nearest_neighbors(self.active_site)) - set(self.active_site) - set(self.adsorbate_atoms)
                
            if i == 2:
                
                active_site_nn[i] = set(self.find_nearest_neighbors(active_site_nn[i-1])) - set(self.active_site) - set(self.adsorbate_atoms)
                for j in np.arange(1, i):
                    active_site_nn[i] = active_site_nn[i] - active_site_nn[j]-set(self.adsorbate_atoms)
                    
        for i in active_site_nn.keys():
            active_site_nn[i] = list(active_site_nn[i])
            
        return active_site_nn
    
        
    def gen_graph(self, h_surface = False, fill_bonds = True):
        
        # Create graph from subgraph, giving each node a name by index
        
        valency = {'H': 1, 'O': 2, 'N': 3, 'C': 4, self.surface_type: 99}
        
        self.graph = nx.Graph(bonds_solved = 'solved')
        
        allvals = self.edge_dict.values()
        
        flat_list = set([item for sublist in allvals for item in sublist]).union((set(self.edge_dict.keys())))
        
        for i in flat_list:
        
            self.graph.add_node(i)
            self.graph.nodes[i]['element'] = self.symbols[i]
            
        for i in self.edge_dict.keys():
            for j in self.edge_dict[i]:
                
                if {self.graph.nodes[i]['element'], self.graph.nodes[j]['element']} == {'H', self.surface_type}:
                    self.graph.add_edge(i,j, weight = 0)
                else:
                    self.graph.add_edge(i,j, weight = 1)

        for node in self.graph.nodes:    
            self.graph.nodes[node]['valency'] = valency[self.graph.nodes[node]['element']]
            self.graph.nodes[node]['edges'] = len(self.graph.edges(node))
            self.graph.nodes[node]['unoccupied'] = self.graph.nodes[node]['valency'] - self.graph.nodes[node]['edges']
          
        if not fill_bonds:
            return
            
        model, results = self.fill_bonds()
        if not model:
            return
        
        self.solver_results = {'model': model, 'results': results}
        
        if self.solver_results['model']:
            
            for index in model.edge_weights_ads:
                self.graph.edges[index]['weight'] = int(model.edge_weights_ads[index].value)
                
            if self.surface_type in [self.graph.nodes[i]['element'] for i in self.graph.nodes]:
                
                edges_pt_dict = {i: model.edge_weights_pts[i].value for i in model.edge_weights_pts}          
                nodes = set([i for sub in model.edges_pts for i in sub])
                not_pt_nodes = [i for i in nodes if self.symbols[i] != self.surface_type]
                
                edge_pt_ads_sort = dict.fromkeys(not_pt_nodes, {})
                
                for index in model.edge_weights_pts:
                    intersection = set(index).intersection(not_pt_nodes)
                    if intersection:
                        edge_pt_ads_sort[list(intersection)[0]][index] = model.edge_weights_pts[index].value
                        
                for node in edge_pt_ads_sort:
                    
                    edge_sum = 0
                    edges= 0
                    
                    for edge in edge_pt_ads_sort[node]:
                        edge_sum += edge_pt_ads_sort[node][edge]
                        edges += 1
                    edge_sum = edge_sum/edges
                    
                    for edge in edge_pt_ads_sort[node]:
                        edges_pt_dict[edge] = edge_sum
                
                for index in edges_pt_dict: 
                    self.graph.edges[index]['weight'] = round(edges_pt_dict[index],3)
                
            
        else:
            # for index in self.graph.edges:
            #     self.graph.edges[index]['weight'] = 'N/A'
                
            self.graph.graph['bonds_solved'] = "Problem with solver"


    def fill_bonds(self):
        
        node_dict = dict(self.graph.nodes)
    
        edges_ads, edges_pts, edges_hs, nodes_ads, nodes_pts, nodes_hs= {}, {}, {}, {}, {}, {}
        
        # Sort edges into surface and adsorbate
        for edge in self.graph.edges:
            
            if 'H' in self.symbols[[edge]]:
                edges_hs[edge] = self.graph.edges[edge]['weight']
            
            elif self.surface_type in self.symbols[[edge]]:
                    edges_pts[edge] = self.graph.edges[edge]['weight']
                    
            else:
                edges_ads[edge] = self.graph.edges[edge]['weight']
        
        # Sort nodes into surface and adsorbate
        for node in self.graph.nodes:
            
            if self.symbols[node]==self.surface_type:
                nodes_pts[node] = node_dict[node]['valency']
            elif self.symbols[node] == 'H':
                nodes_hs[node] = node_dict[node]['valency']
            else:
                nodes_ads[node] = node_dict[node]['valency']

        if not edges_ads and not edges_pts:
            return None, None
        
        model = pe.ConcreteModel()
        
        model.nodes_ads = pe.Set(initialize = list(set(nodes_ads.keys())))
        model.nodes_hs = pe.Set(initialize = list(set(nodes_hs.keys())))
        model.edges_ads = pe.Set(initialize = list(set(edges_ads.keys())))
        model.edges_hs = pe.Set(initialize = list(set(edges_hs.keys())))
        
        model.edge_weights_ads = pe.Var(model.edges_ads, 
                                        within = pe.PositiveIntegers,
                                        initialize = {i: 2 for i in model.edges_ads},
                                        bounds = (1, 4))
        
        model.edge_weights_hs = pe.Param(model.edges_hs,
                                         initialize = {i: 1 for i in model.edges_hs})
        
        model.valency = pe.Param(model.nodes_ads, 
                                 initialize = nodes_ads, 
                                 within=pe.PositiveIntegers)
        
        
        if len(nodes_pts)>0:
            
            model.nodes_pts = pe.Set(initialize = list(set(nodes_pts.keys())))
            model.edges_pts = pe.Set(initialize = list(set(edges_pts)))
            model.edge_weights_pts = pe.Var(model.edges_pts, 
                                            within = pe.PositiveReals,
                                            initialize ={i: 1 for i in model.edges_pts},
                                            bounds = (0.01, 4))
        
            def valency_cap(model, i):
                
                edge_sum = 0
                
                if edges_ads:
                    edge_sum += sum([model.edge_weights_ads[j] for j in model.edge_weights_ads if i in j]) 
                if edges_hs:
                    edge_sum += sum([model.edge_weights_hs[j] for j in model.edge_weights_hs if i in j])
                if edges_pts:
                    edge_sum += sum([model.edge_weights_pts[j] for j in model.edge_weights_pts if i in j])
                
                return model.valency[i] == edge_sum
                       
        
            def edge_sum(model):
                
                total_ads = sum([(model.edge_weights_ads[i]) for i in model.edges_ads])
                total_pts = sum([(model.edge_weights_pts[i]) for i in model.edges_pts])
                
                total = total_ads + total_pts
                
                return total
            
        else:
            
            def valency_cap(model, i):
            
                node_in_edge_ads = sum([model.edge_weights_ads[j] for j in model.edge_weights_ads if i in j])
                node_in_edge_hs = sum([model.edge_weights_hs[j] for j in model.edge_weights_hs if i in j])
                
                return model.valency[i] == node_in_edge_ads + node_in_edge_hs
                       
            
            def edge_sum(model):
                
                return sum([(model.edge_weights_ads[i]) for i in model.edges_ads])



        model.obj = pe.Objective(sense = pe.maximize, rule = edge_sum)


        constraint_node_ads = set([i for sub in model.edges_ads for i in sub])
        
        if edges_pts:
            constraint_nodes_pts = set([i for sub in model.edges_pts for i in sub])
            constraint_nodes = [i for i in constraint_nodes.union(constraint_nodes_pts) if self.symbols[i] != self.surface_type]
        
        model.con = pe.Constraint(constraint_nodes, rule = valency_cap)

        solver = po.SolverFactory('glpk')
        
        try:
            print('Solving ' + str(self.atoms[self.adsorbate_atoms].symbols))
            results = solver.solve(model)
                
        except:
            print('Solver unable to get solution')
            model = None
            results = None
        
        return model, results

    def draw_graph(self, cutoff = 0.3, 
                        node_label_type = 'element', edge_labels = False, edge_label_type = 'weight'):
        
        from utils import draw_surf_graph
        draw_surf_graph(self.graph, cutoff = cutoff, 
                            node_label_type = node_label_type, edge_labels = edge_labels, edge_label_type = edge_label_type)
        
    def get_SMILES_string(self):    
        self.smiles_string = pysmiles.write_smiles(self.graph)

        
    def generalize_graph_metal(self):
        if not self.graph:
            print('No graph generated')
            return
        
        for n in self.graph.nodes(data=True):
            if self.graph.nodes[n[0]]['element'] == self.surface_type:
                self.graph.nodes[n[0]]['element']='M'
        
if __name__=="__main__":
    # vasp = geom2graph(vasp = 'Examples/ase_to_graph/CONTCARmethane')
    # vasp = geom2graph(vasp = 'Examples/ase_to_graph/CONTCARpraneetalphahdown')
    # vasp = geom2graph(vasp = 'Examples/ase_to_graph/CONTCAR_CHCH_holhol')
    vasp = geom2graph(vasp = 'Examples/ase_to_graph/CONTCAR_Ir_CH3_hol', surface_type = 'Ir')
    
    # vasp.find_active_site_x_nearest_neighbors(2)
    
    # for i in vasp.active_site_nn[2]:
    #     vasp.atoms[i].symbol = 'Al'
    # for i in vasp.active_site_nn[1]:
    #     vasp.atoms[i].symbol = 'Au'
    vasp.add_h_surf_bonds()
    vasp.gen_graph()
    vasp.get_SMILES_string()
    print(vasp.smiles_string)
    vasp.get_gcn()
    print(vasp.gcn)
    
    vasp.draw_graph(edge_labels=True)
