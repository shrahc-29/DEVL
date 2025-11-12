import pandas as pd
with open('nba_player_stats.csv','r'):
    content=pd.read_csv('nba_player_stats.csv')
df=content
import matplotlib.pyplot as plt
plt.scatter(df["PTS"], df["AST%"], color='red')
plt.show() 

plt.hist(df["3P%"],color='pink')
plt.show()

import seaborn as sns
corr=df.corr(numeric_only=True)
sns.heatmap(corr)
plt.show()