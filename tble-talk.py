#(speech synthesis-librry)
import pyttsx3
n = input("Enter a number:")
dic = {
    "1":"ones",
    "2":"twos",
    "3":"threes",
    "4":"fours",
    "5":"fives",
    "6":"sixes",
    "7":"sevens",
    "8":"eights",
    "9":"nines",
    "10":"tens"
}
txt = ""
for i in range(1,11):
    mul = i*int(n)
    #1 eights are eight
    txt = txt + str(i) + " " + dic[n] + " are " + str(mul) + "\n"
# print(txt)
#(creating engine for speech synthesis)
engine  = pyttsx3.init()
engine.say(txt)
#(to execute)
engine.runAndWait()