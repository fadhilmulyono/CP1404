from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

MILES_TO_KM = 1.609


class ConvertMilesKilometres(App):
    output_km = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self, text):
        """ handle calculation (could be button press or other call), output result to label widget """
        print("Handle calculation")
        miles = self.convert_to_number(text)
        self.convert_miles_to_km(miles)

    def handle_increment(self, text, increment):
        print("Handle increment")
        miles = self.convert_to_number(text) + increment
        self.root.ids.input_miles.text = str(miles)

    def convert_miles_to_km(self, miles):
        print("Convert miles to kilometres")
        self.output_km = str(miles * MILES_TO_KM)


    @staticmethod
    def convert_to_number(text):
        """ Convert text to float, or 0.0 if invalid"""
        try:
            return float(text)
        except ValueError:
            return 0.0

ConvertMilesKilometres().run()
