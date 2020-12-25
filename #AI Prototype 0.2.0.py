#AI Prototype 0.2.0
import speech_recognition as sr 
r = sr.Recognizer()
from datetime import datetime
from random import randint
from googletrans import Translator
import pyttsx3
import time
from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='d3015796d52f42d2b36cf0d61fbe7a0c')


engine = pyttsx3.init()

#Tuning the voice assistant - completed by Sabeeh
rate = engine.getProperty('rate')
engine.setProperty('rate', 169)

volume = engine.getProperty('volume')
engine.setProperty('volume',3.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)


#Speech Recognition - completed by Sabeeh
def speech():
    with sr.Microphone() as source:
       print("Say something!")
       audio = r.listen(source)
       print("processing")
    try:
       sentence = r.recognize_google(audio)
       print("You said:", sentence)
       return sentence
    except sr.UnknownValueError:
       print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
       print("Could not request results from Google Speech Recognition service; {0}".format(e))   

def introduction(user_speech):
    if "hey" in user_speech.lower() or "hi" in user_speech.lower() or "hello" in user_speech.lower():
        return "Hello User, this is your own Personal Assistant, EVA, would you like to get Started\
        or would you like to know about my Features and their Commands?"

def command_help(user_speech):
    if "command" in user_speech.lower() or "feature" in user_speech.lower():
        return """Sure thing user, these are my Awesome Features, and their Commands, 
        1, Weather changes every day, so to keep track of the Weather in your City, Command me by asking, “What’s the Weather in City-name” 

        2, Want to set a Timer? You can also ask me to set a Timer, so that the cake you are making, won’t burn.
        Just tell me, “Set a Timer for x minutes and y seconds”.

        3, So, you have lost your watch, or don’t wear a watch, and want to know the Current Time? Then you have summoned the right Personal Assistant! 
            To know the Current Time, ask me, “What’s the Time”.

        4, Don’t know what’s going around the world or in your country? Or maybe you just don’t trust the News Channels. I can help you with all the Updates of the Day.
            To know the News, command me by asking, “What’s the News for Today”?

        5, In a mood of hearing a Joke or a Pun? I have the best Jokes for you to hear, in courtesy of my Devs.
            To hear a Joke, Just say, “Tell me a Joke”
            
        6, So, you just read or heard something you don’t recognize, as it’s in another Language?
            Worry not, your Personal Assistant to the rescue!
            Command me, by asking, “Translate word to Language”"""

#Getting Current Time - completed by Faizan
def current_time(wahhaj_i_am_done):
    if 'time' in wahhaj_i_am_done:
        return 'The current time is ' + str(datetime.now().strftime('%H:%M'))

#Timer - completed by Faizan
def countdown(user_speech):
  sentence=user_speech.split()
  t = 0
  if 'timer' in sentence:
      if 'seconds' in sentence and 'minutes' not in sentence: 
        s_no=sentence.index('seconds')
        secs=int(sentence[s_no-1])
        t=secs
      elif 'minutes' in sentence and 'seconds' not in sentence:
        m_no=sentence.index('minutes')
        mins=int(sentence[m_no-1])
        t=mins*60
      elif 'minutes' in sentence and 'seconds' in sentence:
        s_no=sentence.index('seconds')
        secs=int(sentence[s_no-1])
        m_no=sentence.index('minutes')
        mins=int(sentence[m_no-1])
        t=secs+(mins*60)
      
      while t:
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs)  
        print(mins, ":", secs)
        time.sleep(1) 
        t -= 1
      else:
        return 'Times up!'
  


#Randomizing jokes - Zimran
jokes = [
  "Want to hear a construction joke? - Oh never mind, I'm still working on that one.",
  "Why don't scientists trust atoms? - Because they make up everything!",
  "Why did the gym close down? - It just didn't work out!",
  "I have a fear of speed bumps. But I am slowly getting over it.",
  "You can only get spoiled milk from a pampered cow.",
  "Why are ghosts such bad liars? - Because they are easy to see through.",
  "What did the buffalo say when his son left for college? Bison!",
  "Where do fish sleep? In the riverbed.",
  "Where are average things manufactured? - The satisfactory.",
  "Two artists had an art contest. It ended in a draw!",
  "Why are skeletons so calm? - Because nothing gets under their skin.",
  "Where does the sheep get his hair cut? - The baa baa shop!",
  "What do you call a witch that's sitting in the middle of the desert, trembling with fear? - A chicken sandwich.",
  "I hate Russian dolls...so full of themselves.",
  "I waited and stayed up all night and tried to figure out where the sun was. Then it dawned on me.",
  "Somebody actually complimented me on my driving today. They left a little note, it said Parking Fine.",
  "Why don’t lobsters like sharing? Because they’re shellfish.",
  "How do trees get online? - They just log on!",
  "Why did the M&M go to school? He wanted to be a Smartie.",
  "Why do French people eat snails? They don't like fast food!",
  "I was wondering why the frisbee was getting bigger, then it hit me.",
  "Why was six afraid of seven? Because seven ate nine.",
  "Some people think prison is one word…but to robbers it's the whole sentence.",
  "Why did the orange stop? It ran out of juice!",
  "Why doesn't the sun go to college? Because it has a million degrees!"
]

