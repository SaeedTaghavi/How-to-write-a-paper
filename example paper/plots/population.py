import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

from matplotlib import rc
font = {'family' : 'serif','serif': ['Computer Modern'], 'size'   : 11}
rc('font', **font)
rc('text', usetex=True)
rc("axes", linewidth=0.5)

data = pd.read_csv("../data/penguin_data.txt", sep = "\t", skiprows=1)

plt.plot(data["Season"], data["Adelie count"], "x" , label="Adelie", color ="blue")
adelie_fit = linregress(data["Season"], data["Adelie count"])
plt.plot(data["Season"], data["Season"]*adelie_fit.slope + adelie_fit.intercept, "-", color="blue", label='_nolegend_')

plt.plot(data["Season"], data["Chinstrap count"], "^", label="Chinstrap", color="green")
chinstrap_fit = linregress(data["Season"], data["Chinstrap count"])
plt.plot(data["Season"], data["Season"]*chinstrap_fit.slope + chinstrap_fit.intercept, "-", color="green", label='_nolegend_')

plt.plot(data["Season"], data["Gentoo count"], "o", label="Gentoo", color = "red")
gentoo_fit = linregress(data["Season"], data["Gentoo count"])
plt.plot(data["Season"], data["Season"]*gentoo_fit.slope + gentoo_fit.intercept, "-", color="red", label='_nolegend_')

plt.xlabel(r"Year of count")
plt.ylabel(r"Count")
plt.title(r"Penguin population trends for Signy Island")

plt.tight_layout()
plt.legend()
plt.savefig("../figures/population.pdf")
plt.show()