import pandas as pd
import matplotlib.pyplot as plt

x = [10, 100, 1000, 10000, 100000]
y = [2, 4 ,8, 16, 32]

fig = plt.figure(figsize=(8, 6))
plt.scatter(x, y)
plt.plot(x, y)
plt.grid()
plt.xscale("log")
plt.yscale("log",basey=2)
plt.xlabel("x",fontsize=20)
plt.ylabel("y",fontsize=20)
plt.title("Plot with both log axes",fontsize=25)
plt.show()