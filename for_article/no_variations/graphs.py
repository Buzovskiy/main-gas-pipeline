import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter

import for_article.no_variations.calculations as c


plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["mathtext.fontset"] = "stix"
rcParams["font.size"] = "14"

z = np.polyfit(c.x, c.y_pk, 4)
p = np.poly1d(z)
fig, ax = plt.subplots()
ax.plot(c.x, [p(_)*10 for _ in c.x], label="Natural gas pressure")
ax.plot([min(c.x), 110], [p(110)*10, p(110)*10], ls='--', dashes=(10, 10), color='black', lw=0.6)
ax.plot([110, 110], [p(110)*10, 0], ls='--', dashes=(10, 10), color='black', lw=0.6)
ax.plot([max(c.x), max(c.x)], [p(max(c.x))*10, 0], ls='--', dashes=(10, 10), color='black', lw=0.6)
ax.plot([min(c.x), max(c.x)], [p(max(c.x))*10, p(max(c.x))*10], ls='--', dashes=(10, 10), color='black', lw=0.6)
ax.set_ylabel("P,"+"\n"+"бар", rotation=0, labelpad=33, ha='left', va='center')
ax.set_xlabel("x, км")
ax.set_xlim(0)
ax.set_ylim(30)
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(2))
ax.annotate(r"$\mathrm{P_{0}}$", xy=(min(c.x), p(min(c.x))*10), xytext=(min(c.x) + 4, p(min(c.x))*10 - 4),
                arrowprops=dict(arrowstyle='-', ls='-', shrinkA=0, shrinkB=0, lw=0.6)
            )
ax.annotate(r"$\mathrm{P_{x}}$", xy=(min(c.x), p(110)*10), xytext=(min(c.x) + 4, p(110)*10 + 2),
                arrowprops=dict(arrowstyle='-', ls='-', shrinkA=0, shrinkB=0, lw=0.6)
            )
ax.annotate("x", xy=(110, ax.get_ylim()[0]), xytext=(115, ax.get_ylim()[0]+2),
                arrowprops=dict(arrowstyle='-', ls='-', shrinkA=0, shrinkB=0, lw=0.6)
            )
ax.annotate("L", xy=(max(c.x), ax.get_ylim()[0]), xytext=(max(c.x)-7, ax.get_ylim()[0]+2),
                arrowprops=dict(arrowstyle='-', ls='-', shrinkA=0, shrinkB=0, lw=0.6)
            )
ax.annotate(r"$\mathrm{P_{1}}$", xy=(min(c.x), p(max(c.x))*10), xytext=(min(c.x) + 4, p(max(c.x))*10 + 2),
                arrowprops=dict(arrowstyle='-', ls='-', shrinkA=0, shrinkB=0, lw=0.6),
                bbox=dict(facecolor='white', edgecolor='none', boxstyle='round', pad=0)
            )

# ax.text(max(c.x), p(max(c.x))*10, r"$\mathrm{P_{1}}$")
plt.subplots_adjust(left=0.152, bottom=0.245, right=0.971, top=0.98, wspace=0.26, hspace=0.305)
ax.grid(True)
cm = 1/2.54
fig.set_size_inches(15*cm, 6*cm)
plt.savefig('parameters.jpg', dpi=2000)
plt.show()
# axes['ax15'].set_ylabel(r"$\mathrm{\lambda}_{soil}$," +"\n"+r"$\frac{W}{m^2 \cdot K}$", )
