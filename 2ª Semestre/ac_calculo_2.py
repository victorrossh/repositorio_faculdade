import numpy as np
import matplotlib.pyplot as plt



def f(x): return 3*np.log10(x)
x = np.linspace(-10, 9, 10**5)
plt.plot(x, f(x))
plt.grid()
plt.show()


'''
raiz = np.sqrt
seno = np.sin
cos = np.cos
tg = np.tan
log = np.log
log10 = np.log10
e = np.exp
'''