from textblob import TextBlob

def extract_location(user_input):
    blob = TextBlob(user_input)
    words = blob.words
    if "in" in words or "at" in words:
        try:
            if "in" in words:
                index = words.index("in")
            else:
                index = words.index("at")
            # Extract everything after "in" or "at" as the location
            location = " ".join(words[index + 1:])
            return location
        except IndexError:
            return "No location found in the input."
    return "No location keyword ('in', 'at') found in the input."
