#metodo con screen

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.carousel import MDCarousel
from kivymd.uix.card import MDCard
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

Window.size = (350, 580)


class Card(MDCard):
    text = StringProperty()

#las distintas pantallas
class Inicio(Screen):
    pass

class Login(Screen):
	pass

class Registro(Screen):
    pass

class Nexo(Screen):
    pass

class Admin(Screen):
    pass

class ProductosAdmin(Screen):
    def on_enter(self):
        for i in range(5):
            item = OneLineListItem(text=f'Elemento {i} de la lista 1')
            self.ids.list1.add_widget(item)

class Clientes(Screen):
    def on_enter(self):
        for i in range(5):
            item = OneLineListItem(text=f'Elemento {i} de la lista 2')
            self.ids.list2.add_widget(item)

class Tienda(Screen):
    def build(self):
        layout = GridLayout(cols=2, padding=10, spacing=10)
        for i in range(10):
            card = Card(text=f"Card {i}")
            layout.add_widget(card)
        return layout

#barra de navegacion

class ContentNavigationDrawer(MDBoxLayout):
    pass

#la cosa normal
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        Builder.load_file('pantallas.kv')

        #screen manager (lo que controlo las rutas de las pantallas)
        sm = ScreenManager()
        sm.add_widget(Inicio(name = 'ini'))
        sm.add_widget(Login(name = 'login'))
        sm.add_widget(Registro(name = 'registro'))
        sm.add_widget(Nexo(name = 'nexo'))
        sm.add_widget(Admin(name = 'admin'))
        sm.add_widget(ProductosAdmin(name = 'productoAdmin'))
        sm.add_widget(Clientes(name = 'clientes'))
        sm.add_widget(Tienda(name = 'tienda'))
        
        return sm

    def on_start(self):
        self.fps_monitor_start()     

if __name__ == '__main__':
    MainApp().run()
