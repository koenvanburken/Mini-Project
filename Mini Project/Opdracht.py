import requests
import xmltodict

auth_details = ('koen.vanburken@student.hu.nl', 'VoQNEG2N87W9rrn-kU4a5qVs8DaFkVfDy38z6qX5DlYK5dxvQLACmQ')
api_url = 'https://webservices.ns.nl/ns-api-avt?station=ut'
response = requests.get(api_url, auth=auth_details)

vertrekXML = xmltodict.parse(response.text)
from tkinter import *

def callback():
    print('Dit zijn de vertrekkende treinen:')
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
            eindbestemming = vertrek['EindBestemming']

            vertrektijd = vertrek['VertrekTijd']
            vertrektijd = vertrektijd[11:16]

            print('Om '+vertrektijd+' vertrekt een trein naar '+ eindbestemming)

class App:
    def __init__(self,master):
        master.geometry("700x700")

        photo = PhotoImage(file="beginscherm.png")
        self.w = w = Label (master, image=photo)
        w.photo = photo
        w.pack()

        self.actueel = Button(master,text="Actuele vertrektijden",command=callback, height=1,
                              width=20,fg= "white",bg = "darkblue")
        self.actueel.place(x=190, y=500)

        self.ad = Button(master,text="Vertrektijden Amsterdam",command=callback, height=1,
                              width=20,fg= "white",bg = "darkblue")
        self.ad.place(x=350, y=500)
root = Tk() # Creëer het hoofdscherm
app = App(root)

#label = Label(master=root,
#              text='Druk op een station voor de actuele vertrektijden',
#              background='yellow',
#              foreground='blue',
#              font=('Arial', 16, 'bold'),
#              width=50,
#              height=10)
#label.pack()

#entry = Entry(master=root)
#entry.pack(padx=10, pady=10)

#button = Button(master=root, text='Button 1')
#button.pack(side=LEFT, pady=10, fill=X, padx=50)

#button2 = Button(master=root, text='Utrecht Centraal', command=callback)
#button2.pack(side=LEFT, pady=10, fill=X, padx=50)

#button3 = Button(master=root, text='Button 3')
#button3.pack(side=TOP, pady=10)

root.mainloop() # Toon het hoofdscherm
