import win32com.client
import speech_recognition as sr
import webbrowser
import os
import datetime
import wikipedia
import smtplib
import random
import time
import pyautogui
import pynput.keyboard as control
import speedtest
from tkinter import Tk, Label
from PIL import Image, ImageTk, ImageSequence
import pygame
from pygame import mixer
from googletrans import Translator,LANGUAGES
from gtts import gTTS



alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digit=["1","2","3","4","5","6","7","8","9","10"]
num={"one":1,"two":2,"three":3,"four":4,"five":6,"six":6}
sites=[["youtube","https://www.youtube.com"],["instagram","https://www.instagram.com"],["wikipedia", "https://www.wikipedia.com"]]
mails={"harry":"gcmadeacc82@gmail.com","raju":"gulationtop12@gmail.com"}
app=[["python",r"C:\Program Files\JetBrains\PyCharm Community Edition 2024.2.3\bin\pycharm64.exe"],["cmd",r"C:\Users\kalas\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools"]]
lst=["stone","paper","scissor"]
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("hello i am jarvis ai")
print("hello i am jarvis ai")
mixer.init()

def play_music():
    music_path = r"C:\Users\kalas\Downloads\kanye.mp3"
    try:
        mixer.music.load(music_path)
        mixer.music.play()
    except Exception as e:
        print(f"Error loading music: {e}")

def play_gif(root):
    root.lift()
    root.attributes("-topmost", True)

    global img
    try:
        img = Image.open("C:\\Users\\kalas\\Downloads\\bobmarley.gif")
        lbl = Label(root)
        lbl.place(x=0, y=0)
        frames = [ImageTk.PhotoImage(img.resize((1366, 768))) for img in ImageSequence.Iterator(img)]
        total_time =6000
        frame_duration = total_time // len(frames)

        def update_gif(frame_index):
            if frame_index < len(frames):
                lbl.config(image=frames[frame_index])
                root.after(frame_duration, update_gif, frame_index + 1)
            else:
                root.destroy()
        update_gif(0)
    except Exception as e:
        print(f"Error playing GIF: {e}")
       

def text(a):
    query=a
    speaker.Speak(query)
def talk():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        try:
            audio=r.listen(source,phrase_time_limit=5)
            query=r.recognize_google(audio,language="en-in")
            print(f"user said {query}")
            return query
        except Exception as e:
            return "sorry some error occured"
def music():
    l=[]
    for i in os.listdir("C:\songs"):
        l.append(i)
        ran=random.choice(l)
        music="C:\songs\\"+ran
        os.startfile(music)
def stop():
    exit()
def alarm(rec1):
    now=datetime.datetime.now()
    rep=rec1.replace(".","")
    print()
    print(rep)
    
    
    while True:
        now=datetime.datetime.now()
        current=now.strftime("%I:%M %p").lower()
        

        
        if current==rep.lower():
            print("wakeup...its time")
            text("wakeup...its time")
            os.startfile(r"C:\songs\128-Jo Bhi Main - Rockstar 128 Kbps.mp3")
            break
        
        time.sleep(5)
def volumeup():
    keyboard=control.Controller()
    for i in range(5):
        keyboard.press(control.Key.media_volume_up)
        keyboard.release(control.Key.media_volume_up)
        time.sleep(0.1)
def volumedown():
    keyboard=control.Controller()
    for i in range(5):
        keyboard.press(control.Key.media_volume_down)
        keyboard.release(control.Key.media_volume_down)
        time.sleep(0.1)

    
def gen():
    print("generating")
    password=""
    password=password+random.choice(alpha).upper()
    for i in range(5):
        password=password+random.choice(alpha)
    password+="@"
    for i in range(2):
        password+=random.choice(digit)
    print(password)
    text(password)
        
        
    
    
 
def closedtabs(tabs):
    flag=0
    for i in range(tabs):
        try:
            time.sleep(5)
            pyautogui.hotkey("ctrl","w")
            
            time.sleep(1)
        except:
            print("some error occured")
            
            flag=1
        print(f'tabs closed {tabs}' ) 
    if flag==1:
        print("give command again")
        text("give command again")
        talk()
    else:
        pass


def greet():
    current_hour = datetime.datetime.now().hour
    
    if current_hour < 12:
        
        time_of_day = "morning"
    elif 12 <= current_hour < 18:
        time_of_day = "afternoon"
    else:
        time_of_day = "evening"
    return f"Good {time_of_day}, kalash! what can i do for you!"

    

