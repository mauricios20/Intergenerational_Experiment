import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import data
path = '/Users/mau/Dropbox/Mac/Documents/Dissertation/Intergenerational_Exp/Data'
os.chdir(path)

dtf = pd.read_csv('DataNoPractice.csv')
print(dtf.head(10))
dtf.PER.max()
dtfg1 = dtf.loc[dtf['Condition'].isin(["Gen1"])]
dtfg2 = dtf.loc[dtf['Condition'].isin(["Gen2Neg", "Gen2Pos"])]
dtfg3 = dtf.loc[dtf['Condition'].isin(["Gen3NegPos", "Gen3PosNeg "])]

# Plot Figures
# Define Color palettes
palette_tab10 = sns.color_palette("tab10", 10)
paletteG2 = sns.color_palette([palette_tab10[1], palette_tab10[2]])
paletteG3 = sns.color_palette([palette_tab10[3], palette_tab10[4]])

# ## Box Plots ## #
fig1, axes = plt.subplots(2, 1, sharex=True)
sns.boxplot(data=dtf, x='Condition', y='PER', ax=fig1.axes[0]).set(
    ylabel='(%) Allocation in Risky Asset', xlabel=None)

sns.boxplot(data=dtf, x='Condition', y='Belief', ax=fig1.axes[1]).set(
    ylabel='Belief', xlabel=None)

# ## Kernel Density Plots ## #
# Percent Allocations

bw = 0.3
fig2, axes = plt.subplots(2, 3, sharex=True, sharey=True)
sns.kdeplot(data=dtfg1, x='PER', ax=fig2.axes[0], bw_method=bw)
sns.kdeplot(data=dtfg2, x='PER', hue='Condition', palette=paletteG2,
            ax=fig2.axes[1], bw_method=bw, legend=False)
sns.kdeplot(data=dtfg3, x='PER', hue='Condition', palette=paletteG3,
            ax=fig2.axes[2], bw_method=bw, legend=False)

# Beliefs
sns.kdeplot(data=dtfg1, x='Belief', ax=fig2.axes[3], bw_method=bw)
sns.kdeplot(data=dtfg2, x='Belief', hue='Condition', palette=paletteG2,
            ax=fig2.axes[4], bw_method=bw, legend=False)
sns.kdeplot(data=dtfg3, x='Belief', hue='Condition', palette=paletteG3,
            ax=fig2.axes[5], bw_method=bw, legend=False)
axes[0, 1].set(ylabel=None)
axes[0, 2].set(ylabel=None)
axes[1, 1].set(ylabel=None)
axes[1, 2].set(ylabel=None)
axes[1, 0].set(xlabel=None)
axes[1, 1].set_title('(%) Allocation', size=10)
axes[1, 2].set(xlabel=None)
labels = ['Gen1', 'Gen2Pos', 'Gen2Neg', 'Gen3PosNeg', 'Gen3NegPos']
fig2.legend(labels, bbox_to_anchor=(0.5, 0),
            ncol=len(labels), loc='lower center')
for i in range(0, 6):
    fig2.axes[i].grid(True)

# ## Cumulative Density Functions ## #

fig3, axes = plt.subplots(2, 3, sharex=True, sharey=True)
sns.kdeplot(data=dtfg1, x='PER',
            ax=fig3.axes[0], bw_method=bw, cumulative=True)
sns.kdeplot(data=dtfg2, x='PER', hue='Condition', palette=paletteG2,
            ax=fig3.axes[1], bw_method=bw, cumulative=True, legend=False)
sns.kdeplot(data=dtfg3, x='PER', hue='Condition', palette=paletteG3,
            ax=fig3.axes[2], bw_method=bw, cumulative=True, legend=False)

# Beliefs
sns.kdeplot(data=dtfg1, x='Belief',
            ax=fig3.axes[3], bw_method=bw, cumulative=True)
sns.kdeplot(data=dtfg2, x='Belief', hue='Condition', palette=paletteG2,
            ax=fig3.axes[4], bw_method=bw, cumulative=True, legend=False)
sns.kdeplot(data=dtfg3, x='Belief', hue='Condition', palette=paletteG3,
            ax=fig3.axes[5], bw_method=bw, cumulative=True, legend=False)
axes[0, 1].set(ylabel=None)
axes[0, 2].set(ylabel=None)
axes[1, 1].set(ylabel=None)
axes[1, 2].set(ylabel=None)
axes[1, 0].set(xlabel=None)
axes[1, 1].set_title('(%) Allocation', size=10)
axes[1, 2].set(xlabel=None)
labels = ['Gen1', 'Gen2Pos', 'Gen2Neg', 'Gen3PosNeg', 'Gen3NegPos']
fig3.legend(labels, bbox_to_anchor=(0.5, 0),
            ncol=len(labels), loc='lower center')
for i in range(0, 6):
    fig3.axes[i].grid(True)

# ## Individual figures ## #
# Box Plots
fig4 = plt.figure()
sns.boxplot(data=dtf, x='Condition', y='PER').set(
    ylabel='(%) Allocation in Risky Asset', xlabel=None)

fig5 = plt.figure()
sns.boxplot(data=dtf, x='Condition', y='Belief').set(
    ylabel='(%) Allocation in Risky Asset', xlabel=None)

# Kernerl Density
fig6 = plt.figure()
sns.kdeplot(data=dtf, x='PER', hue='Condition',
            bw_method=bw).set(xlabel='(%) Allocation')
plt.grid()

fig7 = plt.figure()
sns.kdeplot(data=dtf, x='Belief', hue='Condition', bw_method=bw)
plt.grid()

# Cumulative Densities
fig8 = plt.figure()
sns.kdeplot(data=dtf, x='PER', hue='Condition', bw_method=bw,
            cumulative=True, common_grid=True).set(xlabel='(%) Allocation')
plt.grid()

fig9 = plt.figure()
sns.kdeplot(data=dtf, x='Belief', hue='Condition',
            bw_method=bw, cumulative=True)
plt.grid()
plt.show()
