
from webscout import PhindSearch

def Main_Brain(text):
    # Initialize the PhindSearch object
    ai = PhindSearch(quiet=True, is_conversation=None)
    
    # Get the AI response to the provided text
    res = ai.chat(text)  # Assuming res is a string from the AI
    
    # Limit the response to 100 words
    word_limit = 100
    res_words = res.split()[:word_limit]  # Split the response and take the first 100 words
    res_limited = " ".join(res_words)  # Join the words back into a string
  
      # Return the limited response
    return res_limited