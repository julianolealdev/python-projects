import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

market= pd.read_csv('dados/sp.csv')

market=pd.DataFrame(market)

enter = input("Enter a letter for which function you want to know the datas, a=Gender, b=City, c=Customer, d=Product ")

plana = (market.groupby(['Gender',"Product"])['Sales'].sum())

planb = (market.groupby(['City',"Product"])['Sales'].sum())

planc = (market.groupby(['Customer type',"Product"])["Sales"].sum())

pland = (market.groupby('Product')['Sales'].sum())

if enter == "a":
    print(plana)
    market1 = market.groupby('Gender')['Sales'].sum()
    market1.plot.bar(x='Gender', y='Sales', rot=0)
    market1.plot(figsize=(12,7))
    plt.savefig('figs/GenderBySales')
    plt.show()
elif enter == "b": 
    print(planb)
    market2 = market.groupby('City')['Sales'].sum()
    market2.plot.bar(x='City', y='Sales', rot=0)
    market2.plot(figsize=(12,7))
    plt.savefig('figs/CityBySales')
    plt.show()
elif enter == "c": 
    print(planc)
    market3 = market.groupby('Customer type')['Sales'].sum()
    market3.plot.bar(x='Customer type', y='Sales', rot=0)
    market3.plot(figsize=(12,7))
    plt.savefig('figs/CustomerBySales')
    plt.show()
elif enter == "d": 
    print(pland)
    market4 = market.groupby('Product')['Sales'].sum()
    market4.plot.bar(x='Product', y='Sales', rot=0)
    market4.plot(figsize=(12,7))
    plt.savefig('figs/ProductBySales')
    plt.show()
else:
    print("You enter something out of the options") 

