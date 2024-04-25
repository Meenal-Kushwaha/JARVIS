import requests # type: ignore
import json
import pyttsx3 # type: ignore

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    api_dict={"business":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey"
                         "=ec88f722395e415f80969ccd83b14555",
             "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey"
                              "=ec88f722395e415f80969ccd83b14555",
             "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey"
                              "=ec88f722395e415f80969ccd83b14555",
             "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey"
                              "=ec88f722395e415f80969ccd83b14555",
             "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey"
                              "=ec88f722395e415f80969ccd83b14555",
             "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey"
                              "=ec88f722395e415f80969ccd83b14555"
}

    content =None
    url=None
    speak("which field news do you want, [business],[health],[technology],[sports],[entertainment],[science] :")
    field=input("Type field news that you want:")
    for key, value in api_dict.items():
        if key.lower() in field.lower():
            url=value
            print(url)
            print("url was found")
            break
        else:
            url= True
            if url is True:
                print("url not found")



    news =requests.get(url).text
    news=json.loads(news)
    speak("here is the first news")


    arts= news["articles"]
    for articles in arts:
        article= articles["title"]
        print(article)
        speak(article)
        news_url=articles['url']
        print(f"for n=more info visist :{news_url}")

        a=input("[press 1 to cont] and [press 2 to stop]")
        if str(a)== "1":
            pass
        elif str(a)=="2":
            break

        speak("thats all")
