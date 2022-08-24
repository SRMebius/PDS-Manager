import pickle
data = {'PDS Manager':['', '']}
with open('pds.pkl', 'wb') as f:
    pickle.dump(data, f)
with open('reg.dll', 'w') as f:
    pass
