import os
from winotify import Notification, audio

def Alert(Text, subtitle=None, duration="short"):
    # Get the current working directory
    current_directory = os.getcwd()

    # Define the relative path to the icon
    icon_name = "cbe227_fb70e39e9dd94e30bbe30c48b2367dd8~mv2.gif"

    # Construct the full path by combining the current directory with the icon's relative path
    icon_path = os.path.join(current_directory, icon_name)

    # Bold text for app_id using Unicode bold letters
    bold_app_id = "🟢 J.A.R.V.I.S."

    # Create the notification object
    toast = Notification(
        app_id=bold_app_id,
        title=Text,
        msg=subtitle if subtitle else "",
        duration=duration,
        icon=icon_path
    )

    # Set the audio (non-looping)
    toast.set_audio(audio.Default, loop=False)

    # Add a dismiss button
    toast.add_actions(label="Dismiss")  # Simulates a dismiss action

    # Display the toast notification
    toast.show()

