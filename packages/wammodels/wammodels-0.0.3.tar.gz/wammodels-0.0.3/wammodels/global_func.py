import numpy as np
import pandas as pd

def adstock_new(sales, decay_rate):
    sales = np.array(sales, dtype=float)
    adstock_sales = np.zeros_like(sales)
    adstock_sales[0] = sales[0]
    for i in range(1, len(sales)):
        adstock_sales[i] = sales[i] + decay_rate * adstock_sales[i-1]            
    return adstock_sales

def adstock(list,adstock_rate):
    adstock_list = []
    for i in range(len(list)):
        if i == 0: 
            adstock_list.append(list[i])
        else:
            adstock_list.append(list[i] + adstock_rate * adstock_list[i-1])            
    return adstock_list

def adbudg(list,rho=0,v=1,p=1,beta=1,alpha=0):
    rho = rho*p
    tk=  alpha+((beta*(np.power(list,v)) )/( (np.power(list,v)) + (np.power(rho,v)) ))
    return tk

def stockbudg(var ,adstock_rate, rho=0, v=1, p=1 ,beta=1, alpha=0):
    return adbudg(adstock_new(var, adstock_rate), v = v, rho = rho, p = p, beta = beta, alpha = alpha)

def creation_seasonalities(data,start_range):
    matrix = np.zeros((len(data), 12))
    base = pd.DataFrame(matrix, columns=["ENE","FEB","MAR","ABR","MAY","JUN","JUL","AGO","SEP","OCT","NOV","DIC"])
    k = start_range
    base.loc[0, base.columns[k-1]] = 1
    for i in range(1, len(data)):
        k += 1
        if k > 12:
            k = 1
        base.loc[i, base.columns[k-1]] = 1
    
    return base

def wmadstock_rate(*args):
    return {"adstock_rate":list(args)}
def wmv(*args):
    return {"v":list(args)}
def wmrho(*args):
    return {"rho":list(args)}
def wmdiff(*args):
    return {"diff":list(args)}
def wmlag(*args):
    return {"lag":list(args)}
def wmcoef(*args):
    return {"coef":list(args)}
def wmcomb(*args):
    if len(args) <= 0:
        return {}
    data =  args[0]
    for arg in args[1:]:
        data = {**data, **arg}
    return data
def wmvar(*args):
    if len(args) <= 0:
        return {}
    data =  args[0]
    for arg in args[1:]:
        data = {**data, **arg}
    data = {k: v[0] for k, v in data.items()}
    return data
    