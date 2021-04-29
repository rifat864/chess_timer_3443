

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.clock import Clock

__version__ = 1.0
version = 1.0

def color(colorinput):
    color_out = []
    for i in colorinput:
        color_out.append(i/255)
    return color_out


Window.clearcolor = color((255, 255, 255, 255))


class MyApp(App):
    def __init__(self):
        super().__init__()
        self.min = '08'

        self.button = Button(
            text=self.min+':00',
            font_size=100,

        )

        self.button.bind(on_press=self.butt_pres1)
        self.button.background_color = color((56,56,56, 255))

        self.button1 = Button(
            text=self.min+':00',
            font_size=100
        )
        self.button1.bind(on_press=self.butt_pres2)
        self.button1.background_color = color((56,56,56, 55))

        self.button_restart = Button(
            text='reser',
            font_size=30,

        )
        self.button_restart.bind(on_press=self.butt_reset)
        self.button_pl = Button(
            text='+',
            font_size=30,

        )
        self.button_pl.bind(on_press=self.butt_pl)
        self.button_mn = Button(
            text='-',
            font_size=30
        )
        self.button_mn.bind(on_press=self.butt_mn)
        self.button_st = Button(
            text='||',
            font_size=30
        )
        self.button_st.bind(on_press=self.butt_st)

        self.active = 3
        self.t = 100
    def on_start(self):
        Clock.schedule_interval(self.time, 1)

    def time(self, *args):
        if self.button.text[:2] == 'Пр':
            return
        if self.active == 1:

            min = int(self.button.text[:2])
            min1 = self.button.text[:2]
            sec = int(self.button.text[3:])
            print(min, sec)
            if sec != 0:
                sec-=1
                if len(list(str(sec))) == 1:
                    sec = '0' + str(sec)
            else:
                sec = 59
                if min == 0:
                    self.button.text = 'Проигрышь'
                    return
                else:
                    min -= 1
                    if len(list(str(min))) == 1:
                        min1 = '0' + str(min)
                    else:
                        min1 = min

            self.button.text = str(min1) + ':' + str(sec)
        elif self.active == 2:
            min = int(self.button1.text[:2])
            min1 = self.button1.text[:2]

            sec = int(self.button1.text[3:])

            if sec != 0:
                sec -= 1
                if len(list(str(sec))) == 1:
                    sec = '0' + str(sec)
            else:
                sec = 59
                if min == 0:
                    self.button1.text = 'Проигрышь'

                    return
                else:
                    min -= 1
                    if len(list(str(min))) == 1:
                        min1 = '0'+str(min)
            # if len(list(str(min))) == 1:
            #     self.button1.text = '0' + str(min) + ':' + str(sec)
            # else:
            self.button1.text = str(min1) + ':' + str(sec)


    def butt_pres1(self, widget):
        if widget.background_color[3]==1:
            self.active = 2
            widget.background_color[3] = 55/255
            self.button1.background_color = color((56, 56, 56, 255))
    def butt_pres2(self, widget):
        if widget.background_color[3]==1:
            self.active = 1
            widget.background_color[3] = 55/255
            self.button.background_color = color((56, 56, 56, 255))
    def butt_reset(self,widget):
        self.button.text = self.min+':00'
        self.button1.text = self.min + ':00'
        self.active=3
    def butt_pl(self,widget):
        if self.active==3:
            self.min = str(int(self.min) + 1)
            self.button.text = self.min+':00'
            self.button1.text = self.min + ':00'
    def butt_mn(self,widget):
        if self.active==3:
            self.min = str(int(self.min) - 1)
            if len(list(str(self.min))) == 1:
                self.min = '0' + str(self.min)
            self.button.text = self.min + ':00'
            self.button1.text = self.min + ':00'
    def butt_st(self,widget):
        self.active = 4




    def build(self):
        mainbox = BoxLayout()
        box1 = BoxLayout()
        box2 = BoxLayout()
        box_control = BoxLayout(padding=[0,0], height= 90, size_hint = (.2, 1), orientation = 'vertical')
        box_control.add_widget(self.button_restart)
        box_control.add_widget(self.button_pl)
        box_control.add_widget(self.button_mn)
        box_control.add_widget(self.button_st)

        box1.add_widget(self.button)
        box2.add_widget(self.button1)

        mainbox.add_widget(box1)
        mainbox.add_widget(box_control)
        mainbox.add_widget(box2)




        return mainbox




if __name__ == '__main__':
    MyApp().run()

