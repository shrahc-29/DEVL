import pandas as pd
with open('nba_player_stats.csv','r'):
    content=pd.read_csv('nba_player_stats.csv')

df=pd.DataFrame(content)
print(df.head())
print(df.describe())



Q1=df["PF"].quantile(0.25)
Q3=df["PF"].quantile(0.75)

IQR=Q3-Q1
low=Q1-1.5*IQR
high=Q3+1.5*IQR

print(low)
print(high)

df_new=df[(df['PF']>=low) & (df['PF']<=high)]
print(df_new)

print("Columns: ")
print(df.columns)

print("Sorted 10: ")
sort=df_new.nlargest(10,"PER")
print(sort)