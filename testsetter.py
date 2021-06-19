import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.ticker import FormatStrFormatter

x = np.arange(1, 5, 0.1)
y = [x1**2/10000000 for x1 in x]


fig, ax = plt.subplots()
ax.plot(x, y)
ax.ticklabel_format(axis='y', style='plain')
# ax.yaxis.set_major_formatter(FormatStrFormatter('%0.1f'))
plt.show()
