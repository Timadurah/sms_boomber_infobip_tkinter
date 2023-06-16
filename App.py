import http.client
import urllib.parse
import tkinter as tk
from tkinter import *

# set ctk
root = tk.Tk()
# set the window size
root.geometry("500x600")
# give it title
root.title("SMS BOOMBER")
# Set the window icon
# root.iconbitmap("icon.ico")
#  set bg color
root.configure(bg='black')

# set k for loop count
k = 0
# textvar for result
labelText = StringVar()
# function to run forms and api


def sms_send_tim():
    passwordy = password_entry.get()
    namey = username_entry.get()
    urlly = Base_url_entry.get()
    iddy = Sender_id_entry.get()
    Textty = urllib.parse.quote(Text_box_entry.get())
    Pho = Phones_entry.get().replace(" ", "")
    Phoney = Pho.replace("+", "")
    listy = [Phoney]
    clist = len(listy)

    conn = http.client.HTTPSConnection(urlly)
    payload = ''

    for phone in listy:
        global my_text
        my_text = k+1
        headers = {
            'Accept': 'application/json'
        }
        conn.request("GET", "/sms/1/text/query?username="+namey+"&password="+passwordy+"&from="+iddy+"&to="+phone+"&text="+Textty +
                     "&flash=false&transliteration=TURKISH&languageCode=TR&intermediateReport=true&notifyUrl=https://www.example.com&notifyContentType=application/json&callbackData=callbackData&validityPeriod=720&track=URL&trackingType=Custom%20tracking%20type", payload, headers)
        res = conn.getresponse()
        data = res.read()

        f = open("./Infobip.txt", "w")
        f.write(data.decode("utf-8"))
        f.close()
        print(data.decode("utf-8"))
        ltv = my_text, 'Message sent out of', clist
        labelText.set(ltv)


frame = tk.Frame(master=root, bg="#28231D")
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = tk.Label(master=frame, text="INFOIP SMS BOOMBER",
                 bg="black", fg="white")
label.pack(pady=12, padx=10)
resulty = tk.Label(master=frame, textvariable=labelText, bg="#28231D")
resulty.pack(pady=12, padx=10)

label_username = tk.Label(master=frame, text="User Name", bg="#28231D" , fg="white" )
label_username.pack()
username_entry = tk.Entry(
    master=frame, text="Username",)
username_entry.pack(pady=12, padx=10)

label_password = tk.Label(master=frame, text="Password", bg="#28231D" , fg="white" )
label_password.pack()
password_entry = tk.Entry(
    master=frame, text="Account password",)
password_entry.pack(pady=12, padx=10)


label_url = tk.Label(master=frame, text="Api Url", bg="#28231D" , fg="white" )
label_url.pack()
Base_url_entry = tk.Entry(
    master=frame, text="Base url",)
Base_url_entry.pack(pady=12, padx=10)


label_ID = tk.Label(master=frame, text="Sender ID", bg="#28231D" , fg="white" )
label_ID.pack()

Sender_id_entry = tk.Entry(
    master=frame, text="Sender ID",)
Sender_id_entry.pack(pady=12, padx=10)


label_textbox = tk.Label(master=frame, text="Text info", bg="#28231D" , fg="white" )
label_textbox.pack()
Text_box_entry = tk.Entry(
    master=frame, text="Text Box",)
Text_box_entry.pack(pady=12, padx=10)



label_Phone = tk.Label(master=frame, text="Phones seperate with comma", bg="#28231D" , fg="white" )
label_Phone.pack()
Phones_entry = tk.Entry(
    master=frame )
Phones_entry.pack(pady=12, padx=10)

button = tk.Button(
    master=frame, text="Broadcast", width=50, command=sms_send_tim)
button.pack(pady=12, padx=10)

# upl = tk.Button(
#     master=frame, text='Open', command=UploadAction)
# upl.pack()

# checkbox = tk.CheckBox(master=frame, text="remember me")
# checkbox.pack(pady=12, padx=10)

root.mainloop()


# thanks
