import re

def extract_volume_level(output_text):
    """
    Extracts the volume level from the given input text.
    Returns the volume level as an integer if valid, otherwise prints an error.
    """
    # Convert input to lowercase for case-insensitive matching
    output_text = output_text.lower()

    # Define possible patterns for volume commands
    patterns = [
        r"set volume to (\d+)%?",    # Matches "set volume to 50" or "set volume to 50%"
        r"set volume level (\d+)%?",# Matches "set volume level 50" or "set volume level 50%"
        r"volume (\d+)%?",          # Matches "volume 50" or "volume 50%"
    ]

    # Search for a match in the input
    for pattern in patterns:
        match = re.search(pattern, output_text)
        if match:
            # Extract the volume level as an integer
            volume_level = int(match.group(1))
            if 0 <= volume_level <= 100:
                return volume_level
            else:
                print("Error: Volume level must be between 0 and 100.")
                return None

    # If no valid command is found
    print("Error: Invalid command or volume level.")
    return None
