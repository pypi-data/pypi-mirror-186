# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 13:08:02 2022

@author: eccn3
"""

import pandas as pd
import numpy as np
import copy
import matplotlib.pyplot as plt

import networkx as nx

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

from itertools import compress

def draw_surf_graph(graph, cutoff = 0.3, 
                    node_label_type = 'element', edge_labels = False, edge_label_type = 'weight'):
   
    graph = remove_small_edges(graph, cutoff = cutoff)

    plt.figure(figsize=(6,5))
   
    metals = ['Ni', 'Ir','Pd','Pt']
   
    colors = {'Ni': [52/255, 235/255, 91/255],
              'Ir': [58/255, 173/255, 194/255],
              'Pd': [64/255, 127/255, 222/255],
              'Pt': [177/255, 185/255, 196/255],
              'C': [127/255, 131/255, 138/255],
              'H': [200/255, 200/255, 200/255],
              'O': [200/255, 0, 0],
              'N': [0.5,0.5,200/255]}    

    for i in colors.keys():
        colors[i] = np.array(colors[i]).reshape(1,-1)              
             
   

    element_count = {i: [] for i in colors.keys()}

    for i in nx.get_node_attributes(graph, 'element').items():
        element_count[i[1]].append(i[0])
   
    init_pos = nx.get_node_attributes(graph, 'element')
   
    for i in init_pos.keys():
        if any([init_pos[i] ==j for j in metals]):
            init_pos[i] = [np.random.uniform(),0.05 +0.1* np.random.uniform()]
        else:
            init_pos[i] = [np.random.uniform(), 0.85 +0.1* np.random.uniform()]
   
    pos = nx.spring_layout(graph,pos=init_pos)    
       
       
    system_count = {'metal surface coordinated': [], 'adsorbate surface coordinated': []}
    keys = system_count.keys()
    for i in nx.get_node_attributes(graph, 'system_type').items():
        if any([i[1] == j for j in keys]):
            system_count[i[1]].append(i[0])
           
           
    options = {"edgecolors": "tab:cyan"}
    for i in system_count.keys():    
        nx.draw_networkx_nodes(graph, pos, nodelist = system_count[i],node_size=400, **options)
       
    for i in element_count.keys():
        if not element_count[i]:
            continue
        if any(i==j for j in ['Ni', 'Ir', 'Pd','Pt']):
            nx.draw_networkx_nodes(graph, pos, nodelist=element_count[i],node_size=100, node_color = colors[i])
        else:
            nx.draw_networkx_nodes(graph, pos, nodelist=element_count[i],node_size=250, node_color = colors[i])

       
       
    nx.draw_networkx_edges(graph, pos, alpha = 0.5)
   
    labels = nx.get_node_attributes(graph, node_label_type)
    nx.draw_networkx_labels(graph, pos, labels)
    
    if edge_labels:
        ed_labels = nx.get_edge_attributes(graph, edge_label_type)
        nx.draw_networkx_edge_labels(graph, pos, ed_labels)
    # plt.close()

def remove_small_edges(graph, cutoff = 0.3):
    small_weights = []

    for i in graph.edges():
        if graph.edges[i]['weight'] < cutoff:
            small_weights.append(i)
            
    copy_graph = copy.deepcopy(graph)
    for i in small_weights:
        copy_graph.remove_edge(*i)

    return copy_graph

def data_keep(X, X_names, idx):
    return X[:, idx], X_names[ idx]

def correlation(df, threshold):
    # try:
    #     y = df[response]
    #     df = df.drop(response, axis = 1)
    # except:
    #     pass
    cor_matrix = df.corr().abs()
    upper_tri = cor_matrix.where(np.triu(np.ones(cor_matrix.shape),k=1).astype(np.bool))
    to_drop = [column for column in upper_tri.columns if any(upper_tri[column] > threshold)]
    print(to_drop)
    df1 = df.drop(to_drop, axis=1)
    # df1 = df1.assign(response = y)
    return df1

def number_select(df, column):
    
    # Selects only rows that have a TYPE NUMBER in specified column
    
    # Input: df = df to search; column = 
    
    df1 = df[pd.to_numeric(df[column], errors='coerce').notnull()]
    
    
    return df1

def match(df1, df2, feature, substrate = True):
    
    # Iterates through df1: looks at adsorbate, substrate, and site combination
    # Find matches in df2 for adsorbate/substrate/site combination to grab its energy
    
    if feature in list(df1.columns):
        newfeat = feature + ' 2'
    
    else:
        newfeat = feature
    
    df1[newfeat] = np.nan
    
    if not substrate:
        for count, i in df1.iterrows():
            comparison_column = (df2[['Adsorbate', 'Site']] == i[['Adsorbate', 'Site']]).all(axis = 1)
            if any(comparison_column):
                df1.at[count, newfeat] = df2[feature][comparison_column].to_numpy()
            
    else:
        for count, i in df1.iterrows():
            comparison_column = (df2[['Adsorbate', 'Site', 'Substrate']] == i[['Adsorbate', 'Site', 'Substrate']]).all(axis = 1)
            if any(comparison_column):
                df1.at[count, newfeat] = df2[feature][comparison_column].to_numpy()
    
    df1 = df1.dropna()

    return df1

def plot_parity(x, y, label = None, alp = 0.75):

    # Plots scatter parity between x and y, with label if desired
    # In: x = x-axis data; y = y-axis data; label = scatter label; alp = alpha for dots
    # Out: scatter plot

    if not label:
        l = 'Parity'

    else:
        l = label

    plt.scatter(x, y, alpha = alp, label = l)
    minx = min(x)-abs(min(x)*0.25)
    miny = min(y)-abs(min(y)*0.25)
    maxx = max(x)+abs(max(x)*0.25)
    maxy = max(y)+abs(max(y)*0.25)
    
    
    minimum = min(minx, miny)
    maximum = max(maxx, maxy)
    
    plt.ylim(minimum, maximum)
    plt.xlim(minimum, maximum)
    plt.plot([minimum,maximum], [minimum, maximum], alpha = 0.5)

def plot_hist(X):
    plt.hist(x=X, bins='auto', rwidth=0.85, label = "Difference in Eads")


def print_results(models, model_selects, model_data, y= []):
    
    # Print results for your fitting. Companion to test_fit
    # In: models = list of models; model_selects = splitting methods used; 
        # model_data = fit results; y = response targets
    # Out: prints for Mean Absolute Error values
    
    if y!=[]:
        MAD = np.round(np.mean(abs(y)),3)
        MADstdev = np.round(np.std(y),3)
    
        print('Mean Absolute Error = ' + str(MAD))

        print('Difference Stdev = ' + str(MADstdev) + '\n')
    
    model_names = [type(i).__name__ for  i in models]
    
    for count, i in enumerate(model_data):
        print(model_names[count])
        MAEs = [np.round(j['MAE'],3) for j in i]
        print('MAEs: ', MAEs)
        StDs = [np.round(np.mean(j['Error Stdev']),3) for j in i]
        print('Error Stdev = ' + str(StDs))
        StDs = [np.round(np.mean(j['Coef Stdevs']),3) for j in i]
        print('Coef Stdevs: ', StDs)
        print()

def plot_across_modelselects(models, feature, percents):
    
    # Plots a feature across model selection methods
    # In: models = results of fittings; feature = what to plot across models; 
        # percents = x-axis data, usually percent of data learned on
        
    # Out: plot of feature versus percent-learned on
    
    y = [i[feature] for i in models]
    stdev = [np.std(i['Errors']) for i in models]
    plt.figure()
    plt.errorbar(percents, y, yerr = stdev)
    
    plt.ylabel(feature)
    plt.xlabel('Percent of Dataset Learned On')
    
    plt.title('Learning Curve')


def drop(df, adsorbate, site):
    
    # Drop from df, based on adsorbate and site. And sensitive.
    # In: df = dataframe of data; adsorbate = adsorbate to drop; site = site to drop
    
    a = (df['Adsorbate'] == adsorbate) & (df['Site'] == site)
    a = [not elem for elem in a]
    
    df = df[a]
    
    return df

def test_fit(X, y, models, model_selects, df1, scale_x = None, scale_y = None, 
             hyper_param_tune = None, group = 'Adsorbate'): 
    
    # Make model_fit_data 
   
    keys = ['Model', 'Predictions', 'Hyperparameters','Coefficients', 
            'Scaled Coefficients','Coef Stdevs', 'Errors', 'MAE', 
            'Error Stdev', 'Feat. Imp', 'Alphas', 'Model Select', 'Weights', 
            'Y scaler', 'X scaler']
    
    model_fit_data = {k: [] for k in keys}
    
    model_data = [[] for i in model_selects]

    data = [copy.deepcopy(model_data) for i in models]

    # Shape y properly
    y = y.reshape(-1,1) 
   
    # Scale y if y scaler input
    if scale_y:
        
        scale_y.fit(y)
        y = scale_y.transform(y)
        model_fit_data['Y scaler'] = scale_y
    
    if scale_x: 
        scale_x.fit(X)
        X = scale_x.transform(X)
        model_fit_data['X scaler'] = scale_x


    for count1, model in enumerate(models):
        
        for count2, model_select in enumerate(model_selects):
            
            m = copy.deepcopy(model_fit_data)
            
            m['Model Select'] = model_select
            m['Train Index'] = []
            m['Test Index'] = []
            m['Test Adsorbate Index'] = []
            test_ind = np.array([]).astype(int)

            
            splits = []
            if str(type(model_select)) == "<class 'sklearn.model_selection._split.KFold'>":
                for i,j in model_select.split(X,y):
                    splits.append((i, j))
                    
            if str(type(model_select)) ==  "<class 'sklearn.model_selection._split.GroupKFold'>":
                for i,j in model_select.split(X,y,df1[group]):
                    splits.append((i, j))

            if str(type(model_select)) ==  "<class 'sklearn.model_selection._split.StratifiedKFold'>":
                for i,j in model_select.split(X = X, y=df1[group]):
                    splits.append((i, j))

            for train_index, test_index in splits:

                test_ind = np.append(test_ind, test_index)                

                m['Train Index'].append(train_index)
                m['Test Index'].append(test_index)
                m['Test Adsorbate Index'] = df1['Adsorbate'].iloc[test_index]
                
                X_train, X_test = X[train_index], X[test_index]
                Y_train, Y_test = y[train_index], y[test_index]
                
                
                if hyper_param_tune:
                    hyper_param_tune.fit(X_train, Y_train)
                    params=hyper_param_tune.best_params_
                    m['Hyperparameters'].append(copy.deepcopy(hyper_param_tune.best_params_))
                    model = model.set_params(**params)    
                
                fitted_model = model.fit(X_train, Y_train)
                
                m['Model'].append(copy.deepcopy(fitted_model))
                
                prediction = fitted_model.predict(X_test).reshape(-1,1)
                
                if scale_y:
                    
                    m['Predictions'].append(scale_y.inverse_transform(prediction))
                    m['Errors'].append(scale_y.inverse_transform(Y_test) - scale_y.inverse_transform(prediction))
                    
                else:
                    m['Predictions'].append(prediction)
                    m['Errors'].append(Y_test - prediction)
                    
                if str(type(model)) == "<class 'sklearn.linear_model._coordinate_descent.LassoCV'>":
                    m['Alphas'].append(fitted_model.alpha_)
                    
                if str(type(model)) == "<class 'sklearn.linear_model._ridge.RidgeCV'>":
                    m['Alphas'].append(fitted_model.alpha_)
                    
                if str(type(model)) == "<class 'sklearn.linear_model._coordinate_descent.ElasticNetCV'>":
                    m['Alphas'].append(fitted_model.alpha_)
                
                if str(type(model)) == "<class 'sklearn.ensemble._forest.RandomForestRegressor'>":
                    m['Feat. Imp'].append(fitted_model.feature_importances_)
                
                if type(model).__name__ == 'XGBRegressor':
                    m['Feat. Imp'].append(fitted_model.feature_importances_)
                    weights = fitted_model.get_booster().get_score(importance_type = 'weight')
                    weight_keys = sorted(list(weights.keys()))
                    weight = [weights[i] for  i in weight_keys]
                    m['Weights'].append(weight)
                
                
                try:
                    
                    if scale_x:
                        xcoefs  = scale_x.transform(fitted_model.coef_.reshape(1,-1))
                        
                            
                        m['Scaled Coefficients'].append(fitted_model.coef_.reshape(1,-1))
                        m['Coefficients'].append(xcoefs)
                        
                    else:
                        m['Coefficients'].append(fitted_model.coef_.reshape(1,-1))
                except:
                    pass
                
            try:
                m['Coefficients'] = np.array(m['Coefficients'])
                m['Coef Stdevs'] = np.std(m['Coefficients'], axis = 0)
            except:
                pass
            
            try:
                
                m['Errors'] = np.concatenate(m['Errors'], axis = 0)[np.argsort(test_ind)]
                m['Predictions'] = np.concatenate(m['Predictions'], axis = 0)[np.argsort(test_ind)]
                m['MAE'] = np.mean(abs(m['Errors']))
                m['Error Stdev'] = np.std(m['Errors'])
            except:
                pass
                
                
            try:
                m['Feat. Imp'] = np.array(m['Feat. Imp'])
                if m['Feat. Imp'].any():
                    m['Coef Stdevs'] = np.std(m['Feat. Imp'], axis = 0)
                
            except:
                pass
            
            data[count1][count2] = m
            
    return data

def lowest_Eads(df):
    
    df_return = np.array([])
    
    for i in list(df.Adsorbate.unique()):
        a = df[df['Adsorbate']==i]
        for j in list(a.Substrate.unique()):
            b = a[a['Substrate']==j]
            df_return= np.append(df_return, b['Eads'].idxmin())
    
    df_return = copy.deepcopy(df).loc[df_return]
    return df_return

def atomic_breakdown(adsorbates):
    uniquechars = ''.join(adsorbates)
    uniquechars = ''.join(set(uniquechars))
    uniquechars = list(''.join([i for i in uniquechars if not i.isdigit()]))
    
    atomsmatrix = np.zeros((len(adsorbates), len(uniquechars)))
    
    for count, i in enumerate(adsorbates):
        counts = dict.fromkeys(uniquechars, 0)
        while len(i)>0:
            if len(i) == 1:
                counts[i] +=1
                i = ''
                continue
            if i[1].isdigit():
                string = i[0:2]
                counts[string[0]] += int(string[1])
                i = i[2:]
                continue
            if not i[1].isdigit():
                counts[i[0]] +=1
                i = i[1:]
                continue
            
        for count2, j in enumerate(uniquechars):
            atomsmatrix[count, count2] = counts[j]
    
    
    return uniquechars, atomsmatrix

def pca_analysis(X, pca = PCA(), cutoff = 0.9):

    pca.fit(X)

    X_new= pca.fit_transform(X)
    
    exp_var = np.cumsum(pca.explained_variance_ratio_)
    
    if str(type(pca)) == "<class 'sklearn.decomposition._pca.PCA'>":
        plt.figure()
        plt.plot(range(len(X_new[0,:])+1), np.append(0, exp_var))
        plt.bar(range(len(X_new[0,:])+1), np.append(0, pca.explained_variance_ratio_))
        plt.ylabel('Explained Variance')
        plt.xlabel('# Principle Components')
        plt.title('PCA: Variance Explained')
        plt.grid()
        
        plt.figure()
        
    if str(type(pca)) == "<class 'sklearn.decomposition._kernel_pca.KernelPCA'>":
        plt.figure()
        plt.plot(range(len(X_new[0,:])+1), np.append(0, np.cumsum(pca.eigenvalues_)/np.sum(pca.eigenvalues_)))
        
    return pca, X_new


def myplot(X, pca = PCA(), labels=None):
    
    plot_pca, X_pca = pca_analysis(X, pca = pca)
    
    score = X_pca[:,0:2]
    coeff= np.transpose(plot_pca.components_[0:2, :])
    
    xs = score[:,0]
    ys = score[:,1]
    n = coeff.shape[0]
    scalex = 1.0/(xs.max() - xs.min())
    scaley = 1.0/(ys.max() - ys.min())
    plt.scatter(xs * scalex,ys * scaley,s=5)
    for i in range(n):
        plt.arrow(0, 0, coeff[i,0], coeff[i,1],color = 'r',alpha = 0.5)
        if labels is None:
            plt.text(coeff[i,0]* 1.15, coeff[i,1] * 1.15, "Var"+str(i+1), color = 'green', ha = 'center', va = 'center')
        else:
            plt.text(coeff[i,0]* 1.15, coeff[i,1] * 1.15, labels[i], color = 'g', ha = 'center', va = 'center')
 
    plt.xlabel("PC{}".format(1))
    plt.ylabel("PC{}".format(2))
    plt.grid()

def loadingplot(coeff,labels=None):

    n = coeff.shape[0]
    for i in range(n):
        plt.arrow(0, 0, coeff[i,0], coeff[i,1],color = 'r',alpha = 0.5)
        
        if labels is None:
            plt.text(coeff[i,0]* 1.15, coeff[i,1] * 1.15, "Var"+str(i+1), color = 'green', ha = 'center', va = 'center')
        else:
            plt.text(coeff[i,0]* 1.15, coeff[i,1] * 1.15, labels[i], color = 'g', ha = 'center', va = 'center')

    plt.xlabel("PC{}".format(1))
    plt.ylabel("PC{}".format(2))
    plt.ylim((-0.5,0.5))
    plt.xlim((-0.5,0.5))
    plt.grid()

        
def cluster_PCs(x, pca=PCA(), cutoff=0.9, clustering = 'kmeans'):
    
    new_pca, x_pca = pca_analysis(x, pca=pca, cutoff=cutoff)
    exp_var = np.cumsum(pca.explained_variance_ratio_)
    cutoff_ind = sum(exp_var<cutoff)+1
    components = new_pca.components_[:cutoff_ind, :].T
    for i in components:
        if i[0] >0:
            i = -i
            
    if clustering == 'kmeans':
        cluster_fit = KMeans(n_clusters= cutoff_ind)
        
    cluster_fit.fit(components)
    centers=cluster_fit.cluster_centers_
    closest = []
    
    for i in centers:
        closest.append(np.argmin(np.linalg.norm(components - i, axis = 1)))
    
    plt.figure()
    plt.scatter(new_pca.components_[0,:], new_pca.components_[1,:], c=cluster_fit.labels_)
    plt.ylim((-0.5,0.5))
    plt.xlim((-0.5,0.5))
    return x_pca, new_pca, cluster_fit,closest

def convert_to_spherical(x):
    
    dims = len(x[0])
    
    spherical = np.empty(shape = np.shape(x))
    
    spherical[:,0] = np.linalg.norm(x, axis = 1)
    
    for i in np.arange(dims)[:-2]:
        
        numerator = x[:,i]
        denominator = np.linalg.norm(x[:,i:], axis = 1)
        
        inside= np.divide(numerator, denominator)
        
        spherical[:,i+1] = np.arccos(inside)
    
    
    numerator = x[:, -2] + np.linalg.norm(x[:, -2:], axis = 1)
    denominator = x[:, -1]
    
    fraction = np.divide(numerator, denominator)
    
    arccot = np.arctan(np.reciprocal(fraction))
    
    
    spherical[:, -1] = 2*arccot
    
   
    return spherical
# def draw_graph(graph):
#     """
#     Displays the graph
#     :param graph: networkx graph object
#     :return: None
#     """
    
