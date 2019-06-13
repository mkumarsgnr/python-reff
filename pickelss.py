import pickle
import requests
r = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
data = r.text
n = data.split("\n")
nn= [item.split(",") for item in n]
file_obj = open("mydata.pkl","wb")
pickle.dump(n,file_obj)
file_obj.close()



# with open("mydata.pkl","rb") as f:
#     print(pickle.load(f))