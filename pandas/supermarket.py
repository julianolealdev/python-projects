import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import pygwalker as pg

market= pd.read_csv('dados/sp.csv')
market=pd.DataFrame(market)

enter = input("Digite a letra para qual junção de dados você gostaria de ver, a = Genero, b = Cidade, c = Customer, d = Type: ")

plana = (market.groupby(['Gender',"Product"])['Sales'].sum())

planb = (market.groupby(['City',"Product"])['Sales'].sum())

planc = (market.groupby(['Customer type',"Product"])["Sales"].sum())

pland = (market.groupby('Product')['Sales'].sum())

if enter == "a":
    print(plana)
elif enter == "b": 
    print(planb)
elif enter == "c": 
    print(planc)
elif enter == "d": 
    print(pland)
else:
    print("Você digitou algo fora das opções")
