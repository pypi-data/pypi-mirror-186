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
        
        bot_slab = fcc111(self.surface_type, (10,10,3), periodic = True)
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
        
        self.solver_results = {'model': model, 'results': results}
        
        if self.solver_results['model']:
            
            for index in model.edge_weights_ads:
                self.graph.edges[index]['weight'] = int(model.edge_weights_ads[index].value)
                
            if self.surface_type in [self.graph.nodes[i]['element'] for i in self.graph.nodes]:
                for index in model.edge_weights_pts:
                    self.graph.edges[index]['weight'] = round(model.edge_weights_pts[index].value,3)
            
            
        else:
            # for index in self.graph.edges:
            #     self.graph.edges[index]['weight'] = 'N/A'
                
            self.graph.graph['bonds_solved'] = "Problem with solver"


    def fill_bonds(self):
        
        node_dict = dict(self.graph.nodes)
    
        edges_ads, edges_pts, nodes_ads, nodes_pts = {}, {}, {}, {}
        
        # Sort edges into surface and adsorbate
        for edge in self.graph.edges:
            
            if self.symbols[edge[0]] == self.surface_type or self.symbols[edge[1]] == self.surface_type:
                if self.symbols[edge[0]] != 'H' and self.symbols[edge[1]] != 'H':
                    edges_pts[edge] = self.graph.edges[edge]['weight']
                    
                else:
                    continue
                    
            else:
                edges_ads[edge] = self.graph.edges[edge]['weight']
        
        # Sort nodes into surface and adsorbate
        for node in self.graph.nodes:
            if self.symbols[node]==self.surface_type:
                nodes_pts[node] = node_dict[node]['valency']
            else:
                nodes_ads[node] = node_dict[node]['valency']

        
        model = pe.ConcreteModel()
        
        model.nodes_ads = pe.Set(initialize = list(set(nodes_ads.keys())))
        model.edges_ads = pe.Set(initialize = list(set(edges_ads.keys())))
        
        model.edge_weights_ads = pe.Var(model.edges_ads, 
                                        within = pe.PositiveIntegers,
                                        initialize = {i: 2 for i in model.edges_ads},
                                        bounds = (1, 4))
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
            
                edge_sum = sum([sum([model.edge_weights_ads[j] for j in model.edge_weights_ads if i in j]),
                                  sum([model.edge_weights_pts[j] for j in model.edge_weights_pts if i in j])])
                
                constraint = edge_sum == model.valency[i]
                       
                return constraint
        
            def tighten_bonds_to_1_1(model):
                
                total2 = sum([(model.edge_weights_pts[i]-1)**2 for i in model.edges_pts])
                total1 = sum([(model.edge_weights_ads[i]-1)**2 for i in model.edges_ads])
                total= total1+total2
                return total
            
            model.obj = pe.Objective(sense = pe.minimize, rule = tighten_bonds_to_1_1)
            model.con = pe.Constraint(model.nodes_ads, rule = valency_cap)
            
        else:
            
            # def valency_cap(model, i):
            
            #     edge_sum = sum([model.edge_weights_ads[j] for j in model.edge_weights_ads if i in j])
                                 
            #     constraint = edge_sum == model.valency[i]
                       
            #     return constraint
            
            # def valency_cap(model, i):
            
            #     edge_sum = sum([model.edge_weights_ads[j] for j in model.edge_weights_ads if i in j])
            #     constraint = edge_sum == model.valency[i]
                       
            #     return constraint
            
            def tighten_bonds_to_1_1(model):
                
                total = sum([(model.edge_weights_ads[i]-1)**2 for i in model.edges_ads])
                return total


            model.obj = pe.Objective(sense = pe.minimize, rule = tighten_bonds_to_1_1)
            # model.con = pe.Constraint(model.nodes_ads, rule = valency_cap)
            
            
            
        solver = po.SolverFactory('ipopt')
        
        # try:
        print('Solving ' + str(self.atoms[self.adsorbate_atoms].symbols))
        results = solver.solve(model)
            
        # except:
        #     print('Solver unable to get solution')
        #     model = None
        #     results = None
        
        return model, results

    def draw_graph(self):
        
        
        """
        Displays the graph
        :param graph: networkx graph object
        :return: None
        """
        
        nodes = self.graph.nodes()
        
        xs = np.linspace(-0.7, 0.7, len(nodes))
        
        positions = {i: (xs[count], np.random.uniform(low = -0.5, high = 1)) for count, i in enumerate(nodes)}
        
        Pt = [i for i in nodes if self.symbols[i] == self.surface_type]
        
        if len(Pt) ==1:
            spaced = (0,-1)
            positions[Pt[0]] = spaced
            fixed_positions = {Pt[0]: tuple(spaced)}
            pos = nx.spring_layout(self.graph, pos = fixed_positions, fixed = fixed_positions, weight=None)
            
        elif len(Pt)>1:
            spaced = np.vstack((np.linspace(-0.95, 0.95, len(Pt)), np.ones(len(Pt))*-1)).T
            for count, i in enumerate(Pt):
                positions[i] = tuple(spaced[count])
            fixed_positions = {i: tuple(spaced[count]) for count, i in enumerate(Pt)}
        
            pos = nx.spring_layout(self.graph, pos = positions, fixed = fixed_positions, weight=None)
            
        
        else:
            pos = nx.spring_layout(self.graph, pos = positions, weight=None)
        
        nx.draw(self.graph, with_labels=False, node_size=1000, node_color="skyblue",
                node_shape="o", alpha=0.5, linewidths=4, font_size=15,
                font_color="black", font_weight="bold", width=2, edge_color="grey",
                pos=pos)
        node_labels = nx.get_node_attributes(self.graph, 'element')
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_labels(self.graph, pos, node_labels)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels)
        plt.show()
        
    def get_SMILES_string(self):
        
        self.smiles = pysmiles.write_smiles(self.graph)
        print(self.smiles)
        
    def generalize_graph_metal(self):
        if not self.graph:
            print('No graph generated')
            return
        
        for n in self.graph.nodes(data=True):
            if self.graph.nodes[n[0]]['element'] == self.surface_type:
                self.graph.nodes[n[0]]['element']='M'
        
# if __name__=="__main__":
#     # vasp = geom2graph(vasp = 'vasp_to_network_tests/CONTCARmethane')
#     vasp = geom2graph(vasp = 'vasp_to_network_tests/CONTCARpraneetalphahdown')
#     vasp = geom2graph(vasp = 'vasp_to_network_tests/CONTCARCCH2CH3ont')
    
#     # vasp.find_active_site_x_nearest_neighbors(2)
    
#     # for i in vasp.active_site_nn[2]:
#     #     vasp.atoms[i].symbol = 'Al'
#     # for i in vasp.active_site_nn[1]:
#     #     vasp.atoms[i].symbol = 'Au'
#     # vasp.add_h_surf_bonds()
#     vasp.gen_graph()
#     # vasp.get_SMILES_string()
#     # vasp.get_gcn()
#     vasp.draw_graph()
