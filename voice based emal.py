
# gui program for voice based email

# complete program to read and send email



import speech_recognition as sr
import pyttsx3
import smtplib
from email.message import EmailMessage


listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print("listening......")
            voice = listener.listen(source,1,4)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass



def send_email(receiver,subject,message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('tripathimihir2002@gmail.com','2002mihir2002')  #my email and password
    email = EmailMessage()
    email['from'] = 'tripathimihir2002@gmail.com'
    email['to'] = receiver
    email['subject'] = subject
    email.set_content(message)
    server.send_message(email)
    talk('Thankyou sir for using me. Your email has been send')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()
    else:
        talk('thank you for usimg me')


email_list={
    'tom':'manjitmax69@gmail.com',
    'tiger':'mihirtripathi69@gmail.com',
    'boy':'skt63377@gmail.com'
}

def get_email_info():
    talk('Hi Sir I am your assistant for today, To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)





# email reading part

import imaplib
import email


def read_email_from_gmail():
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login('tripathimihir2002@gmail.com','2002mihir2002')
        mail.select('inbox')

        result, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])
        for i in range(latest_email_id,first_email_id, -1):
            # need str(i)
            result, data = mail.fetch(str(i), '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    # from_bytes, not from_string
                    msg = email.message_from_bytes(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']
                    email_content = msg['body']
                    talk(email_from)
                    print ('From : ' + email_from + '\n')
                    talk(email_subject)
                    print ('Subject : ' + email_subject + '\n')
                    talk(email_content)
                    print('body : '+email_content+ '\n' )

# nothing to print here




def start_up():
    talk('Hi Sir I am your assistant for today, To send email speak "send", To read email speak "read"')
    info_g = get_info()
    if 'send' in info_g:
        get_email_info()
    elif 'read' in info_g:
        read_email_from_gmail()
    else:
        talk('sorry i am unable to answer this')
        exit()


from tkinter import *
from PIL import ImageTk,Image

root = Tk()

root.title('mihir')
root.geometry('2000x3000')

img = ImageTk.PhotoImage(Image.open('mihir img.jpg'))
panel = Label(root, image=img)
panel.pack(side='right',fill='both',expand='no')

userText = StringVar()

userText.set('hi there plz speak')
userFrame = LabelFrame(root,text='mihir',font=('Railway',24,'bold'))
userFrame.pack(fill='both',expand='yes')

top = Message(userFrame,textvariable=userText,bg='black',fg='white')
top.config(font=("Century Gothlic",15,'bold'))
top.pack(side='top',fill='both',expand='yes')

btn = Button(root,text='run',font=('railway',10,'bold'),bg='red',fg='white',command=start_up).pack(fill='x',expan='no')
btn2 = Button(root,text='Close',font=('railway',10,'bold'),bg='yellow',fg='black',command=root.destroy).pack(fill='x',expan='no')
root.mainloop()