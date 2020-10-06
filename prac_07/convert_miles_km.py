from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKilometresApp(App):
    """ MilesToKilometresApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "Miles To Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, value):
        """ handles the conversion of miles to kilometres """
        result = value * 1.609344
        self.root.ids.output_label.text = str(result)

MilesToKilometresApp().run()