#     Pt = [i for i in graph.nodes() if 'Pt' in graph.nodes[i]['element']]
#     spaced = np.vstack((np.linspace(-0.95, 0.95, len(Pt)), np.ones(len(Pt))*-1)).T
#     fixed_positions = {i: tuple(spaced[count]) for count, i in enumerate(Pt)}
#     for i in graph.nodes:
#         if graph.nodes[i]['element'] != 'Pt':
#             fixed_positions[i] = (np.random.uniform(-1, 1), np.random.uniform(0,1))
            
    
#     if bool(fixed_positions):
#         try:
#             if graph.graph['bonds_solved'] == "Problem with solver":
#                 pos = nx.spring_layout(graph, pos = fixed_positions, weight=None)
#             else:
#                 pos = nx.spring_layout(graph,weight='weight', pos = fixed_positions)
#         except:
#             pos = nx.spring_layout(graph, weight='weight', pos = fixed_positions)
    
#     else:
#         pos = nx.spring_layout(graph,weight='weight')
    
#     edge_styles = []
#     for e1, e2, data in graph.edges(data=True):
#             if data.get("weight", True) == 0: # Ads-Ads bond
#                 edge_styles.append("dashed")
#             else: # Surface-Surface bond
#                 edge_styles.append("solid")

#     plt.figure(figsize = (5,3), dpi = 300)
#     nx.draw(graph, with_labels=False, node_size=1500, node_color="skyblue",
#             node_shape="o", alpha=0.5, linewidths=4, font_size=25,style=edge_styles,
#             font_color="black", font_weight="bold", width=2, edge_color="grey",
#             pos=pos)
#     node_labels = nx.get_node_attributes(graph, 'element')
#     edge_labels = nx.get_edge_attributes(graph,'weight')
#     nx.draw_networkx_labels(graph, pos, node_labels)
#     nx.draw_networkx_edge_labels(graph, pos, edge_labels)
#     plt.show()
    
