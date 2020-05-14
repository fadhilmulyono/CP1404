from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # Add names
        self.names = {"Geraldi Abdiel", "Alexandra Sanny", "Rendy Irvano", "Muhammad Bima", "Arthur Yamin", ""}

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_label.kv')
        for name in self.names:
            label = Label(text=name)
            self.root.ids.entries_box.add_widget(label)
        return self.root


DynamicLabelApp().run()
