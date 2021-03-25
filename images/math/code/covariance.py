import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

x1 = np.arange(0.5,2.5,0.01)
y1 = np.linspace(1.0,4.0,200)
noise = np.random.permutation(np.random.normal(0, 0.5,(200,)))

fig, axes = plt.subplots(2,1, figsize=(5,5))

sns.scatterplot(ax = axes[0], x=x1,y=y1+noise)
axes[0].set(xlabel="X", ylabel="Y", title="Co Variance (X, Y) > 0")


y2 = np.linspace(4.0,1.0,200)

sns.scatterplot(ax = axes[1], x=x1,y=y2+noise)
axes[1].set(xlabel="X", ylabel="Y", title="Co Variance (X, Y) < 0")

plt.show()