def sendmail(to,sub,datas):
    with open("password1.txt", "r") as f:
        password = f.read().strip()
    text = f"Subject: {sub}\n\n{datas}" 
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls() 
        server.login("gcmadeacc82@gmail.com", password)
        server.sendmail("gcmadeacc82@gmail.com",to, text)
        print(f"Mail sent successfully to: {to}")
    except Exception as e:
        print(f"Failed to send mail: {e}")
    finally:
        server.quit()
with open("jarvispassw.txt") as f:
    print("you have 3 attempts only")
    text("you have 3 attempts only")
    datas=f.read()
m=0
for i in range(3):
    choice=input("enter the password:  ")
    if choice==datas:
        print("correct ")
        time.sleep(1)
        m=m+1
       
        break
    else:
        continue
if m==3:
    print("wrong password")
    text("cant use jarvis ai")

            
       
                    
        
if __name__ == "__main__" and choice==datas:
    root = Tk()
    root.geometry("1366x768")
    root.title("Music and GIF Player")
    play_music()
    play_gif(root)
    root.mainloop()
    while True:
        
                
    
    

        flag=0
       
        print('LISTENING....')
        text("listening")
        data=talk()
        if "hello jarvis" in data.lower():
            stored=greet()
            text(stored)
        if "go to sleep" in data.lower():
             
             print("going..")
             text("going")
             exit()
        if "open"in data.lower():
            re=data.replace("open","")
            re=re.replace("jarvis","")              
            try:
                pyautogui.press("super")
                pyautogui.typewrite(re)
                pyautogui.press("enter")
                time.sleep(1)
              
                print("opening...")
                text("opening")
                time.sleep(1)
            except:
                print("app not available on the system")
                text("app not available on the system")
        if 'translate' in data.lower():
            re=data.replace("jarvis",'')
            re=data.replace("translate",'')
            print('sure sir..')
            print(LANGUAGES)
            translator=Translator()
            text("enter the lang u want to translate")
            b=input('enter lang in which to convert:  ')
            trans=translator.translate(re,src="auto",dest=b)
            tex=trans.text
            try:
                speak=gTTS(text=tex,lang=b,slow=False)
                speak.save("voice.mp3")
                os.startfile("voice.mp3")
                time.sleep(5)
                os.remove("voice.mp3")
                text(speak)
            except:
                
                print('unable to translate')
        if "take selfie"in data.lower():
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
            print("clicking pic in 3 sec")
            text("clicking pic in 3 seconds")
            time.sleep(3)
            pyautogui.press("enter")

        for i in sites:
            if f"open {i[0]}".lower() in data.lower():
                print("worked")
                print(f" opening {i[0]}sir..")
                webbrowser.open(i[1])
                break
        if "music".lower() in data.lower():
            print("now playing....")
            text("now playing")
            music()
        
        if "stop"in data.lower():
            pyautogui.press("enter")
        if "start"in data.lower():
            pyautogui.press("enter")
            
        if "the time".lower() in data.lower():
            timenow=datetime.datetime.now()
            t=timenow.strftime("%H:%M ")
            print("Current time:", t)
            text(f"current time is {t}")
            break
        if f"repeat".lower() in data.lower():
            while True:
                print("repeating say....")
                words=talk()
                text(words)
                if "stop"in words.lower():
                    print("okay sir...")
                    break
        if "screenshot"in data.lower() or "ss of screen"in data.lower():
            print("taking now")
            time.sleep(2)
            pyautogui.keyDown('win')
            pyautogui.press('printscreen')
            pyautogui.keyUp('win')
 
            text("taken")
        for j in app:
            if f"open {j[0]}".lower() in data.lower():
                path=j[1]
                print("opening...")
                text("opening..")
                os.startfile(path)
                break
        if "shutdown"in data.lower():
            text("are you sure u want to do it")
            ans=talk()
            if "yes" in ans.lower():
                os.system("shutdown /s /t 1")
            else:
                print("okay sir.")
                text("okay sir")
            
        if "wikipedia".lower() in data.lower():
            re=data.replace("wikipedia",'')
            re=data.replace("tell",'')
            re=data.replace("something",'')
            re=data.replace("about",'')
            re=data.replace("according to",'')
            print("acc to wikipedia....")
            text("according to wikipedia....")
            try:
                result=wikipedia.summary(re,sentences=2)
                print(result)
                text(result)
            except:
                print("no results try again")
                text("no results try again")
        if "alarm" in data.lower():
            print("alarm time")
            text("alarm time")
            record1=input("enter")
            print(f"alarm set for:{record1}")
            try:
                alarm(record1)
                break
            except:
                print("sorry some erro occured")
                continue
        if "close" in data.lower():
            print("how many tabs u want to closed give a number in n tab format")
            tab=text("speak number of tabs u want to closed: ")
            store=talk()
            try:
                for i in num:
                    if i in store.lower():
                        value=num[i]
                        closedtabs(value)
                        break
                    else:
                        pass
            except:
                print("sorry error occured try again")
            
        if "play video" in data.lower():
            time.sleep(3)
            text("playing")
            pyautogui.press("k")
        if "pause" in data.lower():
            time.sleep(3)
            text("paused")
            pyautogui.press("k")
        if "mute" in data.lower():
            text("muting")
            pyautogui.press("m")
        
        if "remember that"in data.lower():
            remember=data.replace("remember that","")
            remember=data.replace("jarvis","")
            with open("remember.txt","w") as f:
                f.write(remember)
                print("stored in mind")
        if "tell me what i told you" in data.lower() or "my reminders" in data.lower():
            try:
                with open("remember.txt","r") as f:
                    re=f.read()
                    print(re)
                    text(re)
            except:
                print("there are no reminders")
                text("there are no reminders")
        if"delete my reminder" in data.lower() or "delete what i told you"in data.lower():
            try:
                os.remove("remember.txt")
                print("deleted")
                text("deleted")
            except:
                print("no reminders to be deleted")
                text("no reminders to be deleted")
        if"password generator"in data.lower() or "password maker"in data.lower() or "generate"in data.lower():
            gen()

        if "test speed" in data.lower()or 'speed'in data.lower():
            
            print("checking plz wait sir...")
            a=speedtest.Speedtest()
            upload=a.upload()/1048576
            rou=round(upload,2)
            print(f"uploading speed is {rou} Mbps")
            
            text(f"uploading speed is {rou} Mbps")        
            download=a.download()/1048576
            r=round(download,2)
            print(f"downloading speed is  {r} Mbps")
            text(f"downloading speed is  {r} Mbps")

            
            
        if "volume up" in data.lower():
            text("doing")
            volumeup()
        if "volume down" in data.lower():
            text("doing")
            volumedown()
        if "calculate"in data.lower():
            ans=data.replace("calculate ","")
        if "play game"in data.lower():
            text("lets play stone paper scissor")
            text("choose one")
            choice=talk()
            print(f"user choose {choice}")
            if choice in lst:
                comp=random.choice(lst)
                print(f'user choose {comp}')
                if comp==choice:
                    print("draw")
                    text("draw")
                elif choice=="stone" and comp=="scissor"or choice=="scissor" and comp=="paper" or choice=="paper" and comp=="stone":
                    print("congrats kalash you won")
                    text("congrats kalash you won")
                else:
                    print('sorry you loose')
                    text("sorry you loose")
            else:
                print("sorry try again")
        if "calculate"in data.lower():
            ans=data.replace("calculate ","")
            try:
                if "+"in data.lower():
                    ans=ans.replace("+","")
                    final=ans.split()
                    num1=int(final[0])
                    num2=int(final[1])
                    calc=num1+num2
                    print(calc)
                    text(calc)
                elif "-"in data.lower():
                    ans=ans.replace("-","")
                    final=ans.split()
                    num1=int(final[0])
                    num2=int(final[1])
                    calc=num1-num2
                    print(calc)
                    text(calc)
                elif "x"in data.lower():
                    ans=ans.replace("x","")
                    final=ans.split()
                    num1=int(final[0])
                    num2=int(final[1])
                    calc=num1*num2
                    print(calc)
                    text(calc)
                else:
                    ans=ans.replace("/","")
                    final=ans.split()
                    num1=int(final[0])
                    num2=int(final[1])
                    if num2==0:
                        print("error cant do try again")
                        talk()
                    else:
                        calc=num1/num2
                        print(calc)
                        text(calc)
            except:
                print("calculation not possible ")
                text("try again")
                talk()
                
            
        for k in mails:
            if f"email to {k}".lower() in data.lower():
                while True:
                    try:
                        print(f"writing a email to {k}....")
                        print("tell the subject")
                        text("tell the subject")        
                        subject=talk()
                        print(subject)
                        print("tell what to say")
                        text("tell what to say")
                        command=talk()
                        print(command)
                        text("are you sure u want to send this yes or no")
                        choice=input("are you sure u want to send this yes or no")
                        
                        if choice.lower()=="yes":
                            sendmail(mails[k],subject,command)
                            break
                        else:
                            continue
                    except Exception as e:
                        print(f"sorry cant send",e)
                  
                    

                    
                        
                
