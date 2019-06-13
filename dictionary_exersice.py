data= {  
        "cat":"cat is called billi in hindi",
        "dog":"dog is called kutta in hindi",
        "elephent":"elephent is called hathi in hindi",
        "horse":"horse is called ghoda in hindi",
        "fish":"fish is called machli in hindi"
      }

word = input("enter a word from(cat, dog, elephent, horse, fish):")
if word not in data:
    print("word not found in dictonary")
else:
    print(data[word])