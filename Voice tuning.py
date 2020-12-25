def tune():
    import pyttsx3
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 169)

    volume = engine.getProperty('volume')
    engine.setProperty('volume',3.0)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    inp=input("Enter string to say:")
    engine.say(inp)
    engine.runAndWait()
    engine.stop()

tune()    
