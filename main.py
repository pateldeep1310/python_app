from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty, StringProperty
from kivy.core.window import Window
from filemanager import MDFileManager
from kivymd.theming import ThemableBehavior
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.picker import MDThemePicker

Window.size = (360, 600)


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
class ContentNavigationDrawer(BoxLayout):
    pass


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        '''Called when tap on a menu item.'''

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

class Display_main(Screen):
    pass


class Mainscreen(Screen):
    pass

class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()

class Img2pdfscreen(Screen):
    pass

class Pdf2imgscreen(Screen):
    pass

class File_manager(Screen):
    pass

class Aboutscreen(Screen):
    pass
class NavigationDrawer (object):
    pass


sm = ScreenManager()
sm.add_widget(Mainscreen(name="mainscr"))
sm.add_widget(Pdf2imgscreen(name="pdf2imgscr"))
sm.add_widget(Img2pdfscreen(name="img2pdfscr"))
sm.add_widget(File_manager(name="filemanagerscr"))
sm.add_widget(Aboutscreen(name="aboutscr"))

class PdfApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Window.bind(on_keyboard=self.events)
        self.theme_cls.primary_palette = "Green"
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            ext=[".pdf"],
            select_path=self.select_path, previous=True,
        )





    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()

    def build(self):
        return

    def open_filemanager(self):
        self.file_manager.show("/")
        self.manager_open = True

    def select_path(self, path):
        # self.exit_manager()
        print(path)

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()

    def change_screen(self, name, *args):
        if "is_drawer_call" in args:
            self.root.ids.manager.transition.direction = "right"
            self.root.ids.manager.current = name
            self.root.ids.nav_drawer.set_state('close')
        else:
            self.root.ids.manager.transition.direction = "right"
            self.root.ids.manager.current = name
    def deep(self):
        print("nice")






        return Screen



PdfApp().run()
