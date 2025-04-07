from kivy.app import App
from kivy.uix.label import Label

class KYCApp(App):
    def build(self):
        return Label(text="KYC App Running...")

if __name__ == "__main__":
    KYCApp().run()
