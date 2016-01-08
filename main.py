from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView

class Add(ModalView):
	def dismis(self):
		super(Add, self).dismiss()

class MainWidget(BoxLayout):
	def showDialog(self):
		Add().open()

class SDApp(App):
    def build(self):
        return MainWidget(size_hint = (1, 1))

SDApp().run()
