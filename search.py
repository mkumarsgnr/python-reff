def matchWords(sentence1 ,sentence2):
    words1= sentence1.split(" ")
    words2 = sentence2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            #print(f"matching {word1} with {word2}")
            if word1.lower()==word2.lower():
                score +=1
    return score
                
    
if __name__ == "__main__":
    #matchWords("this is good","sam is so smart and it's good")
    sentences= ["this is good","sam is so smart and it's good","harry is bhkla","i love good pubg"]
    query = input("Enter the Query String :")
    #list of scores
    scores = [matchWords(query,sentence) for sentence in sentences]
    #zip bindes to lists as if a= [a,b,c] & b= [1,2,3] [ab for ab in zip(a,b)] will be [(a,1),(b,2),(c,3)]
    result = [setscore for setscore in sorted(zip(scores, sentences),reverse =True)]
    for score, data in result:
        print(f"\"{data}\" : the score is {score}")
     