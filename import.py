
import pandas as pd
import gc
import os
store = []
for file in os.listdir("."):
    if file.endswith(".csv"):
        data = pd.read_csv(file, dtype=pd.np.object)
        store += data['Genus'].tolist()
        gc.collect()

store = map(lambda x: x.lower(), store)
print(len(store), len(pd.np.unique(store)))
