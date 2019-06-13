
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(str)
if __name__ == "__main__":
    def fetchnews():
        import requests 
        import json
        d = requests.get('https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=3df9ae509eca44c0886a505f1e7b357e')
        data = d.text
        data1 = json.loads(data)
        
        for i in range(1,11):
            g = str(i)
            speak(f"News number {g} is")
            speak(data1["articles"][i]["title"])

fetchnews()