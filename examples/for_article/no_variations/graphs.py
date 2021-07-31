"""
This file contains the calculations of changing the parameters of natural gas along the length of the gas pipeline
and crates figures 1, 7, 8, 9, 10, 11 for the article
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib.ticker as ticker

import examples.for_article.no_variations.calculations as c


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
ax.set_ylabel("P,"+"\n"+"bar", rotation=0, labelpad=33, ha='left', va='center')
ax.set_xlabel("x, km")
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

plt.subplots_adjust(left=0.152, bottom=0.245, right=0.971, top=0.98, wspace=0.26, hspace=0.305)
ax.grid(True)
cm = 1/2.54
fig.set_size_inches(15*cm, 6*cm)
plt.savefig('fig.1.jpg', dpi=1000)

axes2 = {}
fig2 = {}
figures = ['fig.7', 'fig.8', 'fig.9', 'fig.10', 'fig.11']
for figure in figures:
    fig2[figure], axes2[figure] = plt.subplots()

axes2['fig.7'].plot(c.x, c.y_ro, label="Density of natural gas")
axes2['fig.7'].set_ylabel(r"$\mathrm{\rho},$"+"\n"+r"$\mathrm{\dfrac{kg}{m^3}}$", rotation=0, labelpad=15)
axes2['fig.7'].set_ylim(25)
axes2['fig.7'].yaxis.set_major_locator(ticker.MultipleLocator(5))


axes2['fig.8'].plot(c.x, c.y_nu, label="Viscosity kinematic")
axes2['fig.8'].set_ylabel(r"$\mathrm{\nu},$" +"\n"+r"$\mathrm{\dfrac{m^2}{s}}$", rotation=0, labelpad=15)
axes2['fig.8'].yaxis.set_major_locator(ticker.MultipleLocator(0.25e-7))

axes2['fig.9'].plot(c.x, c.y_mu, label="Natural gas dynamic viscosity, m2/s")
axes2['fig.9'].set_ylabel(r"$\mathrm{\mu},$" +"\n"+r"$\mathrm{Pa \cdot s}$", rotation=0, labelpad=23)
axes2['fig.9'].set_ylim(1.10e-5)
axes2['fig.9'].yaxis.set_major_locator(ticker.MultipleLocator(0.05e-5))

axes2['fig.10'].plot(c.x, c.y_Cp, label="Isobar specific heat capacity of the natural gas")
axes2['fig.10'].set_ylabel(r"$\mathrm{C_p},$" +"\n"+r"$\mathrm{\dfrac{J}{kg \cdot K}}$", rotation=0, labelpad=23)
axes2['fig.10'].set_ylim(2500)
axes2['fig.10'].yaxis.set_major_locator(ticker.MultipleLocator(50))

axes2['fig.11'].plot(c.x, c.y_lambda, label="Hydraulic resistance coefficient")
axes2['fig.11'].set_ylabel(r'$\mathrm{\lambda}$', rotation=0, labelpad=15)
axes2['fig.11'].set_ylim(0.01135)
axes2['fig.11'].yaxis.set_major_locator(ticker.MultipleLocator(0.00001))

cm = 1/2.54
for key, ax in axes2.items():
    ax.grid(True)
    ax.set_xlabel('x, km')
    ax.set_xlim(0)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
    fig2[key].set_size_inches(15*cm, 6*cm)
    fig2[key].subplots_adjust(left=0.2, bottom=0.257, right=0.971, top=0.90, wspace=0.26, hspace=0.42)
    fig2[key].savefig(f'{key}.jpg', dpi=1000)

plt.show()
