import matplotlib.pyplot as plt

fig,ax = plt.subplots(nrows=1, ncols=1)
ax.bar([0,1],[0.7,0.3],align="center")
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
fig.savefig("./GeneralizedLinearModels/figs/bernulli.pdf")



