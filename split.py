
import pandas as pd

data = pd.read_csv('/nas.dbms/noviyanti/STA/data/new2016/train2015.csv')
df= pd.DataFrame(data)
df1=df.sample(n=1000)
df1.to_csv('train15_10000.csv')