employee = [
    {"emp_id": 1, "name": "Charles", "dept": "F1", "salary": 45000, "year_joined": 1998, "H1": 65, "H2": 40},
    {"emp_id": 2, "name": "Mom", "dept": "Bank", "salary": 43000, "year_joined": 1987, "H1": 60, "H2": 64},
    {"emp_id": 3, "name": "Purva", "dept": "Stud", "salary": 15000, "year_joined": 2006, "H1": 85, "H2": 73},
    {"emp_id": 4, "name": "Gargee", "dept": "Stud", "salary": 45800, "year_joined": 2006, "H1": 95, "H2": 75},
    {"emp_id": 5, "name": "Carlos", "dept": "F1", "salary": 4500, "year_joined": 1998, "H1": 35, "H2": 20},
    {"emp_id": 6, "name": "Shriya", "dept": "Stud", "salary": 94000, "year_joined": 2006,"H1": 98, "H2": 90},
]

import pandas as pd

df = pd.DataFrame(employee)
df["avg_rat"]=df[["H1","H2"]].mean(axis=1)
print(df)

sal=df.groupby("dept")["salary"].mean()
print(sal)

sort=df.nlargest(3,"salary")
print(sort)

above_60=(df["avg_rat"]>=60).sum()
perc=(above_60/len(df)*100)
print(f"Percentage: {perc}")


