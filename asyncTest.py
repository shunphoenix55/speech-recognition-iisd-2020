import asyncio
import threading
import time
import speech_recognition as sr 
r = sr.Recognizer()
def speech():
    with sr.Microphone() as source:
       print("Say something!")
       audio = r.listen(source)
    try:
       sentence = r.recognize_google(audio)
       return sentence
    except sr.UnknownValueError:
       print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
       print("Could not request results from Google Speech Recognition service; {0}".format(e))   
    

async def loop():
    while True:
        await asyncio.sleep(120)
        print("test")

async def hello():
    while True:
        await asyncio.sleep(60)
        print("hi")

async def print_speech():
    while True:
        await asyncio.sleep(5)
        sentence = speech()
        print("You said", sentence)
        if sentence != None and sentence.lower()[0:3] == "hey":
            print("hello user")


async def main():
    await asyncio.gather(loop(), hello())#, print_speech())

threading._start_new_thread(asyncio.run, (print_speech(), ))
asyncio.run(main())
#asyncio.run(loop())
#asyncio.run(hello())
#asyncio.create_task(loop())

