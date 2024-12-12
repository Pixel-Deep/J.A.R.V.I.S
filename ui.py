from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.window import Window
from datetime import datetime
import random  # For generating random numbers

# Register a custom font (update the path to your futuristic font)
LabelBase.register(name="Roboto", fn_regular="ui/dusri.ttf")  # Replace with the actual font path

class JarvisUI(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Load the background image
        self.background = Image(
            source="C:/Users/soumy/OneDrive/Desktop/J.A.R.V.I.S/ui/b.png",
            allow_stretch=True,
            keep_ratio=False
        )
        self.add_widget(self.background)

        # Add the "J.A.R.V.I.S" label at the top center
        self.title_label = Label(
            text="[b]J.A.R.V.I.S[/b]",
            font_size="70sp",
            markup=True,
            color=(0.2, 0.2, 1, 1),  # Same blue color as date/time
            font_name="ui/StalinistOne-Regular.ttf",
            size_hint=(None, None),
            pos_hint={"center_x": 0.5, "y": 0.82},  # Positioned at the top center
        )
        self.add_widget(self.title_label)

        # Center GIF with increased size
        self.gif = Image(
            source="C:/Users/soumy/OneDrive/Desktop/J.A.R.V.I.S/cbe227_fb70e39e9dd94e30bbe30c48b2367dd8~mv2.gif",
            anim_delay=0.05
        )
        self.gif.size_hint = (None, None)  # Disable automatic resizing
        self.gif.size = (1000, 1000)  # Set GIF size to 1000x1000
        self.gif.pos_hint = {"center_x": 0.5, "center_y": 0.5}  # Center it
        self.add_widget(self.gif)

        # Time and date labels
        self.time_label = Label(
            text="",
            font_size="44sp",
            color=(0.2, 0.2, 1, 1),  # Same blue color
            font_name="ui/mw.ttf",
            size_hint=(None, None),
            pos_hint={"x": 0.065, "y": 0.85}
        )
        self.add_widget(self.time_label)

        self.date_label = Label(
            text="",
            font_size="21sp",
            color=(0.2, 0.2, 1, 1),  # Same blue color
            font_name="Roboto",
            size_hint=(None, None),
            pos_hint={"x": 0.065, "y": 0.82}
        )
        self.add_widget(self.date_label)

        # Dynamic 8-digit number shuffling (left)
        self.number_label_left = Label(
            text="0",
            font_size="30sp",
            color=(0.2, 0.2, 1, 1),  # Same blue color
            font_name="Roboto",
            size_hint=(None, None),
            pos_hint={"x": 0.30, "center_y": 0.5}  # Positioned to the left of the GIF
        )
        self.add_widget(self.number_label_left)

        # Dynamic 8-digit number shuffling (right)
        self.number_label_right = Label(
            text="0",
            font_size="30sp",
            color=(0.2, 0.2, 1, 1),  # Same blue color
            font_name="Roboto",
            size_hint=(None, None),
            pos_hint={"x": 0.65, "center_y": 0.5}  # Positioned to the right of the GIF
        )
        self.add_widget(self.number_label_right)

        # Timer (top-right corner)
        self.timer_label = Label(
            text="00:00:00",
            font_size="24sp",
            color=(0.2, 0.2, 1, 1),  # Same blue color
            font_name="ui/mw.ttf",
            size_hint=(None, None),
            pos_hint={"x": 0.90, "y": 0.87}  # Positioned at the top-right corner
        )
        self.add_widget(self.timer_label)

        # Initialize timer
        self.start_time = datetime.now()

        # Schedule updates
        Clock.schedule_interval(self.update_time_and_date, 1)
        Clock.schedule_interval(self.update_numbers, 0.1)  # Updates numbers every 0.1 seconds
        Clock.schedule_interval(self.update_timer, 1)  # Updates the timer every second

    def update_time_and_date(self, dt):
        """Update the time and date labels."""
        current_time = datetime.now().strftime("%I:%M %p")  # 12-hour format with AM/PM
        self.time_label.text = current_time

        current_date = datetime.now().strftime("%A, %d %b %Y")  # Full day name, day, short month, year
        self.date_label.text = current_date

    def update_numbers(self, dt):
        """Update the 8-digit number display."""
        numbers_left = [
            round(random.uniform(1, 9) + random.uniform(0.000001, 0.999999), 8)
            for _ in range(7)
        ]
        self.number_label_left.text = "\n\n".join(f"{value:.8f}" for value in numbers_left)

        numbers_right = [
            round(random.uniform(1, 9) + random.uniform(0.000001, 0.999999), 8)
            for _ in range(7)
        ]
        self.number_label_right.text = "\n\n".join(f"{value:.8f}" for value in numbers_right)

    def update_timer(self, dt):
        """Update the timer to show elapsed time since UI started."""
        elapsed = datetime.now() - self.start_time
        hours, remainder = divmod(elapsed.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.timer_label.text = f"{hours:02}:{minutes:02}:{seconds:02}"


class JarvisApp(App):
    def build(self):
        Window.size = (800, 600)  # Set initial window size
        return JarvisUI()


def ui_main():
    JarvisApp().run()


ui_main()
