import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linear_sum_assignment
from greedy_tsp_solver import greedy_tsp_solver

nodes_per_side = 10
mean_fill_rate = 1/24
std_fill_rate = 1/96
fill_threshold = 0.9

np.random.seed(42) # for reproducibility, remove for mc sims
adj_matrix = np.random.randint(1,10, size=(nodes_per_side, nodes_per_side))
np.fill_diagonal(adj_matrix, 0) #avoid self loops
adj_matrix = (adj_matrix + adj_matrix.T)/2 # make symmetric

fill_rates = np.random.normal(mean_fill_rate, std_fill_rate, size=(nodes_per_side, nodes_per_side))
fill_levels = np.zeros((nodes_per_side, nodes_per_side))

def update_fill_levels(fill_levels, fill_rates):
    fill_levels += fill_rates
    return fill_levels

