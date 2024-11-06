import pandas as pd
import matplotlib.pyplot as plt

mobile = pd.read_csv('dados/mobileusage.csv')
mobile2 = mobile.groupby('Device Model')['Screen On Time (hours/day)'].mean()
mobile2.plot.bar(stacked=True, x='Operating System', y='Screen On Time (hours/day)', rot=0)
mobile2.plot(figsize=(11,6))
plt.xlabel("Operating Systems")
plt.ylabel("Hours per day")
plt.show()

mobile3 = mobile.groupby('Device Model')['Battery Drain (mAh/day)'].mean()
mobile3.plot.line(stacked=True, x='Device Model', y='Battery Drain (mAh/day)', rot=0)
mobile3.plot(figsize=(11,6))
plt.xlabel("Device Model")
plt.ylabel("Battery Drain (mAh/day)")
plt.show()

mobile4 = mobile.groupby('Device Model')['App Usage Time (min/day)'].count()
mobile4.plot.pie(stacked=True, x='Device Model', y='Age', rot=0)
mobile4.plot(figsize=(11,6))
plt.xlabel("App Usage Time (min/day)")
plt.ylabel("")
plt.show()

