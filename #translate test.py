from googletrans import Translator
#translate test
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
    print(ind1)
    print(ind2)
    for i in range(ind1+1, ind2):
        newstr += lst[i] + " " 
        print(newstr)
    print(newstr)
    #translator.detect(newstr)
    dest_index = -(lst[::-1].index("to")) 
    print(dest_index)
    print(lst[dest_index])
    try:
       OP = translator.translate(newstr,dest=lst[dest_index])
       return OP.text
    except ValueError:
       print("Sorry, you haven't mentioned a valid language")

while True:
    trans(input("Enter input: "))
