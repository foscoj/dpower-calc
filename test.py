#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import seaborn as sns
df = pd.read_csv('data\\Day-ahead Prices_201901010000-202001010000.csv',skiprows=1,names=['mtu','price_mwh'])
df['price_kwh'] = df['price_mwh'] / 1000
df = df.drop(['price_mwh'], axis=1)
new = df['mtu'].str.split(' - ',n=1,expand=True)
df['mtu_start'] = pd.to_datetime(new[0])
#df['mtu_stop'] = pd.to_datetime(new[1])
df = df.drop(['mtu'], axis=1)
#df = df.drop(['mtu_stop'], axis=1)
df = df.sort_index(axis=1)
df = df.set_index('mtu_start')
mean_hour = df.groupby(df.index.hour).mean()
#box = df.groupby(df.index.hour).boxplot()

#print(mean_hour)
#print(df)

# %%
#df.cumsum()
plt.figure()
#mean_hour.plot.bar()
#df.plot.bar()
#df.boxplot(by=df.index.hour, 
#                       column=['price_kwh'], 
#                       grid=False,)
plt.savefig("export\\box.svg")

print("done")

# %%
df.shape
#bplot = sns.boxplot(y='price_kwh',x=df.index.hour, data=df, width=0.5, palette='colorblind')
vplot = sns.violinplot(y='price_kwh',x=df.index.hour, data=df, palette='colorblind')

#bplot = sns.swarmplot(y='price_kwh',x=df.index.hour, data=df, color='black', alpha=0.25)
#bplot = sns.stripplot(y='price_kwh',x=df.index.hour, data=df, jitter=True, marker='o',color='black', alpha=0.25)
#bplot.axes.set_title("2019: Börsenstrompreis nach Stunde",fontsize=16)
#bplot.set_xlabel("Stunde", fontsize=14)
#bplot.set_ylabel("Preis in €/kwH", fontsize=14)
vplot.axes.set_title("2019: Börsenstrompreis nach Stunde",fontsize=16)
vplot.set_xlabel("Stunde", fontsize=14)
vplot.set_ylabel("Preis in €/kwH", fontsize=14)
#bplot_file_name="boxplot_and_swarmplot_with_seaborn_b.png"
vplot_file_name="boxplot_and_swarmplot_with_seaborn_v.png"
# save as png
#bplot.figure.savefig(bplot_file_name,
#                    format='png',
#                    dpi=300)
vplot.figure.savefig(vplot_file_name,format='png',dpi=300)
# %%
