import cv2
from tkinter import*
from PIL import Image, ImageTk
from HandTrackingModule import HandDetector
from tkinter import filedialog
from gtts import gTTS
from playsound import playsound
import os
import string

Morse={'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
        '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', 
        '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', 
        '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', 
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z', '':' '}

win = Tk()
win.title("PoseVerter")
win.geometry("670x600+200+30")

frame_1 = Frame(win, width=670, height=700, bg="#91a3b0").place(x=0, y=0)
cap = cv2.VideoCapture(0)

buttonX=10
buttonY=450
w = 300
h = 200
label1 = Label(frame_1, width=w, height=h)
label1.place(x=180, y=220)

words=""
checky=False
checkx=False
checkThumb=False

Vid1=StringVar()
Vid2=StringVar()
Vid3=StringVar()
Vid4=StringVar()
Vid5=StringVar()
Vid1.set("")
Vid2.set("")
Vid3.set("")
Vid4.set("")
Vid5.set("")

bVid1=''
bVid2=''
bVid3=''
bVid4=''
bVid5=''

Words=StringVar()
Words.set("")

TTSsave='PoseverterFile'

maxVids=0

def delChar():
    global Words
    n=str(Words.get())
    m=''
    if(len(n)>0):
        for i in range(len(n)-1):
            m+=n[i]
    Words.set(m)

def Help():
    os.startfile("Help.txt")

def Play():
    global TTSsave
    language = 'en'
    n=Words.get()
    if(set(n).intersection(string.ascii_uppercase) != set()):
        myobj = gTTS(text=n, lang=language, slow=False)
    else:
        myobj = gTTS(text="Please enter some text first", lang=language, slow=False)
    TTSsave+='s'
    myobj.save('audio/'+TTSsave+'.mp3')
    playsound('audio/'+TTSsave+'.mp3')

def maxLim():
    global TTSsave
    language = 'en'
    n="Maximum Limit Reached"
    myobj = gTTS(text=n, lang=language, slow=False)
    TTSsave+='s'
    myobj.save('audio/'+TTSsave+'.mp3')
    playsound('audio/'+TTSsave+'.mp3')

def DelVid():
    global maxVids, bVid1, bVid2, bVid3, bVid4, bVid5, Vid1, Vid2, Vid3, Vid4, Vid5
    if(isinstance(bVid5,Button)):
        bVid5.place_forget()
        bVid5=''
        Vid5.set("")
        maxVids-=1
    elif(isinstance(bVid4,Button)):
        bVid4.place_forget()
        bVid4=''
        Vid4.set("")
        maxVids-=1
    elif(isinstance(bVid3,Button)):
        bVid3.place_forget()
        bVid3=''
        Vid3.set("")
        maxVids-=1
    elif(isinstance(bVid2,Button)):
        bVid2.place_forget()
        bVid2=''
        Vid2.set("")
        maxVids-=1
    elif(isinstance(bVid1,Button)):
        bVid1.place_forget()
        bVid1=''
        Vid1.set("")
        maxVids-=1

def Live():
    global cap, detector
    cap = cv2.VideoCapture(0)
    detector = HandDetector(detectionCon=0.5, maxHands=2)
    Words.set("")

def Rec(num):
    global cap, detector
    if(num==1):
        if(".mp4" not in Vid1.get()):
            m=Vid1.get()
            n=''
            o=''
            for i in range(-1, -len(m), -1):
                if m[i]=='/':
                    break
                n+=m[i]
            for i in range(-1, -len(n)-1, -1):
                o+=n[i]
            m+=("/"+str(o)+".mp4")
            Vid1.set(m)
        cap = cv2.VideoCapture(Vid1.get())
        detector = HandDetector(detectionCon=0.5, maxHands=2)
        Words.set("")
    elif(num==2):
        if(".mp4" not in Vid2.get()):
            m=Vid2.get()
            n=''
            o=''
            for i in range(-1, -len(m), -1):
                if m[i]=='/':
                    break
                n+=m[i]
            for i in range(-1, -len(n)-1, -1):
                o+=n[i]
            m+=("/"+str(o)+".mp4")
            Vid2.set(m)
        cap = cv2.VideoCapture(Vid2.get())
        detector = HandDetector(detectionCon=0.5, maxHands=2)
        Words.set("")
    elif(num==3):
        if(".mp4" not in Vid3.get()):
            m=Vid3.get()
            n=''
            o=''
            for i in range(-1, -len(m), -1):
                if m[i]=='/':
                    break
                n+=m[i]
            for i in range(-1, -len(n)-1, -1):
                o+=n[i]
            m+=("/"+str(o)+".mp4")
            Vid3.set(m)
        cap = cv2.VideoCapture(str(Vid3.get()))
        detector = HandDetector(detectionCon=0.5, maxHands=2)
        Words.set("")
    elif(num==4):
        if(".mp4" not in Vid4.get()):
            m=Vid4.get()
            n=''
            o=''
            for i in range(-1, -len(m), -1):
                if m[i]=='/':
                    break
                n+=m[i]
            for i in range(-1, -len(n)-1, -1):
                o+=n[i]
            m+=("/"+str(o)+".mp4")
            Vid4.set(m)
        cap = cv2.VideoCapture(str(Vid4.get()))
        detector = HandDetector(detectionCon=0.5, maxHands=2)
        Words.set("")
    elif(num==5):
        if(".mp4" not in Vid5.get()):
            m=Vid5.get()
            n=''
            o=''
            for i in range(-1, -len(m), -1):
                if m[i]=='/':
                    break
                n+=m[i]
            for i in range(-1, -len(n)-1, -1):
                o+=n[i]
            m+=("/"+str(o)+".mp4")
            Vid5.set(m)
        cap = cv2.VideoCapture(str(Vid5.get()))
        detector = HandDetector(detectionCon=0.5, maxHands=2)
        Words.set("")

def AddVid():
    global Vid1, Vid2, Vid3, Vid4, Vid5, bVid1, bVid2, bVid3, bVid4, bVid5 
    global maxVids
    filename = filedialog.askdirectory()
    if(filename!=""):
        if(maxVids<5):
            if(Vid1.get()==""):
                Vid1.set(filename)
                filename=""
                bVid1 = Button(frame_1,text='Video 1', height=1, width=10, relief=RAISED, cursor="hand2", command= lambda : Rec(1))
                bVid1.place(x=(buttonX+400), y=buttonY)
            elif(Vid2.get()==""):
                Vid2.set(filename)
                filename=""
                bVid2 = Button(frame_1,text='Video 2', height=1, width=10, relief=RAISED, cursor="hand2", command= lambda : Rec(2))
                bVid2.place(x=(buttonX+500), y=buttonY)
            elif(Vid3.get()==""):
                Vid3.set(filename)
                filename=""
                bVid3 = Button(frame_1,text='Video 3', height=1, width=10, relief=RAISED, cursor="hand2", command= lambda : Rec(3))
                bVid3.place(x=(buttonX+400), y=(buttonY+40))
            elif(Vid4.get()==""):
                Vid4.set(filename)
                filename=""
                bVid4 = Button(frame_1,text='Video 4', height=1, width=10, relief=RAISED, cursor="hand2", command= lambda : Rec(4))
                bVid4.place(x=(buttonX+500), y=(buttonY+40))
            elif(Vid5.get()==""):
                Vid5.set(filename)
                filename=""
                bVid5 = Button(frame_1,text='Video 5', height=1, width=10, relief=RAISED, cursor="hand2", command= lambda : Rec(5))
                bVid5.place(x=(buttonX+450), y=(buttonY+80))
        else:
            maxLim()
        if(maxVids<=4):
            maxVids+=1

def ButtonSelect():
    bAdd = Button(frame_1,text='Add Videos', height=1, width=15, relief=RAISED,cursor="hand2", command=AddVid)
    bAdd.place(x=(buttonX+200), y=buttonY)
    label1 = Label(frame_1, text="Max 5 videos",width=10, height=1, bg="#91a3b0")
    label1.place(x=(buttonX+220), y=(buttonY+30))

def select_img():
    global checkThumb, checkx, checky, Words, words, cap, detector
    success, img = cap.read()
    if(success==False):
        cap = cv2.VideoCapture(0)
        select_img()
    img=cv2.flip(img, 1)
    hands, img = detector.findHands(img,flipType=False) 
    img = cv2.resize(img, (w, h))
    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        Index_tipY=lmList1[8][1] #8 for tip of index finger, 1 for y coordinate
        Index_dipY=lmList1[7][1] #7 for dip of index finger, 1 for y coordinate
        Middle_tipY=lmList1[12][1] #12 for tip of middle finger, 1 for y coordinate
        Middle_dipY=lmList1[11][1] #11 for dip of middle finger, 1 for y coordinate
        Thumb_tipX=lmList1[4][0] #4 for tip of thumb, 0 for x coordinate
        Thumb_ipX=lmList1[3][0] #3 for ip of thumb, 0 for x coordinate
        if (Index_tipY>Index_dipY):
            checky=True
        if Index_tipY<Index_dipY and checky :
            words+='-'
            checky=False
        if (Middle_tipY>Middle_dipY):
            checkx=True
        if Middle_tipY<=Middle_dipY and checkx :
            words+='.'
            checkx=False
        if(Thumb_tipX>Thumb_ipX):
            checkThumb=True
        if Thumb_tipX<=Thumb_ipX and checkThumb:
            p=str(Words.get())
            n=p+str(Morse.get(words,''))
            Words.set(n)
            words=''
            checkThumb=False
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(imgRGB)
    finalImage = ImageTk.PhotoImage(image)
    label1.configure(image=finalImage)
    label1.image = finalImage
    win.after(1, select_img)

detector = HandDetector(detectionCon=0.5, maxHands=2)

label2= Label(frame_1, text="Welcome to PoseVerter", bg="#91a3b0", font=('Times', '14', 'bold') ).place(x=0,y=2)
label3= Label(frame_1, text="TEXT : ", bg="#91a3b0").place(x=0,y=28)
label4= Label(frame_1, text="Developed by: Hassan Niaz, Anas Ramzan", bg="#91a3b0", font=('Times', '10', 'bold')).place(x=400,y=570)
textlabel= Label(frame_1, textvariable=Words, width=92, height=10, relief=RIDGE)
textlabel.place(x=10, y=50)
b1 = Button(frame_1,text='Recorded Videos', height=1, width=20, relief=RAISED, cursor="hand2", command=ButtonSelect)
b1.place(x=buttonX, y=buttonY)
b2 = Button(frame_1,text='Live Video', height=1, width=20, relief=RAISED, cursor="hand2", command=Live)
b2.place(x=buttonX, y=(buttonY+40))
b3 = Button(frame_1,text='Delete Video', height=1, width=20, relief=RAISED, cursor="hand2", command=DelVid)
b3.place(x=buttonX, y=(buttonY+80))
b4 = Button(frame_1,text='Play', height=1, width=5, relief=RAISED, cursor="hand2", command=Play)
b4.place(x=10, y=220)
b5 = Button(frame_1,text='Help', height=1, width=5, relief=RAISED, cursor="hand2", command=Help)
b5.place(x=600, y=220)
b6 = Button(frame_1,text='Delete Char', height=1, width=10, relief=RAISED, cursor="hand2", command=delChar)
b6.place(x=500, y=220)
select_img()
win.mainloop()