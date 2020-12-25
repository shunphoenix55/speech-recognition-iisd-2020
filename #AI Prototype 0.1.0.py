#AI Prototype 0.1.0
import speech_recognition as sr 
r = sr.Recognizer()
from datetime import datetime
from random import randint
from googletrans import Translator
import pyttsx3

engine = pyttsx3.init()

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


#Getting Current Time - completed by Faizan
def time(wahhaj_i_am_done):
    if 'time' in wahhaj_i_am_done:
        return 'The current time is ' + str(datetime.now().strftime('%H:%M'))

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

#Calculation - by Muzammil 
def calculate(user_speech = ""):
    

    #num1=int(input("Enter the first number: "))
    #num2=int(input("Enter the second number: "))
    #print("Enter the operator you want to perform"):
    #ch=input("Enter any of these operator for operation +, -, * , /  ")
    result=0
    num1 = 0
    num2 = 0

    ch_index = user_speech.find("+")
    if ch_index == -1:
        ch_index = user_speech.find("-")
        if ch_index == -1:
            ch_index = user_speech.find("*")
            if ch_index == -1:
                ch_index = user_speech.find("/")
                if ch_index == -1:
                    return
            
    ch = user_speech[ch_index]
    if user_speech[ch_index - 1] != " ":
        num1 = int(user_speech[ch_index - 1])
    else:
        num1 = int(user_speech[ch_index - 2])   

    if user_speech[ch_index + 1] != " ":
        num1 = int(user_speech[ch_index + 1])
    else:
        num1 = int(user_speech[ch_index + 2])    
    
    if ch=='+':
        result=num1+num2
    elif ch=='-':
        result=num1-num2
    elif ch=='*':
        result=num1*num2
    elif ch=='/':
        result=num1/num2
    else:
        return("char is not supported")
    return(num1,ch,num2,": ",result)

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

 #infinite loop for final execution      
while True:
    user_speech = speech()
    if user_speech == "":
        print("Nothing was detected")

    else:
        time_str = time(user_speech)
        joke_str = joke(user_speech)
        calc_str = calculate(user_speech)
        trans_str = trans(user_speech)
        for i in [time_str, joke_str, calc_str, trans_str]:
            if i:
                print(i)
                engine.say(i)
        engine.runAndWait()

  