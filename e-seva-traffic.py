import kivy
kivy.require('1.1.1')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="1234",database='mydatabase')

mycursor = mydb.cursor()

class Login(FloatLayout):

    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)

        self.picture()

    def picture(self):
        self.add_widget(Image(source="sriram.jpg",opacity=0.3))

        self.add_widget(Label(text="welcome to my application"))
        self.btn=Button(text='next', background_color=(0.1, 1, 1, 1), size_hint=(0.1, 0.1),pos_hint ={'x':0.45, 'y':0.35})
        self.add_widget(self.btn)
        self.btn.bind(on_press=self.callback)

    def callback (self,instance):

        print("called jolly")
        self.clear_widgets()
        Window.clearcolor=(0.5,0.5,1,1)
        self.btn1=Button(text='ADMIN',background_color=(0.1,1,1,1),size_hint=(0.2,0.1),pos_hint ={'x':0.25, 'y':0.5})
        self.btn2=Button(text='COP',background_color=(0.1,1,1,1),size_hint=(0.2,0.1),pos_hint ={'x':0.45, 'y':0.5})
        self.btn3=Button(text='PUBLIC', background_color=(0.1, 1, 1, 1), size_hint=(0.2, 0.1),
                               pos_hint={'x': 0.65, 'y': 0.5})
        self.add_widget(self.btn1)
        self.add_widget(self.btn2)
        self.add_widget(self.btn3)
        self.btn1.bind(on_press=self.admin)
        self.btn2.bind(on_press=self.cop)
        self.btn3.bind(on_press=self.public)

    def admin(self, instance):
        print("admin pressed")
        self.clear_widgets()
        self.add_widget(Label(text="Admin Login",pos_hint ={'x':0, 'y':0.4},color=(0,0,0,1),font_size="20sp",bold=True))
        self.btn4 = Button(text='COP', background_color=(0.4, 1, 1, 1), size_hint=(0.2, 0.1),
                           pos_hint={'x': 0.4, 'y': 0.75})
        self.add_widget(self.btn4)
        self.add_widget(
            Label(text="Admin Registration", pos_hint={'x': 0, 'y': -0.0025}, color=(0, 0, 0, 1), font_size="20sp", bold=True))
        self.btn5 = Button(text='admin', background_color=(0.6, 0.01, 0.8, 1), size_hint=(0.2, 0.1),
                           pos_hint={'x': 0.4, 'y': 0.3})
        self.add_widget(self.btn5)
        self.btn4.bind(on_press=self.login)
        self.btn5.bind(on_press=self.admin_registration)
    def cop(self, instance):
        print("cop pressed")
        self.clear_widgets()
        self.add_widget(
            Label(text="cop Login", pos_hint={'x': 0, 'y': 0.4}, color=(0, 0, 0, 1), font_size="20sp", bold=True))
        self.btn6 = Button(text='COP', background_color=(0.4, 1, 1, 1), size_hint=(0.2, 0.1),
                           pos_hint={'x': 0.4, 'y': 0.75})
        self.add_widget(self.btn6)
        self.add_widget(
            Label(text="cop Registration", pos_hint={'x': 0, 'y': -0.0025}, color=(0, 0, 0, 1), font_size="20sp",
                  bold=True))
        self.btn7 = Button(text='COP', background_color=(0.6, 0.01, 0.8, 1), size_hint=(0.2, 0.1),
                           pos_hint={'x': 0.4, 'y': 0.3})
        self.add_widget(self.btn7)
        self.btn6.bind(on_press=self.login)
        self.btn7.bind(on_press=self.cop_registration)

    def public (self, instance):
        print("cop pressed")
        self.clear_widgets()
        self.add_widget(
            Label(text="public Login", pos_hint={'x': 0, 'y': 0.4}, color=(0, 0, 0, 1), font_size="20sp", bold=True))
        self.btn8 = Button(text='Public', background_color=(0.4, 1, 1, 1), size_hint=(0.2, 0.1),
                           pos_hint={'x': 0.4, 'y': 0.75})
        self.add_widget(self.btn8)
        self.add_widget(
            Label(text="Public Registration", pos_hint={'x': 0, 'y': -0.0025}, color=(0, 0, 0, 1), font_size="20sp",
                  bold=True))
        self.btn9 = Button(text='Public', background_color=(0.6, 0.01, 0.8, 1), size_hint=(0.2, 0.1),
                           pos_hint={'x': 0.4, 'y': 0.3})
        self.add_widget(self.btn9)
        self.btn6.bind(on_press=self.login)

    def login(self, instance):
        self.clear_widgets()
        self.add_widget(
            Label(text="USERNAME :", pos_hint={'x': -0.1, 'y': 0.1}, color=(0, 0, 0, 1), font_size="20sp", bold=True))
        self.layout=FloatLayout(size=(300,300))

        self.username = TextInput(multiline=False,size_hint=(0.2, 0.1), pos_hint={'x': 0.5, 'y':0.55})

        self.add_widget(self.username)
        self.add_widget(
            Label(text="PASSWORD :", pos_hint={'x': -0.1, 'y': -0.15}, color=(0, 0, 0, 1), font_size="20sp", bold=True))
        self.password = TextInput(multiline=False, size_hint=(0.2, 0.1), pos_hint={'x': 0.5, 'y': 0.3},password=True)
        self.add_widget(self.password)
        self.btn10 = Button(text='SUBMIT', background_color=(0.6, 0.01, 0.8, 1), size_hint=(0.2, 0.1),
                           pos_hint={'x': 0.5, 'y': 0.2},on_press=self.submit)
        self.add_widget(self.btn10)
    def admin_registration(self, instance):
        self.clear_widgets()

        position = 'ADMIN'

        self.add_widget(Label(text="ADMIN REGISTRATION",font_size="30sp", bold=True,pos_hint={'x': 0.05, 'y':0.4}))
        self.add_widget(Label(text="NAME", font_size="20sp", bold=True, pos_hint={'x': 0, 'y': 0.25}))
        self.tx1 = TextInput(multiline=False, size_hint=(0.2, 0.1), pos_hint={'x': 0.55, 'y': 0.7})
        self.add_widget(Label(text="AGE", font_size="20sp", bold=True, pos_hint={'x': 0, 'y': 0.12}))
        self.tx2 = TextInput(multiline=False, size_hint=(0.1, 0.1), pos_hint={'x': 0.6, 'y': 0.55})
        self.add_widget(Label(text="PHONE_NO", font_size="20sp", bold=True, pos_hint={'x': 0, 'y': 0.02}))
        self.tx3 = TextInput(multiline=False, size_hint=(0.1, 0.1), pos_hint={'x': 0.6, 'y': 0.45})
        self.add_widget(Label(text="ADDRESS", font_size="20sp", bold=True, pos_hint={'x': 0, 'y': -0.1}))
        self.tx4 = TextInput( size_hint=(0.1, 0.1), pos_hint={'x': 0.6, 'y': 0.35})
        self.add_widget(Label(text="GENDER", font_size="20sp", bold=True, pos_hint={'x': 0, 'y': -0.2}))
        self.tx5 = TextInput(multiline=False, size_hint=(0.1, 0.1), pos_hint={'x': 0.6, 'y': 0.25})

        self.add_widget(self.tx1)
        self.add_widget(self.tx2)
        self.add_widget(self.tx3)
        self.add_widget(self.tx4)
        self.add_widget(self.tx5)




    def cop_registration(self, instance):
        position = 'COP'
    def submit (self,obj):
        self.clear_widgets()
        self.usr=self.username.text
        self.psw=self.password.text
        print(self.usr,self.psw)
        sql1 = "SELECT * FROM users WHERE ID=%s AND PHONENO=%s"
        adr1=(self.username.text,self.password.text,)
        mycursor.execute(sql1,adr1)
        myresult = mycursor.fetchall()

        print(len(myresult))
        if (len(myresult)>0):
            for x in myresult:
                print(x[6])
                self.add_widget(Label(text="FINE AMOUNT "+str(x[6]), font_size="50sp", bold=True,))
                self.add_widget(Button(text='PAY',size_hint=(0.2,0.2), pos_hint={'x': 0.4, 'y': 0.2},background_color=(1, 0.01, 0.8, 1)))

        else:
           self.login1()
    def login1(self):
        self.clear_widgets()
        self.add_widget(
            Label(text="USERNAME :", pos_hint={'x': -0.1, 'y': 0.1}, color=(0, 0, 0, 1), font_size="20sp", bold=True))
        self.layout=FloatLayout(size=(300,300))

        self.username = TextInput(multiline=False,size_hint=(0.2, 0.1), pos_hint={'x': 0.5, 'y':0.55})

        self.add_widget(self.username)
        self.add_widget(
            Label(text="PASSWORD :", pos_hint={'x': -0.1, 'y': -0.15}, color=(0, 0, 0, 1), font_size="20sp", bold=True))
        self.password = TextInput(multiline=False, size_hint=(0.2, 0.1), pos_hint={'x': 0.5, 'y': 0.3},password=True)
        self.add_widget(self.password)
        self.btn10 = Button(text='SUBMIT', background_color=(0.6, 0.01, 0.8, 1), size_hint=(0.2, 0.1),
                           pos_hint={'x': 0.5, 'y': 0.2},on_press=self.submit)
        self.add_widget(self.btn10)

class Traffic_e_seva(App):
    def build(self):
        return Login()

if __name__=='__main__':
    Traffic_e_seva().run()