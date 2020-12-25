import pyowm

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
    owm = pyowm.OWM(api_key='94fed34093702faedbd32bd357fbbd4b')
    mgr = owm.weather_manager()

    obs = mgr.weather_at_place(city)
    w = obs.weather
    k = w.status
    x = w.temperature(unit='celsius')
    return('The Current weather in %s is %s.\
    \n The maximum temperature is %0.2f\
    \n and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))

user_speech = input("Enter input: ")
print(get_weather(user_speech))