def joke(user_speech):
    if 'joke' in user_speech or 'funny' in user_speech:
        return( jokes[randint(0, len(jokes) - 1)] )

#Weather - Zimran
import pyowm
owm = pyowm.OWM(api_key='94fed34093702faedbd32bd357fbbd4b')
mgr = owm.weather_manager()
def get_weather(user_speech):    
    city = "Dammam"
    if "weather" in user_speech.lower():
        index = user_speech.find(" in ") + 4
        city = ""
        speech_len = len(user_speech)
        while index < speech_len and user_speech[index] != " ":
            city += user_speech[index]
            index += 1
    else:
        return

    obs = mgr.weather_at_place(city)
    w = obs.weather
    k = w.status
    x = w.temperature(unit='celsius')
    return('The Current weather in %s is %s.\
    \n The maximum temperature is %0.2f\
    \n and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))


def count(user_speech, start, step):
    num = 0
    exp = 1
    index = start
    speech_len = len(user_speech)
    while index < speech_len and user_speech[index].isnumeric() and index > -1 :
        if step == -1:
            num += int(user_speech[index]) * exp
        else:
            num = num * exp + int(user_speech[index])
        exp *= 10
        index += step
        #print(num)
    return num

#Calculation - by Muzammil 
def calculate(user_speech = ""):
    

    #num1=int(input("Enter the first number: "))
    #num2=int(input("Enter the second number: "))
    #print("Enter the operator you want to perform"):
    #ch=input("Enter any of these operator for operation +, -, * , /  ")
    result=0

    ch_index = user_speech.find("+")
    if ch_index == -1:
        ch_index = user_speech.find("-")
        if ch_index == -1:
            ch_index = user_speech.lower().find("x")
            if ch_index == -1:
                ch_index = user_speech.find("/")
                if ch_index == -1:
                    return
            
    ch = user_speech[ch_index]
    if user_speech[ch_index - 1] != " ":
        num1 = count(user_speech, ch_index - 1, -1) #int(user_speech[ch_index - 1])
    else:
        num1 = count(user_speech, ch_index - 2, -1)  

    if user_speech[ch_index + 1] != " ":
        num2 = count(user_speech, ch_index + 1, +1)
    else:
        num2 = count(user_speech, ch_index + 2, +1)    

    if ch=='+':
        result=num1+num2
    elif ch=='-':
        result=num1-num2
    elif ch=='x':
        result=num1*num2
    elif ch=='/':
        result=num1/num2
    else:
        print("char is not supported")
    return str(num1) + str(ch) + str(num2) + ": " + str(result)

#Translation - by Sabeeh
translator = Translator()
def trans(user_speech):
    #string=input("Enter translate string of form 'translate [text] from [input lang] to [output lang]':")
    if user_speech.find("translate") == -1:
        return
    else:
        print("translating")
    lst=user_speech.split()
    #lenght=len(lst)
    newstr=''
    ind1=lst.index("translate")
    ind2= len(lst) - lst[::-1].index("to") - 1
    for i in range(ind1+1, ind2):
        newstr += lst[i] + " " 
    translator.detect(newstr)
    dest_index = -(lst[::-1].index("to"))
    try:
       OP = translator.translate(newstr,dest=lst[dest_index])
       return OP.text
    except ValueError:
       print("Sorry, you haven't mentioned a valid language")

#News - Wahhaj
def get_news(user_speech):
    if "news" in user_speech.lower():
        top_news = newsapi.get_top_headlines()
        news_str = ""
        for i in range (0, 5):
            news_str += top_news["articles"][i]["title"] + "\n"
            news_str += top_news["articles"][i]["description"] + "\n"
        return news_str

 #infinite loop for final execution      
while True:
    user_speech = speech()
    if user_speech == None:
        print("Nothing was detected")

    else:
        intro_str = introduction(user_speech)
        help_str = command_help(user_speech)
        time_str = current_time(user_speech)
        joke_str = joke(user_speech)
        calc_str = calculate(user_speech)
        trans_str = trans(user_speech)
        countdown_str = countdown(user_speech)
        weather_str = get_weather(user_speech)
        news_str = get_news(user_speech)

        for i in [intro_str, help_str, time_str, joke_str, calc_str, trans_str, countdown_str, weather_str, news_str]:
            if i:
                print(i)
                engine.say(i)
        engine.runAndWait()

  