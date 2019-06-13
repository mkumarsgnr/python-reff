data = {"data1":"this is data from first dictonary",
        "data2":{"data2.1":"this data from dict2",
                "data2.2":{"gg":"gu "}
                }
        }
#print(data["data2"]['data2.2']['gg'])
data['data2']["daku"]="janver"#adding data in dictonary with using key
print(data)
del data['data1']#deleting dictionary data with key 
print(data)
copy_of_data = data.copy()
print(copy_of_data) 
copy_of_data.update({"data1new":"we can also update dictonaies like this",'yeye':"yeyeyeeyeeyeyey"})#another method to update data
print(copy_of_data)
del copy_of_data['yeye']
print(copy_of_data)
print(data.get("data2"))