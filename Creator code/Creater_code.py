from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.textinput import TextInput
from kivy.uix.switch import Switch
import threading
import os
import random
class Creater_CodeApp(App):
    def callback(self,instance, value):
        if self.ghi==0:
            self.ghi=1
        elif self.ghi==1:
            self.ghi=0
    def Launch(self,args):
        text=self.ti.text
        file1=open("dp.py","r")#открываем файл
        line=""
        for p in range(32):
            # считываем строку
            lin= file1.readline()
            if not lin:
                break
            line+=lin
        file=open("proga.py","w", encoding='utf-8')
        file.write(text+line)
        file.close()
        threading.Thread(target=lambda: os.system('launch.py')).start()
    def build(self):
        self.ghi=0
        bl=BoxLayout(orientation="vertical")
        gr=GridLayout(cols=7,size_hint=(1,.1))
        self.t=TextInput(text="")
        gr.add_widget(self.t)
        gr.add_widget(Button(text="Запуск",on_press=self.Launch,size_hint=(1.1,.05)))
        gr.add_widget(Button(text="сохранить"))
        bl.add_widget(gr)
        self.ti=TextInput()
        bl.add_widget(self.ti)
        return bl
if __name__=="__main__":
    Creater_CodeApp().run()
