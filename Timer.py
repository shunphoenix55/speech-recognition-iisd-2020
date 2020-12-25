import time 
import threading
user_speech=input('ask:')

def countdown(user_speech):
  sentence=user_speech.split()
  
  if 'timer' in sentence:
      t = 0
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
      
  print('Times up!') 

  
countdown(user_speech)  
#try:
#  threading._start_new_thread(countdown, (user_speech, )) 
#except:
 # print("didn't work")