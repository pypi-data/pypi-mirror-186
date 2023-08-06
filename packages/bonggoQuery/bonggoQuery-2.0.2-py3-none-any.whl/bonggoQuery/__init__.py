
# IMPORTING ALL THE PACKAGES
import wolframalpha as wf
import speech_recognition as sr
import pyttsx3
import wikipedia
# -----------------------------------------------



# SETTING THE API

app = wf.Client("3YEQYW-RA6A8LREGV")
# ------------------------------------------

# PROCESS TO SET THE VOICES
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

# ---------------------------------------------------------

# This function will help to give the output in voice
def speak(audio):
           engine.say(audio)
           engine.runAndWait()
# ------------------------------------------------


# NEW FEATURES WILL COME IN SOON
# ***********************************************************


# This finction will take input from the user in voice
def takeCommand():
            r = sr.Recognizer()
            with sr.Microphone() as m:
              print("Listening...")
              # r.pause_threshold=1
              audio = r.listen(m)

            try:
              print("Recognizing...")
              query = r.recognize_google(audio, language="eng-in").lower()
              print(f"User Said:{query}\n")
              return  query
        
            except Exception as e:
                # print(e)

                print("Say that again Please...")
                speak("Say that again Please...")
                return "null"

           
        
            
          


#*********************************************************

# This function will take the query and it will search the data in wikipedia 
          
def wikiLogic(query):
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    return results

 # *************************************************
 
#  THE CLASS TO EXECUTE ALL THE QUERY
    
    
class Query:
     
# this class will take the query and gives the input in two ways
    class normal_query():
          
          # It will give the result in printing mode
        def printing(querys):
            querys= querys.lower()
            res = app.query(querys)
            # speak(next(res.results).text)
            try: 
              return f"{(next(res.results).text)}"
            except Exception:
              try:
                return f"According to Wikipedia {wikiLogic(querys)}"
              except Exception:
                return "There is an error !"
        
        # ******************************************************
        
        # It will give the result in voice
        def speaking(querys):
            querys= querys.lower()
            res = app.query(querys)
            # speak(next(res.results).text)
            try: 
              speak(next(res.results).text)
              return f"{(next(res.results).text)}"
            except Exception:

              try:
                speak(f"According to Wikipedia {wikiLogic(querys)}")
                return f"{wikiLogic(querys)}"
              except Exception:
                speak("There is an error !")
                return "There is an error !"
          #*************************************************************
# ****************************************************************************** 