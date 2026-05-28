from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
class OmniSystem(MDApp):
    def build(self):
        screen = MDScreen()
        layout = MDBoxLayout(orientation='vertical', padding=50, spacing=20)
        
        title_label = MDLabel(text="Omni System Hub", halign="center", font_style="H4")
        connect_btn = MDRaisedButton(text="Connect System", pos_hint={'center_x': 0.5})
        
        layout.add_widget(title_label)
        layout.add_widget(connect_btn)
        screen.add_widget(layout)
        return screen

if __name__ == '__main__':
    OmniSystem().run()