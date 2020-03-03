#basic Kivy GUI client for mysql database
#postponed: Kivy is not that good

from kivy.config import Config

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'resizable', True)

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.pagelayout import PageLayout
from kivy.uix.screenmanager import ScreenManager, Screen

# Batterlean modules
from BatteryData import GotionMySql as GSql


class MyApp(App):

    def a_connect2GotionDB(self, instance):
        raw_text = self.h_login.text.splitlines()

        self.GotionSql = GSql(host_path=raw_text[0],
                              user_name=raw_text[1],
                              password_code=raw_text[2],
                              db_name='GotionDB')
        self.GotionSql.connect()
        # print(self.GotionSql.fetchAllTablesName())
        self.sm.current = 'tablescreen'
        _, self.tables = self.GotionSql.fetchAllTablesName()
        self.create_droplist()

    def create_droplist(self):

        def updatelist(instance, x):
            setattr(mainbutton, 'text', x)
            self.tableSelected = x
            print(x)

        dropdown = DropDown()
        for index in self.tables:
            # When adding widgets, we need to specify the height manually
            # (disabling the size_hint_y) so the dropdown can calculate
            # the area it needs.

            btn = Button(text=index['TABLE_NAME'], size_hint_y=None, height=25)
            # for each button, attach a callback that will call the select() method
            # on the dropdown. We'll pass the text of the button as the data of the
            # selection.
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))

            # then add the button inside the dropdown
            dropdown.add_widget(btn)

            mainbutton = Button(text='Select the Table ', size_hint=(None, None), width=250,height=35)
            mainbutton.bind(on_release=dropdown.open)

            #ropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
            dropdown.bind(on_select=updatelist)

        sn2 = self.sm.get_screen(name='tablescreen')
        sn2.children[0].add_widget(mainbutton)
        return dropdown

    def initialscreen(self):
        layout = BoxLayout(orientation='vertical')
        self.h_login = TextInput(text='sw-wus-hx501q2\ndata_viewer\nwelcome123', multiline=True)
        btn = Button(text='connect to GotionDB')
        btn.bind(on_release=self.a_connect2GotionDB)
        layout.add_widget(self.h_login)
        layout.add_widget(btn)

        sn1 = Screen(name='db_config')
        sn1.add_widget(layout)
        return sn1

    def tablesscreen(self):
        layout = BoxLayout(orientation='horizontal')
        # raw_tables = self.tables.splitlines()
        sn2 = Screen(name='tablescreen')
        sn2.add_widget(layout)
        return sn2

    def pages(self):
        self.sm = ScreenManager()
        self.sm.add_widget(self.initialscreen())
        self.sm.add_widget(self.tablesscreen())
        return self.sm

    def build(self):
        return self.pages()


if __name__ == '__main__':
    MyApp().run()
