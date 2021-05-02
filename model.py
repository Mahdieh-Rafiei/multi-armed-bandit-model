import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(1)
qs = np.random.normal(loc=0, scale=1, size=(10))
d = np.array([np.random.normal(loc=qs[a], scale=1, size=1000) for a in range(10)])
df = pd.DataFrame(d.T).melt(var_name='actions', value_name='reward')

# create figure
fig, ax = plt.subplots(1, figsize=(10, 3))
sns.boxenplot(x='actions', y='reward', data=df,  ax=ax,)
[ax.spines[pos].set_visible(False) for pos in ('right', 'bottom', 'top')];
plt.tight_layout()
