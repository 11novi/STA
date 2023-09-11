import pandas as pd

df = pd.read_csv('/nas.dbms/noviyanti/STA/data/new2016/Laptop_Train_v2.csv')
df.assign(simbol='$')
df["simbol"]='$'
new_col= []
for s in df["Sentence"]:
    for index, w in enumerate(df["Aspect"]):
        if w in s:
            a=" ".join([s.replace(w, simbol) for simbol in df["simbol"][index]])
    new_col.append(a)

df["new_col"]=new_col
df.to_csv('output.csv')
#df["new_col"]=df['Text'].apply(lambda x:' '.join(simbol() if i in df["Aspect"]))
#print(df)