'''
General Utilities for all models

'''
import pickle
import numpy as np
from numpy import interp

def pickle_load(filepath):
    f = open(filepath, "rb")
    data = pickle.load(f)
    f.close()
    return data

def pickle_dump(data, filepath):
    f = open(filepath, "wb")
    pickle.dump(data, f)
    f.close()

def get_data(filepath):
    data = dict()
    handle = open(filepath, 'r')
    for line in handle:
        line = line.split('\t')
        ecnumber = line[0]
        smiles = line[1].strip('\n').split('$')
        data[ecnumber] = smiles
    handle.close()
    return data

def polyfit(x, y, degree):
    results = {"Coefficients": [], "R-squared": 0}

    coeffs = np.polyfit(x, y, degree)

    results["Coefficients"] = coeffs.tolist()

    # R-squared calculation
    p = np.poly1d(coeffs)
    y_fit = p(x)                        
    y_mean = np.sum(y)/len(y)
    ssreg = np.sum((y_fit-y_mean)**2)
    sstot = np.sum((y - y_mean)**2)
    
    results["R-squared"] = ssreg / sstot

    return results