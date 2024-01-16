import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import quad

# normalize
def normalize(arr, t_min, t_max):    
    try:
        arr = arr.to_numpy()
    except:
        pass
    norm_arr = []
    diff = t_max - t_min
    diff_arr = max(arr) - min(arr)   
    for i in arr:
        temp = (((i - min(arr))*diff)/diff_arr) + t_min
        norm_arr.append(temp)
    return norm_arr
def simple_norm(arr):
    try:
        arr = arr.to_numpy()
    except:
        pass
    norm_arr = []
    diff = 1
    diff_arr = max(arr) - min(arr)   
    for i in arr:
        temp = (((i - min(arr))*diff)/diff_arr)
        norm_arr.append(temp)
    return norm_arr
def norm2(arr):
    try:
        arr = arr.to_numpy()
    except:
        pass
    diff_arr = max(arr) - min(arr)   
    return arr/diff_arr

def mapcolors(n):
    """Return a list of n colors from the default colormap"""
    return [plt.cm.jet(int(x*plt.cm.jet.N/n)) for x in range(n)]

# signifikanztest

def ttest(werte,unsicherheiten):
    for i,(v1, uv1) in enumerate(zip(werte,unsicherheiten)):
        # print(i,end = '\t')
        for j,(v2, uv2) in enumerate(zip(werte, unsicherheiten)):
            d = abs(v1-v2)
            ud = np.sqrt(uv1**2 + uv2**2)
            t = d/ud
            print(round(t,3), end = '\t')
        print()

def prob(x):
    return np.exp(-x**2/2)/np.sqrt(2*np.pi)


def ttestPaussen(werte,unsicherheiten):
    for i,(v1, uv1) in enumerate(zip(werte,unsicherheiten)):
        for j,(v2, uv2) in enumerate(zip(werte, unsicherheiten)):
            d = abs(v1-v2)
            ud = np.sqrt(uv1**2 + uv2**2)
            t = d/ud
            P = quad(prob,-t,t)
            # print(round((P[0])*100,3), end = '\t')
            print(f"\SI{{{round((P[0])*100,3)}}}" + r"{\percent}", end = '\t')
            # print(P, end = '\t')
        print()
def ttestPinnen(werte,unsicherheiten):
    for i,(v1, uv1) in enumerate(zip(werte,unsicherheiten)):
        for j,(v2, uv2) in enumerate(zip(werte, unsicherheiten)):
            d = abs(v1-v2)
            ud = np.sqrt(uv1**2 + uv2**2)
            t = d/ud
            P = quad(prob,-t,t)
            # print(round((1-P[0])*100,3), end = '\t')
            print(f"\SI{{{round((1-P[0])*100,3)}}}" + r"{\percent}", end = '\t')
            # print(P, end = '\t')
        print()