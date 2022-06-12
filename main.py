from kivy.lang import Builder

from kivymd.app import MDApp


KV = '''
MDBoxLayout:
    type: "labeled"

    MDNavigationRail:
        text_color_item_normal: app.theme_cls.primary_color

        MDNavigationRailItem:
            text: "STT"
            icon: "microphone"

        MDNavigationRailItem:
            text: "TTS"
            icon: "surround-sound"

'''


class TextAndSpeech(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


if __name__ == '__main__':
    TextAndSpeech().run()