def test_predictions(X, models, y, x_scale = None, y_scale = None):
    
    if x_scale:
        X = x_scale.transform(X)

    
    predictions = []
    errors = []
    
    pred_mean = []
    pred_std = []
    err_mean = []
    
    for i in models:
        
        p = i.predict(X)
        
        if y_scale:
            p=y_scale.inverse_transform(p.reshape(-1,1)).reshape(1,-1)[0]
        
        predictions.append(p)
        errors.append(y-p)

    
    for i in range(len(X)):
      
        thisone = []
        
        for j in predictions:
            thisone.append(j[i])
        pred_mean.append(np.mean(thisone))
        pred_std.append(np.std(thisone))
        err_mean.append(np.mean(y[i]-thisone))
        
    return predictions, pred_mean, pred_std, errors, err_mean

def match_not_pt(x, y,xname, yname):
    
    substrates = x.Substrate.unique()

    
    returns={k: {K:[] for K in ['X', 'y']} for k in substrates}
        
    
    for index, i in x.iterrows():
        ads = i['Adsorbate']
        site = i['Site']
        returns[i['Substrate']]['X'].append(copy.deepcopy(i[xname]))
        returns[i['Substrate']]['y'].append(copy.deepcopy(y[(y['Adsorbate'] ==ads) & (y['Site'] == site)][yname].to_numpy()[0]))
        
    return returns