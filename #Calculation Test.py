#Calculation Test
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
        print(num)
    return num

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
            ch_index = user_speech.find("*")
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
    elif ch=='*':
        result=num1*num2
    elif ch=='/':
        result=num1/num2
    else:
        print("char is not supported")
    print(num1,ch,num2,": ",result)

x = input("Enter calculation ")
calculate(x)

'''
All right, to check for the right numbers, we do something like this 
make function

def count(user_speech, start, step):
    num = 0
    exp = 1
    index = start
    number = user_speech[start]
    while user_speech != " ":
        num += int(user_speech[index]) * exp
        exp *= 10
        index = start + step
    return num


'''