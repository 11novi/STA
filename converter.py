import pickle as pkl
import pandas as pd
with open("/nas.dbms/noviyanti/STA/saved_keywords/global_kws_dict_new2016.pkl", "rb") as f:
    object = pkl.load(f)

df = pd.DataFrame(object)
df.to_csv('filenew16.csv')

#import csv
#import pickle

#with open("/nas.dbms/noviyanti/STA/file.csv", 'r') as f:
    #reader = csv.reader(f)
   # pickle.dump(list(reader), open('file.pkl', 'wb'))