import pandas as pd

volunteers = [
    {"vid": 1, "name": "Aarav", "program": "Health", "hours": {"Q1": 50, "Q2": 60, "Q3": 55, "Q4": 65}, "city": "Pune", "year": 2023},
    {"vid": 2, "name": "Diya", "program": "Education", "hours": {"Q1": 70, "Q2": 80, "Q3": 75, "Q4": 85}, "city": "Mumbai", "year": 2023},
    {"vid": 3, "name": "Rohan", "program": "Environment", "hours": {"Q1": 40, "Q2": 45, "Q3": 50, "Q4": 55}, "city": "Delhi", "year": 2023},
    {"vid": 4, "name": "Mira", "program": "Health", "hours": {"Q1": 65, "Q2": 70, "Q3": 75, "Q4": 80}, "city": "Pune", "year": 2024},
    {"vid": 5, "name": "Kabir", "program": "Education", "hours": {"Q1": 90, "Q2": 85, "Q3": 88, "Q4": 92}, "city": "Mumbai", "year": 2024},
    {"vid": 6, "name": "Isha", "program": "Environment", "hours": {"Q1": 55, "Q2": 60, "Q3": 58, "Q4": 62}, "city": "Delhi", "year": 2024},
    {"vid": 7, "name": "Aarav", "program": "Health", "hours": {"Q1": 60, "Q2": 70, "Q3": 65, "Q4": 75}, "city": "Pune", "year": 2024},
]

df=pd.DataFrame(volunteers)

df["Q1"] = [x["Q1"] for x in df["hours"]]
df["Q2"] = [x["Q2"] for x in df["hours"]]
df["Q3"] = [x["Q3"] for x in df["hours"]]
df["Q4"] = [x["Q4"] for x in df["hours"]]



total_hrs=[]
avg_hrs=[]

for i in range(len(df)):
    total=df.loc[i,"Q1"]+df.loc[i,"Q2"]+df.loc[i,"Q3"]+df.loc[i,"Q4"]
    avg=total/4
    total_hrs.append(total)
    avg_hrs.append(avg)

df["total_hrs"]=total_hrs
df["avg_hrs"]=avg_hrs



prog=df.groupby("program")["avg_hrs"].mean()
print(prog)

n23=list(df[df["year"]==2023]["name"])
n24=list(df[df["year"]==2024]["name"])

retain=0

for name in n23:
    if name in n24:
        retain=+1
    
if retain>0:
    rate=(retain/len(n23))*100
    print(rate)
else:
    print("0")