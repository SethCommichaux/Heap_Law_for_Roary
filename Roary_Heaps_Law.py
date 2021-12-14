import numpy as np
import random
import sys
import math
# import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def heaps_law(x,k,alpha):
	return k*x**(alpha)

print("Loading data!")

# Transpose gene presence absence matrix
r = []

for h,i in enumerate(open(sys.argv[1])):
    tmp = i.strip().split('\t')[1:]
    if h == 0: continue
    tmp = [int(x) for x in tmp]
    r.append(tmp)

r = np.array(r).T
num_genomes,num_genes = r.shape

print("Number of genomes: ",num_genomes,"\nNumber of genes: ",num_genes,"\n")

print("Calculating Heap's Law!")

# estimate parameters of Heaps' Law
x,y = [],[]

for iteration in range(int(sys.argv[2])):
	print('Iteration: ',iteration+1,end = "\r")
	result = np.zeros(num_genes)
	c = list(range(num_genomes))
	random.shuffle(c)
	for h,i in enumerate(c):
		x.append(h+1)
		result += r[i]
		y.append(np.count_nonzero(result))

pars, cov = curve_fit(f=heaps_law, xdata=x, ydata=y, p0=[0, 0], bounds=(-np.inf, np.inf))
k,gamma = pars

print("k = ",k,"\ngamma = ",gamma,"\n")

# plt.scatter(x,y)
# plt.show()
